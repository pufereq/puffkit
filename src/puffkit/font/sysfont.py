# -*- coding: utf-8 -*-
"""System font module for puffkit."""

from __future__ import annotations

import pygame as pg

from puffkit.font.font import PkFont


class PkSysFont(PkFont):
    """System font class.

    A system font is a font that is available on the system. It is used to render
    text on a surface.
    """

    def __init__(self, name: str, size: int) -> None:
        """Initialize the system font.

        Args:
            name (str): Name of the system font.
            size (int): Size of the font.
        """
        super().__init__(None, size)

        self.name: str = name
        self.size: int = size

        self.font = pg.font.SysFont(self.name, self.size)
