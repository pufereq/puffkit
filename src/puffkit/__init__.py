# -*- coding: utf-8 -*-

# init pygame-ce
import pygame as _pygame

del _pygame

from puffkit.app import PkApp
from puffkit.color.color import ColorValue, PkColor
from puffkit.geometry.coordinate import PkCoordinate
from puffkit.geometry.rect import PkRect
from puffkit.object import PkObject
from puffkit.scene import PkScene
from puffkit.subsurface import PkSubSurface
from puffkit.surface import PkSurface
from puffkit.textures import get_texture
from puffkit.container import PkContainer

__all__ = [
    "PkApp",
    "ColorValue",
    "PkColor",
    "PkCoordinate",
    "PkRect",
    "PkObject",
    "PkScene",
    "PkSubSurface",
    "PkSurface",
    "get_texture",
    "PkContainer",
]
__version__ = "0.11.1"

print(f"puffkit {__version__}")
