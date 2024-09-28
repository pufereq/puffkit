# -*- coding: utf-8 -*-
"""Rect module for puffkit."""
from __future__ import annotations

import logging as lg

import pygame

from puffkit.object import PkObject

type RectValue = tuple[float, float, float, float]


class PkRect(PkObject):
    """Rectangle class.

    A rectangle is defined by its top-left corner and its size. It is used to
    represent the position and size of entities, tiles, etc.

    Compatible with `pygame.Rect`, but with no limitation on the coordinates
    and size units.
    """

    def __init__(self, pos: tuple[float, float], size: tuple[float, float]) -> None:
        """Initialize the rectangle.

        Args:
            x (float): The x-coordinate of the rectangle.
            y (float): The y-coordinate of the rectangle.
            w (float): The width of the rectangle.
            h (float): The height of the rectangle.
        """
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.x: float = pos[0]
        self.y: float = pos[1]
        self.w: float = size[0]
        self.h: float = size[1]

    def __iter__(self):
        return iter((self.x, self.y, self.w, self.h))

    def __getitem__(self, index: int) -> float:
        return (self.x, self.y, self.w, self.h)[index]

    def __repr__(self) -> str:
        return f"PkRect({self.topleft}, {self.size})"

    def __str__(self) -> str:
        return f"PkRect({self.topleft}, {self.size})"

    def __eq__(self, other: PkRect | RectValue) -> bool:
        if not isinstance(other, PkRect):
            other = PkRect.from_rectvalue(other)
        return self.topleft == other.topleft and self.size == other.size

    def __ne__(self, other: PkRect | RectValue) -> bool:
        if not isinstance(other, PkRect):
            other = PkRect.from_rectvalue(other)
        return not self == other

    @classmethod
    def from_pygame(cls, rect: pygame.Rect) -> PkRect:
        return cls((rect.x, rect.y), (rect.w, rect.h))

    @classmethod
    def from_rectvalue(cls, rect: RectValue) -> PkRect:
        return cls((rect[0], rect[1]), (rect[2], rect[3]))

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
        return PkRect((self.x, self.y), (self.w, self.h))
