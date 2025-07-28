# -*- coding: utf-8 -*-
"""puffkit SubSurface."""

from __future__ import annotations

from puffkit.surface import PkSurface


class PkSubSurface(PkSurface):
    """Base class for subsurfaces.

    A subsurface is a surface that is part of another surface. It can be a
    button, a text box, etc.
    """

    def __init__(
        self,
        parent: PkSurface,
        pos: tuple[int, int],
        size: tuple[int, int] = (0, 0),
    ):
        """Initialize the subsurface.

        Args:
            parent (PkSurface): Parent surface.
            pos (tuple[int, int]): Position of the subsurface.
            size (tuple[int, int], optional): Size of the subsurface.
                Defaults to (0, 0).
        """
        super().__init__(size, pos)

        self.parent = parent

        self.surface = self.parent.internal_surface.subsurface(pos, size)

    def get_parent(self) -> PkSurface:
        return self.parent

    def get_abs_parent(self) -> PkSurface:
        return self.parent.get_abs_parent()
