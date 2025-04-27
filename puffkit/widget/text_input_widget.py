# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pygame
from puffkit import PkContainer
from puffkit.widget import PkWidget, PkLabelWidget
from puffkit.color import PkBasicPalette
from puffkit.geometry import PkRect, RectValue
from puffkit.color import PkColor, ColorValue

if TYPE_CHECKING:  # pragma: no cover
    from puffkit.event import PkEvent


class PkTextInputWidget(PkWidget):
    """A customizable text input widget for one-line user input.

    PkTextInputWidget provides a text box with configurable appearance and behavior,
    including support for text alignment, input validation, and state-based styling
    (e.g., disabled, focused).
    """

    def __init__(
        self,
        id_: str,
        container: PkContainer,
        rect: PkRect | RectValue,
        text: str = "",
        *,
        on_change_hook: Any | None = None,
        on_focus_hook: Any | None = None,
        on_unfocus_hook: Any | None = None,
        disabled: bool = False,
        font_id: str = "default",
        background_color: PkColor | ColorValue = PkBasicPalette.GREY,
        background_color_disabled: PkColor
        | ColorValue = PkBasicPalette.DARK_GREY,
        background_color_focused: PkColor | ColorValue = PkBasicPalette.BLUE,
        text_color: PkColor | ColorValue = PkBasicPalette.WHITE,
        text_align: str = "left",
        border_radius: int = 0,
        padding: int = 2,
        max_length: int = 0,
        placeholder: str = "",
        placeholder_color: PkColor | ColorValue = PkBasicPalette.LIGHT_GREY,
        placeholder_color_disabled: PkColor | ColorValue = PkBasicPalette.GREY,
        placeholder_color_focused: PkColor
        | ColorValue = PkBasicPalette.LIGHT_GREY,
    ) -> None:
        """Initialize the text input widget.

        Args:
            id_ (str): The unique identifier for the widget.
            container (PkContainer): The parent container for the widget.
            rect (PkRect | RectValue): The rectangle defining the widget's
                position and size.
            text (str, optional): The initial text in the text box.
                Defaults to "".
            on_change_hook (Any | None, optional): Callback function for text change
                events. Defaults to None.
            on_focus_hook (Any | None, optional): Callback function for focus events.
                Defaults to None.
            on_unfocus_hook (Any | None, optional): Callback function for unfocus
                events. Defaults to None.
            disabled (bool, optional): Whether the widget is disabled.
                Defaults to False.
            font_id (str, optional): The font ID for the text.
                Defaults to "default".
            background_color (PkColor | ColorValue, optional): Background color
                of the text box. Defaults to PkBasicPalette.GREY.
            background_color_disabled (PkColor | ColorValue, optional):
                Background color when disabled. Defaults to PkBasicPalette.DARK_GREY.
            background_color_focused (PkColor | ColorValue, optional):
                Background color when focused. Defaults to PkBasicPalette.BLUE.
            text_color (PkColor | ColorValue, optional): Text color.
                Defaults to PkBasicPalette.WHITE.
            text_align (str, optional): Text alignment ("left", "center", "right").
                Defaults to "left".
            padding (int, optional): Padding inside the text box. Defaults to 2.
            border_radius (int, optional): Border radius of the text box.
                Defaults to 0.
            max_length (int, optional): Maximum length of input text.
                Defaults to 0 (no limit).
            placeholder (str, optional): Placeholder text. Defaults to "".
            placeholder_color (PkColor | ColorValue, optional): Placeholder color.
                Defaults to PkBasicPalette.LIGHT_GREY.
            placeholder_color_disabled (PkColor | ColorValue, optional):
                Placeholder color when disabled. Defaults to PkBasicPalette.GREY.
            placeholder_color_focused (PkColor | ColorValue, optional):
                Placeholder color when focused. Defaults to PkBasicPalette.LIGHT_GREY.

        Raises:
            ValueError: If the provided rectangle is invalid or if the maximum length is negative.

        """
        super().__init__(id_, container, rect, focusable=True)
        self.text: str = text

        self.on_change_hook: Any | None = on_change_hook
        self.on_focus_hook: Any | None = on_focus_hook
        self.on_unfocus_hook: Any | None = on_unfocus_hook

        self.disabled: bool = disabled
        self.font_id: str = font_id

        self.background_color: PkColor | ColorValue = PkColor.from_value(
            background_color
        )
        self.background_color_disabled: PkColor | ColorValue = (
            PkColor.from_value(background_color_disabled)
        )
        self.background_color_focused: PkColor | ColorValue = (
            PkColor.from_value(background_color_focused)
        )
        self.text_color: PkColor | ColorValue = PkColor.from_value(text_color)

        self.text_align: str = text_align
        self.border_radius: int = border_radius
        self.max_length: int = max_length

        self.placeholder: str = placeholder
        self.placeholder_color: PkColor | ColorValue = PkColor.from_value(
            placeholder_color
        )
        self.placeholder_color_disabled: PkColor | ColorValue = (
            PkColor.from_value(placeholder_color_disabled)
        )
        self.placeholder_color_focused: PkColor | ColorValue = (
            PkColor.from_value(placeholder_color_focused)
        )

        self.cursor: int = len(self.text)
        self.cursor_chars: list[str] = ["|", "¦"]
        self.cursor_blink_interval: float = 0.6
        self.cursor_blink_timer: float = 0.0

        # check if the padding isn't too large
        if padding * 2 >= self.rect.w or padding * 2 >= self.rect.h:
            raise ValueError(
                "Padding is too large for the input field. "
                f"Input field width: {self.rect.w}, "
                f"Input field height: {self.rect.h}, "
                f"Padding: {padding}"
            )

        inner_container_rect: PkRect = PkRect(
            padding,
            padding,
            self.rect.w - padding * 2,
            self.rect.h - padding * 2,
        )  # inner rectangle for the text box

        inner_container_widget_rect: PkRect = PkRect(
            0,
            0,
            self.rect.w - padding * 2,
            self.rect.h - padding * 2,
        )  # inner rectangle for the text box widget

        # inner container for the text box
        self._inner_container: PkContainer = PkContainer(
            self.container.app,
            self.surface,
            f"{self.id}_inner_container",
            inner_container_rect,
        )

        self._inner_container.add_widget(
            PkLabelWidget(
                f"{self.id}_text",
                self._inner_container,
                self.text,
                inner_container_widget_rect,
                font_id=self.font_id,
                text_color=self.text_color,
                text_align=self.text_align,
                vertical_align="middle",
            )
        )

        self._inner_container.add_widget(
            PkLabelWidget(
                f"{self.id}_placeholder",
                self._inner_container,
                self.placeholder,
                inner_container_widget_rect,
                font_id=self.font_id,
                text_color=self.placeholder_color,
                text_align=self.text_align,
                vertical_align="middle",
            )
        )

    def set_text(self, text: str, supress_hook: bool = False) -> None:
        """Set the text in the text input widget.

        Args:
            text (str): The text to set in the text input widget.
            supress_hook (bool, optional): If True, suppress the on_change_hook.
                Defaults to False.
        """
        if self.max_length == 0 or len(text) <= self.max_length:
            self.text = text
            self.cursor = len(self.text)
            if self.on_change_hook and not supress_hook:
                self.on_change_hook(self)

    def on_key_down(self, event: PkEvent) -> None:
        """Handle key down events.

        Args:
            event (PkEvent): The key down event.
        """
        if self.disabled or not self.focused:
            return

        if event.key == "backspace":
            if self.text:
                self.text = (
                    self.text[: self.cursor - 1] + self.text[self.cursor :]
                )
                self.cursor = max(0, self.cursor - 1)
        elif event.key == "left":
            self.cursor = max(0, self.cursor - 1)
        elif event.key == "right":
            self.cursor = min(len(self.text), self.cursor + 1)
        elif event.key == "home":
            self.cursor = 0
        elif event.key == "end":
            self.cursor = len(self.text)
        elif event.key == "delete":
            if self.text:
                self.text = (
                    self.text[: self.cursor] + self.text[self.cursor + 1 :]
                )
        else:
            if event.unicode.isprintable() and event.unicode != "":
                if self.max_length == 0 or len(self.text) < self.max_length:
                    self.text = (
                        self.text[: self.cursor]
                        + event.unicode
                        + self.text[self.cursor :]
                    )
                    self.cursor += 1
        if self.on_change_hook:
            self.on_change_hook(self)

    def on_focus(self, event: PkEvent) -> None:
        """Handle focus events.

        Args:
            event (PkEvent): The focus event.
        """
        if self.disabled:
            return

        pygame.key.set_repeat(500, 50)

        self.cursor_blink_timer = 0
        if self.on_focus_hook:
            self.on_focus_hook(self)

    def on_unfocus(self, event: PkEvent) -> None:
        """Handle unfocus events.

        Args:
            event (PkEvent): The unfocus event.
        """
        if self.disabled:
            return

        pygame.key.set_repeat()

        if self.on_unfocus_hook:
            self.on_unfocus_hook(self)

    def on_update(self, delta: float) -> None:
        """Update the text input widget.

        Args:
            delta (float): The time since the last update.
        """
        if self.disabled:
            return

        if self.focused:
            self.cursor_blink_timer += delta
            if self.cursor_blink_timer >= self.cursor_blink_interval:
                self.cursor_blink_timer = 0

    def on_render(self) -> None:
        """Render the text box widget.

        This method is called to render the widget on the screen. It updates
        the background color, draws the text, and handles placeholder visibility.
        """
        if self.disabled:
            self.surface.fill(self.background_color_disabled)
            self._inner_container.get_widget(
                f"{self.id}_placeholder"
            ).surface.fill(self.placeholder_color_disabled)
        else:
            self.surface.fill(self.background_color)
            self._inner_container.get_widget(
                f"{self.id}_placeholder"
            ).surface.fill(self.placeholder_color)

        text_with_cursor = self.text

        if self.focused:
            # self.surface.fill(self.background_color_focused)
            self._inner_container.get_widget(
                f"{self.id}_placeholder"
            ).surface.fill(self.placeholder_color_focused)
            cursor = self.cursor_chars[
                int(
                    self.cursor_blink_timer
                    // (self.cursor_blink_interval / len(self.cursor_chars))
                )
                % len(self.cursor_chars)
            ]
            text_with_cursor = (
                self.text[: self.cursor] + cursor + self.text[self.cursor :]
            )

        if self.text != "" or self.focused:
            self._inner_container.get_widget(f"{self.id}_text").set_text(
                text_with_cursor
            )
            self._inner_container.get_widget(f"{self.id}_text").visible = True
            self._inner_container.get_widget(
                f"{self.id}_placeholder"
            ).visible = False
        else:
            self._inner_container.get_widget(f"{self.id}_text").set_text("")
            self._inner_container.get_widget(f"{self.id}_text").visible = False
            self._inner_container.get_widget(
                f"{self.id}_placeholder"
            ).visible = True

        self._inner_container.render()
