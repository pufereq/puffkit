# -*- coding: utf-8 -*-
"""Font module for puffkit."""
from __future__ import annotations

import pygame as pg

from puffkit.color.color import PkColor
from puffkit.object import PkObject


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

    def render(
        self,
        text: str,
        antialias: bool = True,
        color: PkColor = PkColor(255, 255, 255),
        bgcolor: PkColor | None = None,
        max_width: int | None = None,
    ) -> PkSurface:
        from puffkit.surface import PkSurface

        """Render text to a surface.

        Args:
            text (str): Text to render.
            antialias (bool): Whether to use antialiasing.
            color (PkColor): Text color.
            bg_color (PkColor, optional): Background color. Defaults to None.

        Returns:
            PkSurface: Surface with the rendered text.
        """
        self.logger.debug(f"Rendering text: {text}")

        max_width = max_width if max_width is not None else 0

        text_surface = self.font.render(
            text,
            antialias,
            tuple(color),
            tuple(bgcolor) if bgcolor is not None else None,
            max_width,
        )

        return PkSurface.from_pygame(text_surface)
