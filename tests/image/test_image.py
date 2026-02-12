from unittest.mock import MagicMock
import unittest.mock
import pygame as pg
import pytest

from puffkit.image import PkImage
from puffkit.surface import PkSurface

@pytest.fixture
def mock_image() -> PkImage:
    surface: PkSurface = PkSurface((100, 100))
    return PkImage("test_image", surface)

def test_image_properties(mock_image: PkImage) -> None:
    assert mock_image.id == "test_image"
    assert mock_image.width == 100
    assert mock_image.height == 100
    assert mock_image.filename is None
    assert isinstance(mock_image.image, PkSurface)

@unittest.mock.patch("puffkit.image.image.pg.image.load")
def test_image_from_file(mock_pygame_load: MagicMock) -> None:
    mock_surface = pg.Surface((50, 50))
    mock_pygame_load.return_value = mock_surface

    image = PkImage.from_file("file_image", "path/to/image.png")

    assert image.id == "file_image"
    assert image.width == 50
    assert image.height == 50
    assert image.filename == "path/to/image.png"
    mock_pygame_load.assert_called_once_with("path/to/image.png")

