# -*- coding: utf-8 -*-
"""Surface module for puffkit."""

from __future__ import annotations

from typing import Any, Final, Self, TYPE_CHECKING

import pygame

from puffkit.color.color import ColorValue, PkColor
from puffkit.color.palettes import PkBasicPalette
from puffkit.font.sysfont import PkSysFont
from puffkit.geometry.coordinate import PkCoordinate, CoordinateValue
from puffkit.geometry.rect import PkRect, RectValue
from puffkit.geometry.size import PkSize, SizeValue
from puffkit.object import PkObject

if TYPE_CHECKING:
    from puffkit.subsurface import PkSubSurface
    from puffkit.font.font import PkFont


class PkSurface(PkObject):
    """Base class for surfaces.

    A surface is a part of the screen. It can be a scene, a topbar, a button,
    etc.
    """

    def __init__(
        self,
        size: PkSize | SizeValue,
        pos: PkCoordinate | CoordinateValue = PkCoordinate(0, 0),
        transparent: bool = False,
        *,
        flags: int = 0,
        depth: int = 32,
        masks: tuple[int, int, int, int] | None = None,
    ):
        """Initialize the surface.

        Args:
            size (PkSize): Size of the surface.
            pos (PkCoordinate, optional): Position of the surface.
                Defaults to PkCoordinate(0, 0).
            transparent (bool, optional): Whether the surface supports
                transparency.
            flags (int, optional): Flags for the surface. Defaults to 0.
            depth (int, optional): Depth of the surface. Defaults to 32.
            masks (tuple[int, int, int, int] | None, optional): Masks for the
                surface. Defaults to None.
        """
        if not isinstance(size, PkSize):
            size = PkSize(*size)
        if not isinstance(pos, PkCoordinate):
            pos = PkCoordinate(*pos)

        super().__init__()

        self.transparent: Final[bool] = transparent

        if self.transparent:
            flags |= pygame.SRCALPHA

        self.pos = pos
        self.masks = masks

        if masks is None:
            self.internal_surface = pygame.Surface(size.tuple, flags, depth)
        else:
            self.internal_surface = pygame.Surface(size.tuple, flags, depth, masks)

    def __str__(self) -> str:
        """Return the string representation of the surface."""

        return (
            f"PkSurface({self.size.w}x{self.size.h} at {self.pos},"
            f" transparent={self.transparent})"
        )

    def __repr__(self) -> str:
        """Return the string representation of the surface."""
        return (
            f"PkSurface({self.size}, {self.pos}, {self.transparent},"
            f" flags={self.get_flags()}, depth={self.get_bitsize()},"
            f" masks={self.get_masks()})"
        )

    @classmethod
    def from_pygame(cls, surface: pygame.Surface) -> Self:
        """Create a surface from a pygame surface.

        Args:
            surface (pygame.Surface): Pygame surface.

        Returns:
            Surface: The created surface.
        """
        instance = cls(
            size=PkSize(*surface.get_size()),
            flags=surface.get_flags(),
            depth=surface.get_bitsize(),
            masks=surface.get_masks(),
        )
        instance.internal_surface = surface
        return instance

    @property
    def size(self) -> PkSize:
        """Size of the surface.

        Returns:
            tuple[int, int]: Size of the surface.
        """
        return PkSize(*self.internal_surface.get_size())

    @property
    def width(self) -> int | float:
        """Width of the surface.

        Returns:
            int: Width of the surface.
        """
        return self.size.w

    @property
    def height(self) -> int | float:
        """Height of the surface.

        Returns:
            int: Height of the surface.
        """
        return self.size.h

    def blit(
        self,
        source: PkSurface,
        dest: PkCoordinate | CoordinateValue,
        area: RectValue | PkRect | None = None,
        special_flags: int = 0,
    ):
        """Draw one surface onto another.

        Args:
            source (Surface): Surface to draw.
            dest (tuple[int, int]): Position of the surface.
        """
        if not isinstance(dest, PkCoordinate):
            dest = PkCoordinate(*dest)
        self.internal_surface.blit(
            source.internal_surface, dest.tuple, area, special_flags
        )

    def blits(
        self,
        blit_sequence: (
            list[tuple[PkSurface, tuple[int, int]]]
            | list[tuple[PkSurface, tuple[int, int], tuple[int, int, int, int]]]
            | list[tuple[PkSurface, tuple[int, int], tuple[int, int, int, int], int]]
        ),
    ):
        """Draw multiple surfaces onto this surface.

        Args:
            blit_sequence (list[tuple[PkSurface, tuple[int, int]]] |
                list[tuple[PkSurface, tuple[int, int], tuple[int, int, int, int]]] |
                list[tuple[PkSurface, tuple[int, int], tuple[int, int, int, int], int]]):
                Sequence of blits. Each tuple contains the surface to draw, the
                position to draw it at, the area to draw, and special flags.
        """
        for blit in blit_sequence:
            self.blit(*blit)

    def convert(self, surface: PkSurface | None = None) -> PkSurface:
        """Convert the surface to a new format.

        Args:
            surface (Surface | None, optional): Surface to convert to.
                Defaults to None.

        Returns:
            Surface: Converted surface.
        """
        if surface is not None:
            return self.from_pygame(
                self.internal_surface.convert(surface.internal_surface)
            )
        else:
            return self.from_pygame(self.internal_surface.convert())

    def convert_alpha(self) -> PkSurface:
        """Convert the surface to a new format with per-pixel alpha.

        Args:
            surface (Surface | None, optional): Surface to convert to.
                Defaults to None.

        Returns:
            Surface: Converted surface.
        """
        return self.from_pygame(self.internal_surface.convert_alpha())

    def copy(self) -> PkSurface:
        """Copy the surface.

        Returns:
            Surface: Copied surface.
        """
        return self.from_pygame(self.internal_surface.copy())

    def fill(
        self,
        color: PkColor | ColorValue,
        rect: tuple[int, int, int, int] | None = None,
        special_flags: int = 0,
    ):
        """Fill the surface with a color.

        Args:
            color (PkColor | ColorValue): Color to fill with.
            rect (tuple[int, int, int, int] | None, optional): Area to fill.
                Defaults to None (whole surface).
            special_flags (int, optional): Special flags. Defaults to 0.
        """
        if not isinstance(color, PkColor):
            color = PkColor.from_value(color)
        self.internal_surface.fill(tuple(color), rect, special_flags)

    def scroll(self, dx: int, dy: int) -> None:
        """Scroll the surface.

        Args:
            dx (int): Horizontal scroll amount.
            dy (int): Vertical scroll amount.
        """
        self.internal_surface.scroll(dx, dy)

    def set_colorkey(self, color: PkColor | ColorValue) -> None:
        """Set the colorkey of the surface.

        Args:
            color (PkColor): Colorkey to set.
        """
        if not isinstance(color, PkColor):
            color = PkColor.from_value(color)
        self.internal_surface.set_colorkey(tuple(color))

    def get_colorkey(self) -> tuple[int, int, int, int] | None:
        """Get the colorkey of the surface.

        Returns:
            tuple[int, int, int, int]: Colorkey of the surface.
        """
        return self.internal_surface.get_colorkey()

    def set_alpha(self, alpha: int) -> None:
        """Set the alpha value of the surface.

        Args:
            alpha (int): Alpha value to set.
        """
        self.internal_surface.set_alpha(alpha)

    def get_alpha(self) -> int | None:
        """Get the alpha value of the surface.

        Returns:
            int: Alpha value of the surface.
        """
        return self.internal_surface.get_alpha()

    def lock(self) -> None:
        """Lock the surface."""
        self.internal_surface.lock()

    def unlock(self) -> None:
        """Unlock the surface."""
        self.internal_surface.unlock()

    def mustlock(self) -> bool:
        """Check if the surface must be locked.

        Returns:
            bool: Whether the surface must be locked.
        """
        return self.internal_surface.mustlock()

    def get_locked(self) -> bool:
        """Check if the surface is locked.

        Returns:
            bool: Whether the surface is locked.
        """
        return self.internal_surface.get_locked()

    def get_locks(self) -> tuple[Any, ...]:
        """Get the number of locks on the surface.

        Returns:
            tuple: Locks on the surface.
        """
        return self.internal_surface.get_locks()

    def get_at(self, pos: tuple[int, int]) -> PkColor:
        """Get the color of a pixel.

        Args:
            pos (tuple[int, int]): Position of the pixel.

        Returns:
            PkColor: Color of the pixel.
        """
        return PkColor.from_pygame(self.internal_surface.get_at(pos))

    def set_at(self, pos: tuple[int, int], color: PkColor | ColorValue) -> None:
        """Set the color of a pixel.

        Args:
            pos (tuple[int, int]): Position of the pixel.
            color (tuple[int, int, int, int]): Color to set.
        """
        if not isinstance(color, PkColor):
            color = PkColor.from_value(color)
        self.internal_surface.set_at(pos, tuple(color))

    def get_at_mapped(self, pos: tuple[int, int]) -> int:
        """Get the mapped color of a pixel.

        Args:
            pos (tuple[int, int]): Position of the pixel.

        Returns:
            int: Color of the pixel.
        """
        return self.internal_surface.get_at_mapped(pos)

    def get_palette(self) -> list[PkColor]:
        """Get the palette of the surface.

        Returns:
            list[PkColor]: Palette of the surface.
        """
        return [PkColor(*color) for color in self.internal_surface.get_palette()]

    def set_palette(self, palette: list[PkColor]) -> None:
        """Set the palette of the surface.

        Args:
            palette (list[PkColor]): Palette to set.
        """
        int_palette = [tuple(color) for color in palette]
        self.internal_surface.set_palette(int_palette)

    def set_palette_at(self, index: int, color: PkColor | ColorValue) -> None:
        """Set a color in the palette.

        Args:
            index (int): Index of the color.
            color (PkColor | ColorValue): Color to set.
        """
        if not isinstance(color, PkColor):
            color = PkColor.from_value(color)
        self.internal_surface.set_palette_at(index, tuple(color))

    def map_rgb(self, color: PkColor | ColorValue) -> int:
        """Map an RGB color to a mapped color.

        Args:
            color (PkColor | ColorValue): Color to map.

        Returns:
            int: Mapped color.
        """
        if not isinstance(color, PkColor):
            color = PkColor.from_value(color)
        return self.internal_surface.map_rgb(tuple(color))

    def unmap_rgb(self, color: int) -> PkColor:
        """Convert a mapped integer color value to an RGB color.

        Args:
            color (int): Mapped color.

        Returns:
            PkColor: RGB color.
        """
        return PkColor.from_pygame(self.internal_surface.unmap_rgb(color))

    def set_clip(self, rect: PkRect | None) -> None:
        """Set the clipping area of the surface.

        Args:
            rect (PkRect | None): Clipping area.
        """
        self.internal_surface.set_clip(tuple(rect) if rect is not None else None)

    def get_clip(self) -> PkRect:
        """Get the clipping area of the surface.

        Returns:
            PkRect: Clipping area of the surface.
        """
        return PkRect.from_pygame(self.internal_surface.get_clip())

    def subsurface(self, rect: PkRect | RectValue) -> PkSubSurface:
        """Create a subsurface.

        Args:
            rect (tuple[int, int, int, int]): Area of the subsurface.

        Returns:
            PkSubSurface: Created subsurface.
        """
        from puffkit.subsurface import PkSubSurface

        return PkSubSurface(self, rect[:2], rect[2:])

    def get_parent(self) -> Self:
        """Get the parent surface of the surface.
        A surface does not have a parent surface.

        Returns:
            Self: Parent surface.
        """
        self.logger.warning(f"Surface {self} is already a top-level surface.")
        return self

    def get_abs_parent(self) -> PkSurface:
        """Get the absolute parent surface of the surface.

        Returns:
            Self: Absolute parent surface.
        """
        return self

    def get_offset(self) -> tuple[int, int]:
        """Get the offset of the surface.

        Returns:
            tuple[int, int]: Offset of the surface.
        """
        return self.internal_surface.get_offset()

    def get_size(self) -> tuple[int, int]:
        """Get the size of the surface.

        Returns:
            tuple[int, int]: Size of the surface.
        """
        return tuple(self.size)

    def get_width(self) -> int:
        """Get the width of the surface.

        Returns:
            int: Width of the surface.
        """
        return self.internal_surface.get_width()

    def get_height(self) -> int:
        """Get the height of the surface.

        Returns:
            int: Height of the surface.
        """
        return self.internal_surface.get_height()

    def get_rect(self) -> PkRect:
        """Get the rect of the surface.

        Returns:
            PkRect: Rect of the surface.
        """
        return PkRect.from_pygame(self.internal_surface.get_rect())

    def get_bitsize(self) -> int:
        """Get the bit size of the surface.

        Returns:
            int: Bit size of the surface.
        """
        return self.internal_surface.get_bitsize()

    def get_bytesize(self) -> int:
        """Get the byte size of the surface.

        Returns:
            int: Byte size of the surface.
        """
        return self.internal_surface.get_bytesize()

    def get_flags(self) -> int:
        """Get the flags of the surface.

        Returns:
            int: Flags of the surface.
        """
        return self.internal_surface.get_flags()

    def get_masks(self) -> tuple[int, int, int, int]:
        """Get the masks of the surface.

        Returns:
            tuple[int, int, int, int]: Masks of the surface.
        """
        return self.internal_surface.get_masks()

    def set_masks(self, masks: tuple[int, int, int, int]) -> None:
        """Set the masks of the surface.
        This method is deprecated and kept for compatibility.

        Args:
            masks (tuple[int, int, int, int]): Masks to set.
        """
        raise DeprecationWarning(
            "set_masks is deprecated. Use masks attribute instead."
        )

    def get_shifts(self) -> tuple[int, int, int, int]:
        """Get the shifts of the surface.

        Returns:
            tuple[int, int, int, int]: Shifts of the surface.
        """
        return self.internal_surface.get_shifts()

    def set_shifts(self, shifts: tuple[int, int, int, int]) -> None:
        """Set the shifts of the surface.
        This method is deprecated and kept for compatibility.

        Args:
            shifts (tuple[int, int, int, int]): Shifts to set.
        """
        raise DeprecationWarning(
            "set_shifts is deprecated. Use shifts attribute instead."
        )

    def get_losses(self) -> tuple[int, int, int, int]:
        """Get the the significant bits used to convert between a color and a mapped integer.

        Returns:
            tuple[int, int, int, int]: Losses of the surface.
        """
        return self.internal_surface.get_losses()

    def get_bounding_rect(self, min_alpha: int = 1) -> tuple[int, int, int, int]:
        """Get the bounding rect of the surface.

        Args:
            min_alpha (int, optional): Minimum alpha value. Defaults to 1.

        Returns:
            tuple[int, int, int, int]: Bounding rect of the surface.
        """
        return self.internal_surface.get_bounding_rect(min_alpha)

    def get_view(self) -> pygame.BufferProxy:
        """Get the buffer view of the Surface's pixels.view of the surface.

        Returns:
            BufferProxy: Buffer view of the surface.
        """
        return self.internal_surface.get_view()

    def get_buffer(self) -> pygame.BufferProxy:
        """Get the buffer of the surface.

        Returns:
            BufferProxy: Buffer of the surface.
        """
        return self.internal_surface.get_buffer()

    @property
    def _pixels_address(self) -> int:
        """Get the address of the pixels of the surface.

        Returns:
            int: Address of the pixels of the surface.
        """
        return self.internal_surface._pixels_address

    def premul_alpha(self) -> PkSurface:
        """Premultiply the alpha of the surface.

        Returns:
            Surface: Surface with premultiplied alpha.
        """
        return self.from_pygame(self.internal_surface.premul_alpha())

    def scale(self, size: tuple[int, int]) -> PkSurface:
        """Scale the surface.

        Args:
            size (tuple[int, int]): Size to scale to.

        Returns:
            Surface: Scaled surface.
        """
        return self.from_pygame(pygame.transform.scale(self.internal_surface, size))

    def draw_rect(
        self,
        rect: PkRect | RectValue,
        color: PkColor | ColorValue,
        width: int = 0,
        border_radius: int = -1,
        border_top_left_radius: int = -1,
        border_top_right_radius: int = -1,
        border_bottom_left_radius: int = -1,
        border_bottom_right_radius: int = -1,
    ) -> None:
        """Draw a rectangle on the surface.

        Args:
            rect (PkRect | RectValue): Rectangle to draw.
            color (PkColor | ColorValue): Color of the rectangle.
            width (int, optional): Stroke width of the rectangle.
                Defaults to 0 (filled).
            border_radius (int, optional): Radius of the rectangle border.
                Defaults to -1 (no border radius).
            border_top_left_radius (int, optional): Radius of the top-left corner.
                Defaults to -1 (no border radius).
            border_top_right_radius (int, optional): Radius of the top-right corner.
                Defaults to -1 (no border radius).
            border_bottom_left_radius (int, optional): Radius of the bottom-left corner.
                Defaults to -1 (no border radius).
            border_bottom_right_radius (int, optional): Radius of the bottom-right corner.
                Defaults to -1 (no border radius).
        """
        if not isinstance(color, PkColor):
            color = PkColor.from_value(color)
        pygame.draw.rect(
            self.internal_surface,
            tuple(color),
            tuple(rect),
            width,
            border_radius,
            border_top_left_radius,
            border_top_right_radius,
            border_bottom_left_radius,
            border_bottom_right_radius,
        )

    def blit_text(
        self,
        text: str,
        rect: PkRect | RectValue,
        *,
        wrap: bool = True,
        text_align: str = "left",
        vertical_align: str = "top",
        tab_size: int = 4,
        font: PkFont | PkSysFont,
        color: PkColor | ColorValue = PkBasicPalette.WHITE,
        bg_color: PkColor | ColorValue | None = None,
        antialias: bool = True,
    ) -> None:
        """Add text to the surface.

        Args:
            text (str): Text to add.
            rect (PkRect | RectValue): Rectangle specifying the position and size
                of the text.

        Keyword Args:
            wrap (bool, optional): Whether to wrap the text. Defaults to True.
            text_align (str, optional): Horizontal alignment of the text.
                Avaliable values: "left", "center", "right". Defaults to "left".
            vertical_align (str, optional): Vertical alignment of the text.
                Avaliable values: "top", "middle", "bottom". Defaults to "top".
            color (PkColor | ColorValue): Color of the text. Defaults to SimulatPalette.FOREGROUND.
            bg_color (PkColor | ColorValue | None, optional): Background color of the text. Defaults to None (transparent).
            font (PkFont, optional): Font to use. Defaults to "main".
            antialias (bool, optional): Whether to use font antialiasing.
                Defaults to True.
        """

        # color conversion
        if not isinstance(color, PkColor):
            color = PkColor.from_value(color)
        if not isinstance(bg_color, PkColor):
            bg_color = PkColor.from_value(bg_color) if bg_color is not None else None

        # rect conversion
        if not isinstance(rect, PkRect):
            rect = PkRect.from_tuple(rect)

        text_surface: PkSurface = PkSurface(rect.size, transparent=True)

        max_width = int(rect.width) if wrap else 0

        # text preparation
        text = text.replace("\t", " " * tab_size)

        align_map = {
            "left": pygame.FONT_LEFT,
            "center": pygame.FONT_CENTER,
            "right": pygame.FONT_RIGHT,
        }

        rendered_text = font.render(
            text,
            antialias,
            color,
            bg_color,
            max_width,
            align_map[text_align],
        )

        # vertical alignment
        if vertical_align == "middle":
            y_pos = text_surface.height // 2 - rendered_text.get_height() // 2
        elif vertical_align == "bottom":
            y_pos = text_surface.height - rendered_text.get_height()
        else:
            y_pos = 0

        text_surface.blit(rendered_text, (0, y_pos))

        self.blit(text_surface, rect.pos)
