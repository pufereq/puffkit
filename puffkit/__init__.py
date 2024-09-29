# -*- coding: utf-8 -*-

__version__ = "0.1.0"

print(f"puffkit {__version__}")

from puffkit.app import PkApp
from puffkit.color import palettes
from puffkit.color.color import ColorValue, PkColor
from puffkit.coordinate import PkCoordinate
from puffkit.object import PkObject
from puffkit.rect import PkRect
from puffkit.scene import PkScene
from puffkit.subsurface import PkSubSurface
from puffkit.surface import PkSurface
from puffkit.textures import get_texture
