# -*- coding: utf-8 -*-
"""Label widget module for puffkit.

This module contains the `PkLabelWidget` class, which is used to represent a
label widget in a container. The class is used in the `puffkit` package to
display text on the screen.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from puffkit import ColorValue, PkColor, PkContainer, PkRect, PkSurface
from puffkit.color import PkBasicPalette
from puffkit.font import PkSysFont
from puffkit.geometry import RectValue
from puffkit.widget import PkWidget

if TYPE_CHECKING:  # pragma: no cover
    from puffkit.font import PkFont


class PkLabelWidget(PkWidget):
    """Class to represent a label widget in a container.

    The class is used to display text on the screen.
    """

    def __init__(
        self,
        container: PkContainer,
        text: str,
        rect: PkRect | RectValue,
        *,
        font_id: str = "default",
        text_color: PkColor | ColorValue = PkBasicPalette.BLACK,
        background_color: PkColor | ColorValue | None = None,
        text_wrap: bool = True,
        text_align: str = "left",
    ):
        """Initialize the label widget.

        Args:
            container (PkContainer): The container of the widget.
            text (str): The text to display.
            rect (PkRect | RectValue): The rectangle of the widget.

        Keyword Args:
            font_id (str): The ID of the font to use. Defaults to "default".
            text_color (PkColor | ColorValue): The color of the text. Defaults to black.
            background_color (PkColor | ColorValue | None): The background color of the widget.
                Defaults to None.
            text_wrap (bool): Whether to wrap the text. Defaults to True.
            text_align (str): The alignment of the text. Defaults to "left".
        """
        super().__init__(container, rect)

        if not isinstance(text_color, PkColor):
            text_color = PkColor.from_value(text_color)

        if not isinstance(background_color, PkColor) and background_color is not None:
            background_color = PkColor.from_value(background_color)

        self._text: str = text

        self.font_id: str = font_id
        self.text_color: PkColor = text_color

        self.font: PkFont = self._find_font(font_id)

        self.background_color: PkColor | None = background_color
        self.background_surface: PkSurface = PkSurface(self.rect.size, transparent=True)

        self.text_wrap: bool = text_wrap
        self.text_align: str = text_align

        self.needs_redraw: bool = True

    def __str__(self) -> str:
        """Return a string representation of the label widget.

        Returns:
            str: The string representation of the label widget.
        """
        return (
            f"PkLabelWidget(in {self.container} at {self.rect},"
            f" text: {repr(self._text)}, font: {self.font_id} ({self.font.label}),"
            f" text_color: {self.text_color}, background_color: {self.background_color},"
            f" text_wrap: {self.text_wrap}, text_align: {self.text_align}"
        )

    def __repr__(self) -> str:
        """Return a string representation of the label widget.

        Returns:
            str: The string representation of the label widget.
        """
        return (
            f"PkLabelWidget({self.container}, {self._text}, {self.rect},"
            f" font_name={self.font_id}, text_color={self.text_color},"
            f" background_color={self.background_color}, text_wrap={self.text_wrap},"
            f" text_align={self.text_align})"
        )

    def _find_font(self, font_name: str) -> PkFont:
        """Find a font by its name. If the font is not found in the app's fonts,
        try to find a system font with the given name. If that fails, use the
        default font.

        Args:
            font_name (str): The name of the font.

        Returns:
            PkFont: The font object.
        """
        try:
            return self.container.app.fonts[font_name]
        except KeyError:
            self.logger.warning(
                f"Font '{font_name}' not found. Looking for a system font..."
            )
            try:
                return PkSysFont(font_name, 12)
            except FileNotFoundError:
                self.logger.error(
                    f"System font '{font_name}' not found. Using default font."
                )
                return PkSysFont("default", 12)

    def get_text(self) -> str:
        """Get the text of the label.

        Returns:
            str: The text of the label.
        """
        return self._text

    def set_text(self, text: str) -> None:
        """Set the text of the label.

        Args:
            text (str): The text to set.
        """
        self._text = text
        self.needs_redraw = True

    def on_render(self) -> None:
        """Render the label widget."""
        if not self.needs_redraw:
            return

        if self.background_color:
            self.background_surface.fill(self.background_color)
        self.surface.blit(self.background_surface, (0, 0))

        self.surface.blit_text(
            self._text,
            (0, 0, self.rect.width, self.rect.height),
            font=self.font,
            color=self.text_color,
            text_align=self.text_align,
            wrap=self.text_wrap,
        )

        self.needs_redraw = False
