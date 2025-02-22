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
