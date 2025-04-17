from typing import Any
import pytest
from unittest.mock import Mock
from puffkit import PkApp
from puffkit.color import PkBasicPalette, PkColor
from puffkit.geometry import PkRect
from puffkit.container import PkContainer
from puffkit.widget.button_widget import PkButtonWidget
from puffkit.event import PkEvent


@pytest.fixture(scope="module")
def app() -> PkApp:
    """Fixture to create a PkApp instance."""

    class InnerPkApp(PkApp):
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            super().__init__(*args, **kwargs)

    app = InnerPkApp(
        "test_app",
        "0.1.0",
        (64, 64),
        {},
        (64, 64),
    )
    return app


@pytest.fixture
def mock_container(app: PkApp) -> Mock:
    """Fixture to create a mock container."""
    mock = Mock(spec=PkContainer)
    mock.app = app
    mock.rect = PkRect(0, 0, 200, 150)
    return mock


@pytest.fixture
def button_widget(mock_container: Mock):
    """Fixture to create a PkButtonWidget instance."""
    return PkButtonWidget(
        id_="test_button",
        container=mock_container,
        rect=PkRect(0, 0, 100, 50),
        label="Click Me",
        on_click=Mock(),
        on_hover=Mock(),
        disabled=False,
        font_id="default",
        background_color=PkBasicPalette.GREY,
        background_color_disabled=PkBasicPalette.DARK_GREY,
        background_color_pressed=PkBasicPalette.LIGHT_GREY,
        background_color_hovered=PkBasicPalette.BLUE,
        text_color=PkBasicPalette.WHITE,
        text_align="center",
        border_radius=5,
    )


@pytest.mark.parametrize(
    "rect, label, on_click, on_hover, disabled, font_id, background_color, "
    "background_color_disabled, background_color_pressed, "
    "background_color_hovered, text_color, text_align, border_radius",
    [
        [
            PkRect(0, 0, 100, 50),
            "Click Me",
            Mock(),
            Mock(),
            False,
            "default",
            PkBasicPalette.GREY,
            PkBasicPalette.DARK_GREY,
            PkBasicPalette.LIGHT_GREY,
            PkBasicPalette.BLUE,
            PkBasicPalette.WHITE,
            "center",
            5,
        ],
        [
            PkRect(10, 10, 80, 40),
            "Submit",
            Mock(),
            Mock(),
            True,
            "Arial",
            PkBasicPalette.RED,
            PkBasicPalette.CYAN,
            PkBasicPalette.GREEN,
            PkBasicPalette.BLUE,
            PkBasicPalette.BLACK,
            "left",
            10,
        ],
        [
            PkRect(20, 20, 60, 30),
            "Cancel",
            Mock(),
            Mock(),
            False,
            "Verdana",
            (0, 0, 255),
            (0, 0, 128),
            (173, 216, 230),
            (0, 0, 255),
            (255, 255, 255),
            "right",
            0,
        ],
    ],
)
def test_button_initialization(
    mock_container: Mock,
    rect: PkRect,
    label: str,
    on_click: Mock,
    on_hover: Mock,
    disabled: bool,
    font_id: str,
    background_color: PkColor,
    background_color_disabled: PkColor,
    background_color_pressed: PkColor,
    background_color_hovered: PkColor,
    text_color: PkColor,
    text_align: str,
    border_radius: int,
):
    """Test the initialization of the button widget."""
    button_widget = PkButtonWidget(
        id_="test_button",
        container=mock_container,
        rect=rect,
        label=label,
        on_click=on_click,
        on_hover=on_hover,
        disabled=disabled,
        font_id=font_id,
        background_color=background_color,
        background_color_disabled=background_color_disabled,
        background_color_pressed=background_color_pressed,
        background_color_hovered=background_color_hovered,
        text_color=text_color,
        text_align=text_align,
        border_radius=border_radius,
    )


def test_button_on_click_action(button_widget: PkButtonWidget):
    """Test the on_click action of the button."""
    button_widget._pressed = True
    button_widget.on_mouse_up(Mock(spec=PkEvent))
    button_widget.action_on_click.assert_called_once()


def test_button_on_hover_action(button_widget: PkButtonWidget):
    """Test the on_hover action of the button."""
    button_widget.on_hover(Mock(spec=PkEvent))
    button_widget.action_on_hover.assert_called_once()


@pytest.mark.parametrize(
    "disabled, expected_color",
    [
        (True, PkBasicPalette.DARK_GREY),
        (False, PkBasicPalette.GREY),
    ],
)
def test_button_render_disabled_state(
    button_widget: PkButtonWidget, disabled: bool, expected_color: PkColor
):
    """Test the rendering of the button in disabled and normal states."""
    button_widget._disabled = disabled
    button_widget.surface = Mock()
    button_widget.on_render()
    button_widget.surface.draw_rect.assert_called_with(
        PkRect(0, 0, 100, 50),
        expected_color,
        0,
        5,
    )


@pytest.mark.parametrize(
    "state, expected_color",
    [
        ("pressed", PkBasicPalette.LIGHT_GREY),
        ("hovered", PkBasicPalette.BLUE),
        ("normal", PkBasicPalette.GREY),
    ],
)
def test_button_render_states(
    button_widget: PkButtonWidget, state: bool, expected_color: PkColor
):
    """Test the rendering of the button in different states."""
    button_widget.surface = Mock()
    button_widget._disabled = False

    button_widget._focused = state == "pressed"
    button_widget._pressed = state == "pressed"

    button_widget._hovered = state == "hovered"

    button_widget.on_render()
    button_widget.surface.draw_rect.assert_called_with(
        PkRect(0, 0, 100, 50),
        expected_color,
        0,
        5,
    )


@pytest.mark.parametrize(
    "delta, disabled",
    [
        (0.016, False),
        (0.033, False),
        (0.05, False),
        (0.016, True),
        (0.033, True),
        (0.05, True),
    ],
)
def test_button_update(button_widget: PkButtonWidget, delta: float, disabled: bool):
    """Test the update method of the button widget."""
    button_widget._disabled = disabled
    button_widget.update(delta)
    assert button_widget._pressed is False
    assert button_widget._hovered is False


@pytest.mark.parametrize(
    "disabled",
    [
        (True),
        (False),
    ],
)
def test_button_on_mouse_up(button_widget: PkButtonWidget, disabled: bool):
    """Test the on_mouse_up method of the button widget."""
    button_widget._disabled = disabled
    button_widget._pressed = True  # simulate button being pressed
    button_widget.on_mouse_up(Mock(spec=PkEvent, kwargs={"pos": (5, 5)}))
    if disabled:
        button_widget.action_on_click.assert_not_called()
    else:
        button_widget.action_on_click.assert_called_once()
    assert button_widget._pressed is True


@pytest.mark.parametrize(
    "disabled, event",
    [
        (True, Mock(spec=PkEvent, kwargs={"pos": (5, 5)})),
        (False, Mock(spec=PkEvent, kwargs={"pos": (5, 5)})),
    ],
)
def test_button_on_hover(button_widget: PkButtonWidget, disabled: bool, event: Mock):
    """Test the on_hover method of the button widget."""
    button_widget._disabled = disabled
    button_widget.on_hover(event)
    if disabled:
        button_widget.action_on_hover.assert_not_called()
    else:
        button_widget.action_on_hover.assert_called_once()
