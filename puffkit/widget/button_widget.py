# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from puffkit.color import PkBasicPalette, PkColor, ColorValue
from puffkit.container import PkContainer

from puffkit.geometry import PkRect, RectValue
from puffkit.widget import PkLabelWidget, PkWidget

if TYPE_CHECKING:  # pragma: no cover
    from puffkit.event import PkEvent


class PkButtonWidget(PkWidget):
    """A customizable button widget for user interaction.

    PkButtonWidget provides a button with configurable appearance and behavior,
    including support for click and hover actions, text alignment, and state-based
    styling (e.g., disabled, pressed, hovered).
    """

    def __init__(
        self,
        container: PkContainer,
        rect: PkRect | RectValue,
        label: str,
        *,
        on_click: Any | None = None,
        on_hover: Any | None = None,
        disabled: bool = False,
        font_id: str = "default",
        background_color: PkColor | ColorValue = PkBasicPalette.GREY,
        background_color_disabled: PkColor | ColorValue = PkBasicPalette.DARK_GREY,
        background_color_pressed: PkColor | ColorValue = PkBasicPalette.LIGHT_GREY,
        background_color_hovered: PkColor | ColorValue = PkBasicPalette.BLUE,
        text_color: PkColor | ColorValue = PkBasicPalette.WHITE,
        text_align: str = "center",
        border_radius: int = 0,
    ):
        """Initialize the button widget.

        Args:
            container (PkContainer): The container that the button belongs to.
            rect (PkRect | RectValue): The rectangle that the button occupies.
                Relative to the container.
            label (str): The label of the button.
            on_click (Any | None, optional): The action to perform when the
                button is clicked. Defaults to None.
            on_hover (Any | None, optional): The action to perform when the
                button is hovered. Defaults to None.
            disabled (bool, optional): Whether the button is disabled.
                Defaults to False.
            font_id (str, optional): The font ID of the button label.
                Defaults to "default".
            background_color (PkColor | ColorValue, optional): The background
                color of the button. Defaults to PkBasicPalette.GREY.
            background_color_disabled (PkColor | ColorValue, optional):
                The background color of the button when disabled.
                Defaults to PkBasicPalette.DARK_GREY.
            background_color_pressed (PkColor | ColorValue, optional):
                The background color of the button when pressed.
                Defaults to PkBasicPalette.LIGHT_GREY.
            background_color_hovered (PkColor | ColorValue, optional):
                The background color of the button when hovered.
                Defaults to PkBasicPalette.BLUE.
            text_color (PkColor | ColorValue, optional): The text color of
                the button label. Defaults to PkBasicPalette.WHITE.
            text_align (str, optional): The text alignment of the button label.
                Defaults to "center".
            border_radius (int, optional): The border radius of the button.
                Defaults to 0.
        """
        super().__init__(container, rect)

        if not isinstance(background_color, PkColor):
            background_color = PkColor.from_value(background_color)
        if not isinstance(background_color_disabled, PkColor):
            background_color_disabled = PkColor.from_value(background_color_disabled)
        if not isinstance(background_color_pressed, PkColor):
            background_color_pressed = PkColor.from_value(background_color_pressed)
        if not isinstance(background_color_hovered, PkColor):
            background_color_hovered = PkColor.from_value(background_color_hovered)
        if not isinstance(text_color, PkColor):
            text_color = PkColor.from_value(text_color)

        self.label: str = label

        self.action_on_click: Any | None = on_click
        self.action_on_hover: Any | None = on_hover
        self.disabled: bool = disabled

        self.font_id: str = font_id

        self.background_color: PkColor = background_color
        self.background_color_disabled: PkColor = background_color_disabled
        self.background_color_pressed: PkColor = background_color_pressed
        self.background_color_hovered: PkColor = background_color_hovered

        self.text_color: PkColor = text_color

        self.text_align: str = text_align
        self.border_radius: int = border_radius

        self.inner_container: PkContainer = PkContainer(
            self.container.app,
            self.surface,
            "pkbutton_inner_container",
            PkRect(0, 0, self.rect.width, self.rect.height),
        )

        self.inner_container.add_widget(
            PkLabelWidget(
                self.inner_container,
                self.label,
                PkRect(0, 0, self.rect.width, self.rect.height),
                font_id=self.font_id,
                text_color=self.text_color,
                background_color=None,
                text_align=self.text_align,
                vertical_align="middle",
            )
        )

    def __str__(self) -> str:  # pragma: no cover
        return (
            f"PkButtonWidget(container={self.container} label={self.label}, "
            f"disabled={self.disabled}, "
            f"on_click={self.action_on_click}, on_hover={self.action_on_hover})"
        )

    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"PkButtonWidget(container={self.container}, label={self.label}, "
            f"disabled={self.disabled}, "
            f"on_click={self.action_on_click}, on_hover={self.action_on_hover})"
        )

    def on_update(self, delta: float) -> None:
        if self._disabled:
            self._hovered = False
        self.inner_container.update(delta)

    def on_mouse_up(self, event: PkEvent) -> None:
        if self._disabled:
            return

        if callable(self.action_on_click) and self._pressed:
            self.action_on_click()

    def on_hover(self, event: PkEvent) -> None:
        if self._disabled:
            return

        if callable(self.action_on_hover):
            self.action_on_hover()

    def on_render(self) -> None:
        # fill the surface with a background color depending on the state
        if self._disabled:
            self.surface.draw_rect(
                PkRect(0, 0, self.rect.width, self.rect.height),
                self.background_color_disabled,
                0,
                self.border_radius,
            )
        elif self._pressed:
            self.surface.draw_rect(
                PkRect(0, 0, self.rect.width, self.rect.height),
                self.background_color_pressed,
                0,
                self.border_radius,
            )
        elif self._hovered:
            self.surface.draw_rect(
                PkRect(0, 0, self.rect.width, self.rect.height),
                self.background_color_hovered,
                0,
                self.border_radius,
            )
        else:
            self.surface.draw_rect(
                PkRect(0, 0, self.rect.width, self.rect.height),
                self.background_color,
                0,
                self.border_radius,
            )

        self.inner_container.render()
