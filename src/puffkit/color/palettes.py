# -*- coding: utf-8 -*-
"""Color definitions."""

from typing import Final

from puffkit.color.color import PkColor


class PkBasicPalette:
    """A class containing basic color definitions."""

    TRANSPARENT: Final[PkColor] = PkColor(0, 0, 0, 0)
    BLACK: Final[PkColor] = PkColor.from_hex("#000000")
    WHITE: Final[PkColor] = PkColor.from_hex("#ffffff")
    RED: Final[PkColor] = PkColor.from_hex("#ff0000")
    GREEN: Final[PkColor] = PkColor.from_hex("#00ff00")
    BLUE: Final[PkColor] = PkColor.from_hex("#0000ff")
    YELLOW: Final[PkColor] = PkColor.from_hex("#ffff00")
    CYAN: Final[PkColor] = PkColor.from_hex("#00ffff")
    MAGENTA: Final[PkColor] = PkColor.from_hex("#ff00ff")
    ORANGE: Final[PkColor] = PkColor.from_hex("#ff7f00")
    PURPLE: Final[PkColor] = PkColor.from_hex("#7f00ff")
    PINK: Final[PkColor] = PkColor.from_hex("#ff007f")
    BROWN: Final[PkColor] = PkColor.from_hex("#7f3f00")
    GREY: Final[PkColor] = PkColor.from_hex("#808080")
    LIGHT_GREY: Final[PkColor] = PkColor.from_hex("#d3d3d3")
    DARK_GREY: Final[PkColor] = PkColor.from_hex("#a9a9a9")
