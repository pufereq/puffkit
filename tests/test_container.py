import pytest
from unittest.mock import MagicMock
from typing import Union
from puffkit import PkContainer
from puffkit.geometry import PkRect, RectValue


@pytest.mark.parametrize(
    "rect, expect_error",
    [
        ((-1, 0, 50, 50), True),
        ((0, -1, 50, 50), True),
        (
            (80, 0, 30, 50),
            True,
        ),  # right would be 110, out of bounds if parent width is 100
        (
            (0, 80, 50, 30),
            True,
        ),  # bottom would be 110, out of bounds if parent height is 100
        ((0, 0, 50, 50), False),
        (PkRect(10, 10, 20, 20), False),
    ],
)
def test_pkcontainer_init_edge_cases(
    rect: PkRect | RectValue, expect_error: bool
) -> None:
    """
    Test PkContainer initialization with various rectangle positions to ensure
    ValueError is raised when out of bounds and no error otherwise.
    """
    mock_app = MagicMock()
    mock_surface = MagicMock()
    mock_surface.get_width.return_value = 100
    mock_surface.get_height.return_value = 100

    rect_value: PkRect | RectValue = rect
    if expect_error:
        with pytest.raises(ValueError):
            PkContainer(mock_app, mock_surface, "test_container", rect_value)
    else:
        container = PkContainer(mock_app, mock_surface, "test_container", rect_value)
        assert container.rect.x == rect[0]
        assert container.rect.y == rect[1]
        assert container.rect.width == rect[2]
        assert container.rect.height == rect[3]


@pytest.mark.parametrize("draw_outline", [True, False])
def test_pkcontainer_outline(draw_outline: bool) -> None:
    """Test creation of outline_surface when draw_outline is True."""
    mock_app = MagicMock()
    mock_surface = MagicMock()
    mock_surface.get_width.return_value = 100
    mock_surface.get_height.return_value = 100
    container = PkContainer(
        mock_app,
        mock_surface,
        "outline_test",
        (0, 0, 50, 50),
        draw_outline=draw_outline,
    )
    if draw_outline:
        assert hasattr(container, "outline_surface")
    else:
        assert not hasattr(container, "outline_surface")


def test_pkcontainer_add_remove_widget() -> None:
    """Test adding and removing widgets from the container."""
    mock_app = MagicMock()
    mock_surface = MagicMock()
    mock_surface.get_width.return_value = 100
    mock_surface.get_height.return_value = 100
    mock_widget = MagicMock()
    container = PkContainer(mock_app, mock_surface, "widget_test", (0, 0, 50, 50))
    container.add_widget(mock_widget)
    assert len(container.children) == 1
    container.remove_widget(mock_widget)
    assert len(container.children) == 0


def test_pkcontainer_update() -> None:
    """Test the update method of the container to ensure child widgets receive updates."""
    mock_app = MagicMock()
    mock_surface = MagicMock()
    mock_surface.get_width.return_value = 100
    mock_surface.get_height.return_value = 100

    mock_widget = MagicMock()
    container = PkContainer(mock_app, mock_surface, "update_test", (0, 0, 50, 50))
    container.add_widget(mock_widget)

    container._input = {
        "events": [],
        "keys": [],
        "mouse_pos": (0, 0),
        "mouse_buttons": (False, False, False),
    }
    container.update(0.016)
    mock_widget.input.assert_called_once()
    mock_widget.update.assert_called_once()


def test_pkcontainer_render() -> None:
    """Test the render method to ensure children are rendered."""
    mock_app = MagicMock()
    mock_surface = MagicMock()
    mock_surface.get_width.return_value = 100
    mock_surface.get_height.return_value = 100

    mock_widget = MagicMock()
    container = PkContainer(
        mock_app, mock_surface, "render_test", (0, 0, 50, 50), draw_outline=True
    )
    container.add_widget(mock_widget)
    container.render()
    mock_surface.blit.assert_called()
    mock_widget.render.assert_called_once()
