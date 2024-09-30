# -*- coding: utf-8 -*-
"""Size module for puffkit.

This module contains the `PkSize` class, which is used to represent a size in a
2D space. The class is used in the `puffkit` package to represent the size of
objects on the screen.
"""

from __future__ import annotations

from typing import Iterable


class PkSize:
    """Class to represent a size in a 2D space.

    The class is used to represent the size of objects on the screen.
    """

    def __init__(self, w: int | float, h: int | float) -> None:
        """Initialize the size.

        Args:
            w (int | float): Width of the size.
            h (int | float): Height of the size.
        """
        self.w = w
        self.h = h

    @property
    def width(self) -> int | float:
        """Return the width of the size."""
        return self.w

    @property
    def height(self) -> int | float:
        """Return the height of the size."""
        return self.h

    def __str__(self) -> str:
        """Return a human-friendly representation of the size."""
        return f"({self.w}, {self.h})"

    def __repr__(self) -> str:
        """Return a string representation of the size."""
        return f"PkSize({self.w}, {self.h})"

    def __eq__(self, other: PkSize | tuple[int | float, int | float]) -> bool:
        """Compare two sizes for equality.

        Args:
            other (PkSize | tuple[int | float, int | float]): The other size to compare.
        Returns:
            bool: True if the sizes are equal, False otherwise.
        """
        if not isinstance(other, PkSize):
            other = PkSize(*other)
        return self.w == other.w and self.h == other.h

    def __ne__(self, other: PkSize | tuple[int | float, int | float]) -> bool:
        """Compare two sizes for inequality.

        Args:
            other (PkSize): The other size to compare.

        Returns:
            bool: True if the sizes are not equal, False otherwise.
        """
        if not isinstance(other, PkSize):
            other = PkSize(*other)
        return self.w != other.w or self.h != other.h

    def __add__(self, other: PkSize) -> PkSize:
        """Add two sizes together.

        Args:
            other (PkSize): The other size to add.

        Returns:
            PkSize: The sum of the two sizes.
        """
        return PkSize(self.w + other.w, self.h + other.h)

    def __sub__(self, other: PkSize) -> PkSize:
        """Subtract one size from another.

        Args:
            other (PkSize): The other size to subtract.

        Returns:
            PkSize: The difference between the two sizes.
        """
        return PkSize(self.w - other.w, self.h - other.h)

    def __mul__(self, other: int) -> PkSize:
        """Multiply the size by a scalar.

        Args:
            other (int): The scalar to multiply the size by.

        Returns:
            PkSize: The size multiplied by the scalar.
        """
        return PkSize(self.w * other, self.h * other)

    def __truediv__(self, other: int) -> PkSize:
        """Divide the size by a scalar.

        Args:
            other (int): The scalar to divide the size by.

        Returns:
            PkSize: The size divided by the scalar.
        """
        return PkSize(self.w // other, self.h // other)

    def __iter__(self) -> Iterable[int]:
        """Return an iterable of the size components."""
        return iter((self.w, self.h))

    def __getitem__(self, index: int) -> int:
        """Return the size component at the given index."""
        return (self.w, self.h)[index]
