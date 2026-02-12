# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import TYPE_CHECKING, override

import pygame as pg

from puffkit.geometry import PkSize
from puffkit.object import PkObject
from puffkit.surface import PkSurface


class PkImage(PkObject):
    """Represents an image in puffkit."""

    def __init__(
        self,
        id_: str,
        image: PkSurface,
    ) -> None:
        """Initialize a PkImage.

        Args:
            id_ (str): The unique identifier for the image.
            image (PkSurface): The surface representing the image.
        """
        super().__init__(True)

        self.id: str = id_
        self.image: PkSurface = image
        self.filename: str | None = None

    @classmethod
    def from_file(cls, id_: str, file_path: str) -> PkImage:
        """Create a PkImage from a file.

        Args:
            id_ (str): The unique identifier for the image.
            file_path (str): The path to the image file.

        Returns:
            PkImage: The created PkImage instance.
        """
        image_surface: PkSurface = PkSurface.from_pygame(
            pg.image.load(file_path).convert_alpha()
        )
        class_ = cls(id_, image_surface)
        class_.filename = file_path
        return class_

    @override
    def __repr__(self) -> str:  # pragma: no cover
        return f"PkImage(id_={self.id}, size={self.size})"

    @override
    def __str__(self) -> str:  # pragma: no cover
        return f"PkImage(id_={self.id}, size={self.size})"

    @property
    def width(self) -> int | float:  # pragma: no cover
        return self.image.width

    @property
    def height(self) -> int | float:  # pragma: no cover
        return self.image.height

    @property
    def size(self) -> PkSize:  # pragma: no cover
        return self.image.size
