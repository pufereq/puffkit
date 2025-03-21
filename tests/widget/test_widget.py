import pytest
from unittest.mock import MagicMock
from puffkit.widget.widget import PkWidget
from puffkit.geometry import PkRect, RectValue
from typing import Generator


@pytest.fixture
def mock_container() -> Generator[MagicMock, None, None]:
    """
    Provide a mock container with a fixed rectangle and parent surface.
    """
    container = MagicMock()
    container.rect = PkRect(0, 0, 100, 100)
    container.parent_surface = MagicMock()
    yield container


@pytest.mark.parametrize(
    "rect",
    [
        (0, 0, 50, 50),
        PkRect(10, 10, 20, 20),
    ],
)
def test_widget_init_in_bounds(
    mock_container: MagicMock, rect: PkRect | RectValue
) -> None:
    """
    Test that PkWidget initializes properly when coordinates are in bounds.
    """
    widget = PkWidget(mock_container, rect)
    assert widget.rect == rect
    assert widget.abs_rect.x == rect[0] + mock_container.rect.x
    assert widget.abs_rect.y == rect[1] + mock_container.rect.y


@pytest.mark.parametrize(
    "x, y, width, height, expected_err",
    [
        (-1, 0, 10, 10, "Widget is out of bounds."),
        (0, -1, 10, 5, "Widget is out of bounds."),
        (80, 10, 30, 10, "Widget is out of bounds."),
        (10, 90, 10, 20, "Widget is out of bounds."),
    ],
)
def test_widget_init_out_of_bounds(
    mock_container: MagicMock,
    x: int,
    y: int,
    width: int,
    height: int,
    expected_err: str,
) -> None:
    """
    Test that PkWidget constructor raises ValueError for out-of-bounds coordinates.
    """
    rect = PkRect(x, y, width, height)
    with pytest.raises(ValueError) as exc_info:
        PkWidget(mock_container, rect)
    assert expected_err in str(exc_info.value)


def test_widget_update_calls_on_update(mock_container: MagicMock) -> None:
    """
    Test that update method calls on_update with the provided delta.
    """
    widget = PkWidget(mock_container, PkRect(0, 0, 10, 10))
    widget.on_update = MagicMock()
    widget.update(0.016)
    widget.on_update.assert_called_once_with(0.016)


def test_widget_update_event_handling(mock_container: MagicMock) -> None:
    """Test update method handles events by calling specific `on` methods."""
    widget = PkWidget(mock_container, PkRect(0, 0, 10, 10))
    widget.on_key_down = MagicMock()
    widget.on_key_up = MagicMock()
    widget.on_mouse_motion = MagicMock()
    widget.on_mouse_down = MagicMock()
    widget.on_mouse_up = MagicMock()
    widget.on_hover = MagicMock()
    widget.on_mouse_enter = MagicMock()
    widget.on_mouse_leave = MagicMock()

    KEYDOWN = MagicMock()
    KEYUP = MagicMock()
    MOUSEMOTION_IN = MagicMock()
    MOUSEMOTION_OUT = MagicMock()
    MOUSEBUTTONDOWN = MagicMock()
    MOUSEBUTTONUP = MagicMock()

    KEYDOWN.name = "KEYDOWN"
    KEYUP.name = "KEYUP"

    MOUSEMOTION_IN.name = "MOUSEMOTION"
    MOUSEMOTION_IN.pos = (5, 5)
    MOUSEMOTION_OUT.name = "MOUSEMOTION"
    MOUSEMOTION_OUT.pos = (15, 15)

    MOUSEBUTTONDOWN.name = "MOUSEBUTTONDOWN"
    MOUSEMOTION_IN.pos = (5, 5)
    MOUSEBUTTONUP.name = "MOUSEBUTTONUP"
    MOUSEMOTION_IN.pos = (5, 5)

    widget.input(
        events=[
            KEYDOWN,
            KEYUP,
            MOUSEMOTION_IN,
            MOUSEMOTION_OUT,
            MOUSEBUTTONDOWN,
            MOUSEBUTTONUP,
        ],
        keys={},
        mouse_pos=(0, 0),
        mouse_buttons=(False, False, False),
    )
    widget.update(0.016)

    widget.on_key_down.assert_called_once()
    widget.on_key_up.assert_called_once()
    widget.on_mouse_motion.assert_called()
    widget.on_mouse_enter.assert_called_once()
    widget.on_mouse_leave.assert_called_once()
    widget.on_mouse_down.assert_called_once()
    widget.on_mouse_up.assert_called_once()


def test_widget_render_calls_on_render_and_blit(mock_container: MagicMock) -> None:
    """
    Test that render method calls on_render and then blits the widget onto the parent surface.
    """
    widget = PkWidget(mock_container, PkRect(0, 0, 10, 10))
    widget.on_render = MagicMock()
    widget.render()
    widget.on_render.assert_called_once()
    mock_container.parent_surface.blit.assert_called_once_with(
        widget.surface, widget.abs_rect.pos
    )
