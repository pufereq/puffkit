# -*- coding: utf-8 -*-
"""Coordinate module for puffkit.

This module contains the `PkCoordinate` class, which is used to represent a
coordinate in a 2D space. The class is used in the `puffkit` package to
represent positions and sizes of objects on the screen.
"""

from __future__ import annotations

from typing import Iterable


class PkCoordinate:
    """Class to represent a coordinate in a 2D space.

    The class is used to represent positions and sizes of objects on the screen.
    """

    def __init__(self, x: int, y: int) -> None:
        """Initialize the coordinate.

        Args:
            x (int): X coordinate.
            y (int): Y coordinate.
        """
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Return a human-friendly representation of the coordinate."""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Return a string representation of the coordinate."""
        return f"PkCoordinate({self.x}, {self.y})"

    def __add__(self, other: PkCoordinate) -> PkCoordinate:
        """Add two coordinates together.

        Args:
            other (PkCoordinate): The other coordinate to add.

        Returns:
            PkCoordinate: The sum of the two coordinates.

        """
        return PkCoordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other: PkCoordinate) -> PkCoordinate:
        """Subtract one coordinate from another.

        Args:
            other (PkCoordinate): The other coordinate to subtract.

        Returns:
            PkCoordinate: The difference between the two coordinates.
        """
        return PkCoordinate(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int) -> PkCoordinate:
        """Multiply the coordinate by a scalar.

        Args:
            other (int): The scalar to multiply the coordinate by.

        Returns:
            PkCoordinate: The coordinate multiplied by the scalar.
        """
        return PkCoordinate(self.x * other, self.y * other)

    def __truediv__(self, other: int) -> PkCoordinate:
        """Divide the coordinate by a scalar.

        Args:
            other (int): The scalar to divide the coordinate by.

        Returns:
            PkCoordinate: The coordinate divided by the scalar.
        """
        return PkCoordinate(self.x // other, self.y // other)

    def to_tuple(self) -> tuple[int, int]:
        """Return the coordinate as a tuple.

        Returns:
            tuple[int, int]: The coordinate as a tuple.
        """
        return (self.x, self.y)

    def distance_to(self, other: PkCoordinate) -> float:
        """Calculate the distance to another coordinate.

        Args:
            other (PkCoordinate): The other coordinate to calculate the distance to.

        Returns:
            float: The distance to the other coordinate.
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __eq__(self, other: PkCoordinate) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: PkCoordinate) -> bool:
        return self.x != other.x or self.y != other.y

    def __iter__(self) -> Iterable[int]:
        return iter((self.x, self.y))

    def __getitem__(self, index: int) -> int:
        return (self.x, self.y)[index]

    @classmethod
    def from_tuple(cls, coord: tuple[int, int]) -> PkCoordinate:
        """Create a `PkCoordinate` from a tuple.

        Args:
            coord (tuple[int, int]): The tuple to create the coordinate from.

        Returns:
            PkCoordinate: The created coordinate.
        """
        return cls(coord[0], coord[1])