# -*- coding: utf-8 -*-

from __future__ import annotations

import colorsys
from typing import Iterator

import pygame

type ColorValue = tuple[int, int, int, int] | tuple[int, int, int] | str


class PkColor:
    """Color handling class."""

    def __init__(self, r: int, g: int, b: int, a: int = 255) -> None:
        """Create a new color object.

        Args:
            r (int): Red value.
            g (int): Green value.
            b (int): Blue value.
            a (int, optional): Alpha value. Defaults to 255.
        """
        if not isinstance(r, int) or not isinstance(g, int) or not isinstance(b, int):
            raise TypeError("RGB values must be integers.")
        if not isinstance(a, int):
            raise TypeError("Alpha value must be an integer.")

        if (r < 0 or r > 255) or (g < 0 or g > 255) or (b < 0 or b > 255):
            raise ValueError(f"Invalid RGB color: ({r}, {g}, {b})")
        if a < 0 or a > 255:
            raise ValueError(f"Invalid alpha value: {a}")

        self.r: int = r
        self.g: int = g
        self.b: int = b
        self.a: int = a

    @staticmethod
    def hsva_to_rgba(
        h: float, s: float, v: float, a: float
    ) -> tuple[int, int, int, int]:
        """Convert an HSVA color to an RGBA tuple using colorsys.

        Args:
            h (float): Hue value.
            s (float): Saturation value.
            v (float): Value value.
            a (float): Alpha value.

        Returns:
            tuple[int, int, int, int]: RGBA tuple.
        """
        r, g, b = colorsys.hsv_to_rgb(h / 360, s, v)
        return (
            int(r * 255),
            int(g * 255),
            int(b * 255),
            int(a * 255),
        )

    @staticmethod
    def hsla_to_rgba(
        h: float, s: float, l: float, a: float
    ) -> tuple[int, int, int, int]:
        """Convert an HSLA color to an RGBA tuple using colorsys.

        Args:
            h (float): Hue value.
            s (float): Saturation value.
            l (float): Lightness value.
            a (float): Alpha value.

        Returns:
            tuple[int, int, int, int]: RGBA tuple.
        """
        r, g, b = colorsys.hls_to_rgb(h / 360, l, s)
        return (
            int(r * 255),
            int(g * 255),
            int(b * 255),
            int(a * 255),
        )

    @staticmethod
    def hex_to_rgba(hex_color: str) -> tuple[int, int, int, int]:
        """Convert a hex color to an RGBA tuple.

        Args:
            hex_color (str): Hex color string (e.g. "#RRGGBBAA").

        Returns:
            tuple[int, int, int, int]: RGBA tuple.
        """
        if hex_color.count("#") != 1:
            raise ValueError(f"Invalid hex color: {hex_color}")
        hex_color = hex_color.lstrip("#").lower()
        if len(hex_color) == 3:  # #RGB -> (RRR, GGG, BBB, 255)
            rgba_value = (
                int(hex_color[0], 16) * 17,  # R
                int(hex_color[1], 16) * 17,  # G
                int(hex_color[2], 16) * 17,  # B
                255,  # A
            )
        elif len(hex_color) == 6:  # #RRGGBB -> (RRR, GGG, BBB, 255)
            rgba_value = (
                int(hex_color[:2], 16),  # R
                int(hex_color[2:4], 16),  # G
                int(hex_color[4:6], 16),  # B
                255,  # A
            )
        elif len(hex_color) == 8:  # #RRGGBBAA -> (RRR, GGG, BBB, AAA)
            rgba_value = (
                int(hex_color[:2], 16),  # R
                int(hex_color[2:4], 16),  # G
                int(hex_color[4:6], 16),  # B
                int(hex_color[6:8], 16),  # A
            )
        else:
            raise ValueError(f"Invalid hex color: {hex_color}")
        return rgba_value

    @staticmethod
    def cmy_to_rgba(c: int, m: int, y: int) -> tuple[int, int, int, int]:
        """Convert a CMY color to an RGBA tuple.
        Note that CMY does not have an alpha channel.

        Args:
            c (int): Cyan value.
            m (int): Magenta value.
            y (int): Yellow value.

        Returns:
            tuple[int, int, int, int]: RGBA tuple.
        """
        if (c < 0 or c > 255) or (m < 0 or m > 255) or (y < 0 or y > 255):
            raise ValueError(f"Invalid CMY color: ({c}, {m}, {y})")

        return (255 - c, 255 - m, 255 - y, 255)

    @staticmethod
    def correct_gamma(value: float) -> float:
        """Correct gamma of a color value.

        Args:
            value (float): Color value.

        Returns:
            float: Corrected color value.
        """
        if value <= 0.0031308:
            return 12.92 * value
        return 1.055 * (value ** (1 / 2.4)) - 0.055

    @classmethod
    def from_pygame(cls, color: pygame.Color) -> PkColor:
        """Create a color from a Pygame color tuple.

        Args:
            color (pygame.Color): Pygame color tuple.

        Returns:
            PkColor: Color object.
        """
        return cls(*color)

    @classmethod
    def from_hex(cls, hex_color: str) -> PkColor:
        """Create a color from a hex string.

        Args:
            hex_color (str): Hex color string.

        Returns:
            PkColor: Color object.
        """
        return cls(*cls.hex_to_rgba(hex_color))

    @classmethod
    def from_cmy(cls, c: int, m: int, y: int) -> PkColor:
        """Create a color from a CMY tuple.

        Args:
            c (int): Cyan value.
            m (int): Magenta value.
            y (int): Yellow value.

        Returns:
            PkColor: Color object.
        """
        return cls(*cls.cmy_to_rgba(c, m, y))

    @classmethod
    def from_hsva(cls, h: float, s: float, v: float, a: float) -> PkColor:
        """Create a color from an HSVA tuple.

        Args:
            h (float): Hue value.
            s (float): Saturation value.
            v (float): Value value.
            a (float): Alpha value.

        Returns:
            PkColor: Color object.
        """
        return cls(*cls.hsva_to_rgba(h, s, v, a))

    @classmethod
    def from_hsla(cls, h: float, s: float, l: float, a: float) -> PkColor:
        """Create a color from an HSLA tuple.

        Args:
            h (float): Hue value.
            s (float): Saturation value.
            l (float): Lightness value.
            a (float): Alpha value.

        Returns:
            PkColor: Color object.
        """
        return cls(*cls.hsla_to_rgba(h, s, l, a))

    @classmethod
    def from_value(cls, color: PkColor | ColorValue) -> PkColor:
        """Create a color from a color value.

        Args:
            color (PkColor | ColorValue): Color value.

        Returns:
            PkColor: Color object.
        """
        if isinstance(color, tuple):
            return cls(*color)
        elif isinstance(color, str):
            if color.startswith("#"):
                return cls.from_hex(color)
            else:
                raise ValueError(f"Invalid color value: {color}")
        elif isinstance(color, PkColor):
            return cls(color.r, color.g, color.b, color.a)
        else:
            raise ValueError(f"Invalid color value: {color}")

    @property
    def hex(self) -> str:
        """Convert a color to a hex string.

        Returns:
            str: Hex string.
        """
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    @property
    def hexa(self) -> str:
        """Convert a color to a hex string with alpha.

        Returns:
            str: Hex string with alpha.
        """
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}{self.a:02x}"

    @property
    def rgba(self) -> tuple[int, int, int, int]:
        """Get the color as an RGBA tuple.

        Returns:
            tuple[int, int, int, int]: RGBA tuple.
        """
        return (self.r, self.g, self.b, self.a)

    @property
    def rgb(self) -> tuple[int, int, int]:
        """Get the color as an RGB tuple.

        Returns:
            tuple[int, int, int]: RGB tuple.
        """
        return (self.r, self.g, self.b)

    @property
    def cmy(self) -> tuple[int, int, int]:
        """Get the color as a CMY tuple.

        Returns:
            tuple[int, int, int]: CMY tuple.
        """
        return (255 - self.r, 255 - self.g, 255 - self.b)

    @property
    def hsva(self) -> tuple[float, float, float, float]:
        """Get the color as an HSVA tuple.

        Returns:
            tuple[float, float, float, float]: HSVA tuple.
        """
        hsv = colorsys.rgb_to_hsv(
            self.normalize(self.r), self.normalize(self.g), self.normalize(self.b)
        )
        return (hsv[0] * 360, hsv[1], hsv[2], self.normalize(self.a))

    @property
    def hsla(self) -> tuple[float, float, float, float]:
        """Get the color as an HSLA tuple.

        Returns:
            tuple[float, float, float, float]: HSLA tuple.
        """
        hls = colorsys.rgb_to_hls(
            self.normalize(self.r), self.normalize(self.g), self.normalize(self.b)
        )
        hsl = hls[0] * 360, hls[2], hls[1]
        return hsl + (self.normalize(self.a),)

    def normalize(self, value: int) -> float:
        """Normalize a color value to the range [0, 1].

        Args:
            value (int): Color value.

        Returns:
            float: Normalized color value.
        """
        return value / 255

    def grayscale(self) -> int:
        """Convert a color to grayscale.

        Returns:
            int: Grayscale value.
        """
        return round(0.2989 * self.r + 0.5870 * self.g + 0.1140 * self.b)

    def lerp(self, other: PkColor, t: float) -> PkColor:
        """Linearly interpolate between self and another color.

        Args:
            other (PkColor): Other color.
            t (float): Interpolation factor.

        Returns:
            PkColor: Interpolated color.
        """
        return PkColor(
            int(self.r + t * (other.r - self.r)),
            int(self.g + t * (other.g - self.g)),
            int(self.b + t * (other.b - self.b)),
            int(self.a + t * (other.a - self.a)),
        )

    def premul_alpha(self) -> PkColor:
        """Premultiply the alpha channel of a color.

        Returns:
            PkColor: Premultiplied color.
        """
        return PkColor(
            int(self.r * self.a / 255),
            int(self.g * self.a / 255),
            int(self.b * self.a / 255),
            self.a,
        )

    def update(
        self,
        r: int,
        g: int,
        b: int,
        a: int | None = None,
    ) -> None:
        """Update the color with new values.
        None values will keep the original values.

        Args:
            r (int): Red value.
            g (int): Green value.
            b (int): Blue value.
            a (int | None): Alpha value. Defaults to None.
        """
        self.r = r
        self.g = g
        self.b = b
        self.a = a if a is not None else self.a

    def __str__(self) -> str:
        return f"PkColor({self.r}, {self.g}, {self.b}, {self.a})"

    def __repr__(self) -> str:
        return f"PkColor({self.r}, {self.g}, {self.b}, {self.a})"

    def __iter__(self) -> Iterator[int]:
        return iter([self.r, self.g, self.b, self.a])

    def __eq__(self, other: PkColor | ColorValue) -> bool:
        if not isinstance(other, PkColor):
            other = PkColor.from_value(other)

        return (
            self.r == other.r
            and self.g == other.g
            and self.b == other.b
            and self.a == other.a
        )

    def __add__(self, other: PkColor) -> PkColor:
        return PkColor(
            min(self.r + other.r, 255),
            min(self.g + other.g, 255),
            min(self.b + other.b, 255),
            min(self.a + other.a, 255),
        )

    def __sub__(self, other: PkColor) -> PkColor:
        return PkColor(
            max(self.r - other.r, 0),
            max(self.g - other.g, 0),
            max(self.b - other.b, 0),
            self.a,
        )

    def __mul__(self, other: PkColor) -> PkColor:
        return PkColor(
            self.r * other.r // 255,
            self.g * other.g // 255,
            self.b * other.b // 255,
            self.a * other.a // 255,
        )
