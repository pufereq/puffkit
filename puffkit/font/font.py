# -*- coding: utf-8 -*-
"""Font module for puffkit."""
from __future__ import annotations
from typing import TYPE_CHECKING

import pygame as pg

from puffkit.color.color import PkColor
from puffkit.object import PkObject

if TYPE_CHECKING:  # pragma: no cover
    # PkSurface is still called, imported in PkFont.render()
    from puffkit import PkSurface


class PkFont(PkObject):
    """Font class.

    A font is a typeface and its size. It is used to render text on a surface.
    """

    def __init__(self, path: str | None, size: int) -> None:
        """Initialize the font.

        Args:
            path (str | None): Path to the font file. If None, use the default font.
            size (int): Size of the font.
        """
        super().__init__()

        self.path: str = path
        self.size: int = size

        self.font = pg.font.Font(self.path, self.size)

    @property
    def label(self) -> str:
        """Get the font label."""
        return self.font.name

    @property
    def align(self) -> int:
        """Get the text alignment."""
        return self.font.align

    @align.setter
    def align(self, align: int) -> None:
        """Set the text alignment."""
        self.font.align = align

    def render(
        self,
        text: str,
        antialias: bool = True,
        color: PkColor = PkColor(255, 255, 255),
        bgcolor: PkColor | None = None,
        max_width: int | None = None,
        align: int = 0,
    ) -> PkSurface:
        from puffkit.surface import PkSurface

        """Render text to a surface.

        Args:
            text (str): Text to render.
            antialias (bool): Whether to use antialiasing.
            color (PkColor): Text color.
            bg_color (PkColor, optional): Background color. Defaults to None.
            max_width (int, optional): Maximum width of the text. Defaults to None.
            align (int, optional): Text alignment. Defaults to 0.

        Returns:
            PkSurface: Surface with the rendered text.
        """

        max_width = max_width if max_width is not None else 0

        self.align = align
        text_surface = self.font.render(
            text,
            antialias,
            tuple(color),
            tuple(bgcolor) if bgcolor is not None else None,
            max_width,
        )
        self.align = pg.FONT_LEFT

        return PkSurface.from_pygame(text_surface)
