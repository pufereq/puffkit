from typing import Any
from unittest import mock

import pygame as pg
import pytest

from puffkit.color.palettes import PkBasicPalette
from puffkit.surface import PkSurface
from puffkit.textures import get_texture


@pytest.mark.parametrize(
    "path, texture_size",
    [
        ("valid_texture_path.png", (2, 2)),
        ("invalid_texture_path.png", (2, 2)),
    ],
)
@mock.patch("puffkit.textures.pg.image.load")
@mock.patch("puffkit.textures.PkSurface.from_pygame")
def test_get_texture(
    mock_from_pygame: Any, mock_pg_load: Any, path: str, texture_size: tuple[int, int]
):
    """Test the get_texture function with valid and invalid paths."""
    mock_from_pygame.return_value = PkSurface(texture_size)
    if path.startswith("valid"):
        mock_pg_load.return_value = mock.Mock()
    else:
        mock_pg_load.side_effect = FileNotFoundError

    texture = get_texture(path, texture_size)

    if path.startswith("valid"):
        mock_pg_load.assert_called_with(path)
        mock_from_pygame.assert_called()
        assert isinstance(texture, PkSurface)
    else:
        mock_pg_load.assert_called_with(path)
        mock_from_pygame.assert_called()
        assert texture.size == texture_size

        assert isinstance(texture, PkSurface)
