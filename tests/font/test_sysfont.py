from unittest import mock

import pygame as pg
import pytest

from puffkit.font.sysfont import PkSysFont

# -*- coding: utf-8 -*-
"""Tests for the PkSysFont class."""


@pytest.mark.parametrize(
    "name, size",
    [
        ("Arial", 12),
        ("Times New Roman", 16),
        ("Courier New", 10),
    ],
)
def test_pksysfont_initialization(name: str, size: int) -> None:
    """Test the initialization of PkSysFont.

    Args:
        name (str): Name of the system font.
        size (int): Size of the font.
    """
    with mock.patch("pygame.font.SysFont") as mock_sysfont:
        font = PkSysFont(name, size)
        mock_sysfont.assert_called_once_with(name, size)
        assert font.name == name
        assert font.size == size
        assert font.font == mock_sysfont.return_value
