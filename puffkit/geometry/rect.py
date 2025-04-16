# -*- coding: utf-8 -*-
"""Rect module for puffkit."""
from __future__ import annotations

import logging as lg

import pygame

from puffkit.geometry.coordinate import PkCoordinate
from puffkit.geometry.size import PkSize
from puffkit.object import PkObject

type RectValue = tuple[int | float, int | float, int | float, int | float]


class PkRect(PkObject):
    """Rectangle class.

    A rectangle is defined by its top-left corner and its size. It is used to
    represent the position and size of entities, tiles, etc.

    Compatible with `pygame.Rect`, but with no limitation on the coordinates
    and size units.
    """

    def __init__(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
    ) -> None:
        """Initialize the rectangle.

        Args:
            x (float): The x-coordinate of the rectangle.
            y (float): The y-coordinate of the rectangle.
            w (float): The width of the rectangle.
            h (float): The height of the rectangle.
        """
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.x: float = x
        self.y: float = y
        self.w: float = w
        self.h: float = h

    @classmethod
    def from_value(cls, rect: RectValue | PkRect) -> PkRect:
        """Create a rectangle from a tuple of values.

        Args:
            rect (RectValue): A tuple of values representing the rectangle.

        Returns:
            PkRect: The created rectangle.
        """
        if isinstance(rect, PkRect):
            return rect
        return cls(*rect)

    @classmethod
    def from_tuple(cls, rect: RectValue) -> PkRect:
        """# DEPRECATED

        This method is deprecated. Use `from_value` instead.
        """
        raise DeprecationWarning("from_tuple is deprecated. Use from_value instead.")
        return cls(*rect)

    @property
    def tuple(self) -> RectValue:
        return (self.x, self.y, self.w, self.h)

    def __iter__(self):
        return iter((self.x, self.y, self.w, self.h))

    def __getitem__(self, index: int) -> float:
        return (self.x, self.y, self.w, self.h)[index]

    def __repr__(self) -> str:  # pragma: no cover
        return f"PkRect({self.x}, {self.y}, {self.w}, {self.h})"

    def __str__(self) -> str:  # pragma: no cover
        return f"PkRect(x={self.x}, y={self.y}, w={self.w}, h={self.h})"

    def __eq__(self, other: PkRect | RectValue) -> bool:
        if not isinstance(other, PkRect):
            other = PkRect(*other)
        return (
            self.x == other.x
            and self.y == other.y
            and self.w == other.w
            and self.h == other.h
        )

    @classmethod
    def from_pygame(cls, rect: pygame.Rect) -> PkRect:
        return cls(rect.x, rect.y, rect.w, rect.h)

    @property
    def pos(self) -> tuple[float, float]:
        return (self.x, self.y)

    @pos.setter
    def pos(self, value: tuple[float, float]) -> None:
        self.x, self.y = value

    @property
    def width(self) -> float:
        return self.w

    @width.setter
    def width(self, value: float) -> None:
        self.w = value

    @property
    def height(self) -> float:
        return self.h

    @height.setter
    def height(self, value: float) -> None:
        self.h = value

    @property
    def top(self) -> float:
        return self.y

    @top.setter
    def top(self, value: float) -> None:
        self.y = value

    @property
    def bottom(self) -> float:
        return self.y + self.h

    @bottom.setter
    def bottom(self, value: float) -> None:
        self.y = value - self.h

    @property
    def left(self) -> float:
        return self.x

    @left.setter
    def left(self, value: float) -> None:
        self.x = value

    @property
    def right(self) -> float:
        return self.x + self.w

    @right.setter
    def right(self, value: float) -> None:
        self.x = value - self.w

    @property
    def size(self) -> tuple[float, float]:
        return (self.w, self.h)

    @size.setter
    def size(self, value: tuple[float, float]) -> None:
        self.w, self.h = value

    @property
    def center(self) -> tuple[float, float]:
        return (self.x + self.w / 2, self.y + self.h / 2)

    @center.setter
    def center(self, value: tuple[float, float]) -> None:
        self.x, self.y = value[0] - self.w / 2, value[1] - self.h / 2

    @property
    def topleft(self) -> tuple[float, float]:
        return (self.x, self.y)

    @topleft.setter
    def topleft(self, value: tuple[float, float]) -> None:
        self.x, self.y = value

    @property
    def topright(self) -> tuple[float, float]:
        return (self.x + self.w, self.y)

    @topright.setter
    def topright(self, value: tuple[float, float]) -> None:
        self.x, self.y = value[0] - self.w, value[1]

    @property
    def midtop(self) -> tuple[float, float]:
        return (self.x + self.w / 2, self.y)

    @midtop.setter
    def midtop(self, value: tuple[float, float]) -> None:
        self.x, self.y = value[0] - self.w / 2, value[1]

    @property
    def midleft(self) -> tuple[float, float]:
        return (self.x, self.y + self.h / 2)

    @midleft.setter
    def midleft(self, value: tuple[float, float]) -> None:
        self.x, self.y = value[0], value[1] - self.h / 2

    @property
    def midbottom(self) -> tuple[float, float]:
        return (self.x + self.w / 2, self.y + self.h)

    @midbottom.setter
    def midbottom(self, value: tuple[float, float]) -> None:
        self.x, self.y = value[0] - self.w / 2, value[1] - self.h

    @property
    def midright(self) -> tuple[float, float]:
        return (self.x + self.w, self.y + self.h / 2)

    @midright.setter
    def midright(self, value: tuple[float, float]) -> None:
        self.x, self.y = value[0] - self.w, value[1] - self.h / 2

    @property
    def bottomleft(self) -> tuple[float, float]:
        return (self.x, self.y + self.h)

    @bottomleft.setter
    def bottomleft(self, value: tuple[float, float]) -> None:
        self.x, self.y = value[0], value[1] - self.h

    @property
    def bottomright(self) -> tuple[float, float]:
        return (self.x + self.w, self.y + self.h)

    @bottomright.setter
    def bottomright(self, value: tuple[float, float]) -> None:
        self.x, self.y = value[0] - self.w, value[1] - self.h

    def collidepoint(self, point: tuple[float, float]) -> bool:
        x, y = point

        return self.left < x < self.right and self.top < y < self.bottom

    def colliderect(self, rect: PkRect) -> bool:
        return (
            self.left < rect.right
            and self.right > rect.left
            and self.top < rect.bottom
            and self.bottom > rect.top
        )

    def copy(self) -> PkRect:
        return PkRect(self.x, self.y, self.w, self.h)
