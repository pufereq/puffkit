# -*- coding: utf-8 -*-
"""Textures module.

This module contains the textures used in the game.
"""

from __future__ import annotations

import logging as lg

import pygame as pg

from puffkit.color.palettes import PkBasicPalette
from puffkit.surface import PkSurface


def get_texture(path: str, texture_size: tuple[int, int]) -> PkSurface:
    """Load a texture from a file.

    Args:
        path (str): Path to the texture file.
        texture_size (tuple[int, int]): Size of the texture.

    Returns:
        PkSurface: Texture surface.
    """
    logger = lg.getLogger(f"{__name__}.get_texture")
    logger.info(f"Loading texture from file: {path}")

    try:
        texture = PkSurface.from_pygame(pg.image.load(path))
    except FileNotFoundError:
        logger.error(f"Error loading texture from file: {path}")
        # return surface with a black-and-magenta checkerboard pattern
        texture = PkSurface((2, 2))
        texture.fill(PkBasicPalette.BLACK)
        texture.fill(PkBasicPalette.MAGENTA, (1, 0, 1, 1))
        texture.fill(PkBasicPalette.MAGENTA, (0, 1, 1, 1))
    finally:
        texture = texture.scale(texture_size)
        return texture
