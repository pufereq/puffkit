from itertools import product
from unittest.mock import MagicMock, NonCallableMagicMock
import unittest.mock
import pygame as pg
import pytest

from puffkit.app import PkApp
from puffkit.image import PkImage
from puffkit.widget.image_widget import PkImageWidget
from puffkit.surface import PkSurface
from puffkit.geometry import PkRect
from puffkit.container import PkContainer

@pytest.fixture
def image_widget() -> PkImageWidget:
    surface: PkSurface = PkSurface((100, 100))
    mock_image = MagicMock(spec=PkImage)
    mock_image.id = "test_image"
    mock_image.image = surface
    mock_image.width = 100
    mock_image.height = 100

    mock_container = MagicMock(spec=PkContainer)
    mock_container.rect = PkRect(0, 0, 100, 100)
    rect = PkRect(0, 0, 100, 100)

    return PkImageWidget(
        id_="test_widget",
        container=mock_container,
        image=mock_image,
        rect=rect,
        resize_mode="stretch",
    )


def test_image_widget_init(image_widget: PkImageWidget) -> None:
    assert image_widget.id == "test_widget"
    assert image_widget.container == image_widget.container
    assert image_widget.image == image_widget.image
    assert image_widget.rect == image_widget.rect
    assert image_widget.resize_mode == "stretch"
    assert isinstance(image_widget.resized_image, PkImage)


def test_image_widget_invalid_resize_mode(image_widget: PkImageWidget) -> None:
    with pytest.raises(ValueError):
        _ = PkImageWidget(
            id_="invalid_widget",
            container=image_widget.container,
            image=image_widget.image,
            rect=image_widget.rect,
            resize_mode="INVALID_MODE",
        )


@pytest.mark.parametrize("resize_mode, new_size", product(
    [None, "stretch", "fit", "fill", "tile"],
    [(200, 150), (150, 200), (50, 50), (300, 300)],
))
def test_image_widget_resize_mode(image_widget: PkImageWidget, resize_mode: str | None, new_size: tuple[int, int]) -> None:
    image_widget.rect = PkRect(0, 0, new_size[0], new_size[1])
    resized_image = image_widget._resize_image(resize_mode)
    assert isinstance(resized_image, PkImage)
    assert resized_image.id == image_widget.image.id

    if resize_mode == "stretch":
        assert resized_image.image.size == new_size
    elif resize_mode == "fit":
        assert resized_image.image.width <= new_size[0]
        assert resized_image.image.height <= new_size[1]
    elif resize_mode == "fill":
        assert resized_image.image.width >= new_size[0]
        assert resized_image.image.height >= new_size[1]
    elif resize_mode == "tile":
        assert resized_image.image.size == new_size
    elif resize_mode is None:
        assert resized_image.image.size == (100, 100)  # original size

def test_image_widget_resize_mode_invalid(image_widget: PkImageWidget) -> None:
    with pytest.raises(ValueError):
        image_widget._resize_image("INVALID_MODE")

def test_image_widget_on_click_no_hook(image_widget: PkImageWidget) -> None:
    mock_event = MagicMock()

    image_widget.click_hook = NonCallableMagicMock()
    image_widget.on_click(mock_event)  # should do nothing
    image_widget.click_hook.assert_not_called()

def test_image_widget_on_click_with_hook(image_widget: PkImageWidget) -> None:
    mock_event = MagicMock()

    image_widget.click_hook = MagicMock(return_value=None)
    image_widget.on_click(mock_event)
    image_widget.click_hook.assert_called_once_with(image_widget, mock_event)





def test_image_widget_on_hover_no_hook(image_widget: PkImageWidget) -> None:
    mock_event = MagicMock()

    image_widget.hover_hook = NonCallableMagicMock()
    image_widget.on_hover(mock_event)  # should do nothing
    image_widget.hover_hook.assert_not_called()

def test_image_widget_on_hover_with_hook(image_widget: PkImageWidget) -> None:
    mock_event = MagicMock()

    image_widget.hover_hook = MagicMock(return_value=None)
    image_widget.on_hover(mock_event)
    image_widget.hover_hook.assert_called_once_with(image_widget, mock_event)


def test_image_widget_on_render(image_widget: PkImageWidget) -> None:
    # ensure no exceptions are raised
    image_widget.on_render()
