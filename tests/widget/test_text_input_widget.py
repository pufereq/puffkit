import pytest
import pygame
from unittest.mock import Mock, MagicMock
from puffkit.widget.text_input_widget import PkTextInputWidget
from puffkit.geometry import PkRect
from puffkit.font import PkFont
from puffkit import PkApp, PkSurface

# from puffkit.color import PkBasicPalette
from puffkit import PkContainer


@pytest.fixture
def mock_container() -> PkContainer:
    pygame.init()
    app = MagicMock(spec=PkApp)
    app.fonts = {"default": PkFont(None, 12)}

    parent_surface = MagicMock(spec=PkSurface)
    parent_surface.get_width.return_value = 200
    parent_surface.get_height.return_value = 100
    container = PkContainer(app, parent_surface, "test_container", (0, 0, 200, 50))
    return container


@pytest.fixture
def text_input_widget(mock_container):
    """Fixture to create a PkTextInputWidget instance."""
    rect = PkRect(0, 0, 200, 50)
    return PkTextInputWidget(
        id_="test_widget",
        container=mock_container,
        rect=rect,
        text="",
        max_length=10,
        placeholder="Enter text",
    )


@pytest.mark.parametrize(
    "initial_text, key_event, expected_text",
    [
        ("", Mock(key="a", unicode="a"), "a"),
        ("hello", Mock(key="backspace", unicode=""), "hell"),
        ("hello", Mock(key="delete", unicode=""), "hello"),
        ("hello", Mock(key="left", unicode=""), "hello"),
        ("hello", Mock(key="right", unicode=""), "hello"),
        ("hello", Mock(key="home", unicode=""), "hello"),
        ("hello", Mock(key="end", unicode=""), "hello"),
    ],
)
def test_on_key_down(text_input_widget, initial_text, key_event, expected_text):
    """Test the on_key_down method with various key events."""
    text_input_widget.focused = True
    text_input_widget.text = initial_text
    text_input_widget.cursor = len(initial_text)
    text_input_widget.on_key_down(key_event)
    assert text_input_widget.text == expected_text


def test_on_key_down_no_focus(text_input_widget):
    """Test the on_key_down method when the widget is not focused."""
    text_input_widget.focused = False
    initial_text = "hello"
    text_input_widget.text = initial_text
    text_input_widget.cursor = len(initial_text)
    text_input_widget.on_key_down(Mock(key="a", unicode="a"))
    assert text_input_widget.text == initial_text


def test_on_key_down_action(text_input_widget):
    """Test the on_key_down method with an action key."""
    text_input_widget.focused = True
    text_input_widget.action_on_change = Mock()
    initial_text = "hello"
    text_input_widget.text = initial_text
    text_input_widget.cursor = len(initial_text)
    text_input_widget.on_key_down(Mock(key="enter", unicode=""))
    assert text_input_widget.text == initial_text
    text_input_widget.action_on_change.assert_called_once_with(text_input_widget)


def test_on_focus(text_input_widget):
    """Test the on_focus method."""
    mock_event = Mock()

    # widget not disabled
    text_input_widget.action_on_focus = Mock()
    text_input_widget.on_focus(mock_event)
    assert text_input_widget.cursor_blink_timer == 0
    assert text_input_widget.action_on_focus.called

    # widget disabled
    text_input_widget.disabled = True
    text_input_widget.cursor_blink_timer = 0.5
    text_input_widget.action_on_focus = Mock()
    text_input_widget.on_focus(mock_event)
    assert text_input_widget.cursor_blink_timer == 0.5  # ensure the timer is not reset
    text_input_widget.action_on_focus.assert_not_called()


def test_on_unfocus(text_input_widget):
    """Test the on_unfocus method."""
    mock_event = Mock()

    # widget not disabled
    text_input_widget.action_on_unfocus = Mock()
    text_input_widget.on_unfocus(mock_event)
    text_input_widget.action_on_unfocus.assert_called_once_with(text_input_widget)

    # widget disabled
    text_input_widget.disabled = True
    text_input_widget.action_on_unfocus = Mock()
    text_input_widget.on_unfocus(mock_event)
    text_input_widget.action_on_unfocus.assert_not_called()


def test_on_update(text_input_widget):
    """Test the on_update method."""
    text_input_widget.focused = True
    text_input_widget.cursor_blink_interval = 0.5

    # simulate the cursor blink timer
    text_input_widget.on_update(0.3)
    assert text_input_widget.cursor_blink_timer == 0.3

    # simulate the cursor blink interval being reached
    text_input_widget.on_update(0.5)
    assert text_input_widget.cursor_blink_timer == 0

    # pass if disabled
    text_input_widget.disabled = True
    text_input_widget.cursor_blink_timer = 0.5
    text_input_widget.on_update(0.5)
    assert text_input_widget.cursor_blink_timer == 0.5  # ensure the timer is not reset


def test_on_render(text_input_widget):
    """Test the on_render method."""
    text_input_widget.text = "hello"
    text_input_widget.focused = True
    text_input_widget.on_render()


def test_invalid_padding_raises_value_error(mock_container):
    """Test that invalid padding raises a ValueError."""
    rect = PkRect(0, 0, 10, 10)
    with pytest.raises(ValueError, match="Padding is too large for the input field"):
        PkTextInputWidget(
            id_="test_widget",
            container=mock_container,
            rect=rect,
            padding=6,
        )
