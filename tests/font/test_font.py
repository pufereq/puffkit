# -*- coding: utf-8 -*-
"""Tests for the PkFont class."""
from unittest import mock

import pygame as pg
import pytest

from puffkit.color.color import PkColor
from puffkit.font.font import PkFont
from puffkit.surface import PkSurface


@pytest.fixture
def mock_pygame_font():
    pg.font.init()
    with mock.patch("pygame.font.Font") as mock_font:
        yield mock_font


@pytest.mark.parametrize(
    "path, size",
    [
        (None, 12),
        ("path/to/font.ttf", 24),
    ],
)
def test_pkfont_initialization(mock_pygame_font, path: str | None, size: int) -> None:
    """Test the initialization of PkFont."""
    font = PkFont(path, size)
    assert font.path == path
    assert font.size == size
    mock_pygame_font.assert_called_once_with(path, size)


@pytest.mark.parametrize(
    "text, antialias, color, bgcolor, max_width",
    [
        ("Hello, World!", True, PkColor(255, 255, 255), None, None),
        ("Test", False, PkColor(0, 0, 0), PkColor(255, 255, 255), 100),
    ],
)
def test_pkfont_render(
    mock_pygame_font,
    text: str,
    antialias: bool,
    color: PkColor,
    bgcolor: PkColor | None,
    max_width: int | None,
) -> None:
    """Test the render method of PkFont."""
    font = PkFont(None, 12)
    mock_surface = mock.Mock()
    mock_pygame_font.return_value.render.return_value = mock_surface

    with mock.patch(
        "puffkit.surface.PkSurface.from_pygame", return_value=mock_surface
    ) as mock_from_pygame:
        result = font.render(text, antialias, color, bgcolor, max_width)
        mock_pygame_font.return_value.render.assert_called_once_with(
            text,
            antialias,
            tuple(color),
            tuple(bgcolor) if bgcolor is not None else None,
            max_width if max_width is not None else 0,
        )
        mock_from_pygame.assert_called_once_with(mock_surface)
        assert result == mock_surface


def test_pkfont_align_getter(mock_pygame_font) -> None:
    """Test the align property getter of PkFont."""
    font = PkFont(None, 12)
    assert font.align == font.font.align


def test_pkfont_align_setter(mock_pygame_font) -> None:
    """Test the align property setter of PkFont."""
    font = PkFont(None, 12)
    font.align = 1
    assert font.align == 1
    assert font.font.align == 1
    font.font.align = 2
    assert font.align == 2
    assert font.font.align == 2
