# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

from puffkit import PkObject, PkSurface
from puffkit.geometry import PkRect, RectValue

if TYPE_CHECKING:  # pragma: no cover
    from puffkit.container import PkContainer
    from puffkit.event import PkEvent


class PkWidget(PkObject):
    """Class to represent a widget in a container.

    The class is used to represent a widget in a container. Widgets are used to
    display information on the screen, and can be used to create user interfaces.
    """

    def __init__(
        self,
        id_: str,
        container: PkContainer,
        rect: PkRect | RectValue,
    ):
        """Initialize the widget.

        Args:
            id_ (str): The ID of the widget.
            container (PkContainer): The container that the widget belongs to.
            rect (PkRect | RectValue): The rectangle that the widget occupies.
                Relative to the container.
        """
        super().__init__()
        self.id: str = id_
        self.container: PkContainer = container

        if isinstance(rect, PkRect):
            self.rect: PkRect = rect
        else:
            self.rect: PkRect = PkRect.from_tuple(rect)

        # check if the widget is out of bounds
        if self.rect.x < 0:
            raise ValueError(
                "Widget is out of bounds. "
                f"Widget x: {self.rect.x} < 0, "
                "Widget must be within the container."
            )
        if self.rect.y < 0:
            raise ValueError(
                "Widget is out of bounds. "
                f"Widget y: {self.rect.y} < 0, "
                "Widget must be within the container."
            )
        if self.rect.right > self.container.rect.width:
            raise ValueError(
                "Widget is out of bounds. "
                f"Widget right: {self.rect.right} > {self.container.rect.width}, "
                "Widget must be within the container."
            )
        if self.rect.bottom > self.container.rect.height:
            raise ValueError(
                "Widget is out of bounds. "
                f"Widget bottom: {self.rect.bottom} > {self.container.rect.height}, "
                "Widget must be within the container."
            )

        # calculate the absolute rectangle
        self.abs_rect: PkRect = PkRect(
            self.rect.x + self.container.rect.x,
            self.rect.y + self.container.rect.y,
            self.rect.w,
            self.rect.h,
        )

        self.surface: PkSurface = PkSurface(self.rect.size, transparent=True)

        self._last_mouse_pos: tuple[int, int] = (0, 0)

        self._visible: bool = True
        self._disabled: bool = False
        self._hovered: bool = False
        self._pressed: bool = False
        self._focused: bool = False

    @property
    def visible(self) -> bool:
        return self._visible

    @visible.setter
    def visible(self, value: bool) -> None:
        self._visible = value

    @property
    def disabled(self) -> bool:
        return self._disabled

    @disabled.setter
    def disabled(self, value: bool) -> None:
        self._disabled = value
        self._hovered = False
        self._pressed = False

    @property
    def hovered(self) -> bool:
        return self._hovered

    @hovered.setter
    def hovered(self, value: bool) -> None:
        self._hovered = value

    @property
    def pressed(self) -> bool:
        return self._pressed

    @pressed.setter
    def pressed(self, value: bool) -> None:
        self._pressed = value

    @property
    def focused(self) -> bool:
        return self._focused

    @focused.setter
    def focused(self, value: bool) -> None:
        self._focused = value

    def on_key_down(self, event: PkEvent) -> None:  # pragma: no cover
        """Handle the key down event.

        This method is called when a key is pressed.

        Args:
            event (PkEvent): The key down event.
        """
        pass

    def on_key_up(self, event: PkEvent) -> None:  # pragma: no cover
        """Handle the key up event.

        This method is called when a key is released.

        Args:
            event (PkEvent): The key up event.
        """
        pass

    def on_hover(self, event: PkEvent) -> None:  # pragma: no cover
        """Handle the hover event.

        This method is called when the mouse over the widget.

        Args:
            event (PkEvent): The mouse move event.
        """
        pass

    def on_mouse_motion(self, event: PkEvent) -> None:  # pragma: no cover
        """Handle the mouse motion event.

        This method is called when the mouse is moved over the widget.

        Args:
            event (PkEvent): The mouse move event.
        """
        # self.logger.debug("Mouse motion")
        pass

    def on_mouse_enter(self, event: PkEvent) -> None:  # pragma: no cover
        """Handle the mouse enter event.

        This method is called when the mouse enters the widget.

        Args:
            event (PkEvent): The mouse move event.
        """
        pass

    def on_mouse_leave(self, event: PkEvent) -> None:  # pragma: no cover
        """Handle the mouse leave event.

        This method is called when the mouse leaves the widget.

        Args:
            event (PkEvent): The mouse move event.
        """
        pass

    def on_mouse_down(self, event: PkEvent) -> None:  # pragma: no cover
        """Handle the mouse down event.

        This method is called when the mouse button is pressed over the widget.

        Args:
            event (PkEvent): The mouse down event.
        """
        pass

    def on_mouse_up(self, event: PkEvent) -> None:  # pragma: no cover
        """Handle the mouse up event.

        This method is called when the mouse button is released over the widget.

        Args:
            event (PkEvent): The mouse up event.
        """
        pass

    def on_focus(self, event: PkEvent) -> None:  # pragma: no cover
        """Handle the focus event.

        This method is called when the widget is focused.

        Args:
            event (PkEvent): The focus event.
        """
        pass

    def on_unfocus(self, event: PkEvent) -> None:  # pragma: no cover
        """Handle the unfocus event.

        This method is called when the widget is unfocused.

        Args:
            event (PkEvent): The unfocus event.
        """
        pass

    def on_change(self, event: PkEvent) -> None:  # pragma: no cover
        """Handle the change event.

        This method is called when the widget's state changes.

        Args:
            event (PkEvent): The change event.
        """
        pass

    def on_update(self, delta: float) -> None:  # pragma: no cover
        """Update the widget.

        This method is called every frame to update the widget.

        Args:
            delta (float): The time in seconds since the last frame.
        """
        pass

    def on_render(self) -> None:  # pragma: no cover
        """Render the widget.

        This method is called every frame to render the widget.
        """
        pass

    def update(self, delta: float) -> None:
        """Update the widget.

        This internal method is called every frame to update the widget.
        NOTE: Do not override this method. Instead, override `on_update`.

        Args:
            delta (float): The time in seconds since the last frame.
        """
        events: list[PkEvent] = self._input["events"]

        for event in events:
            if event.name == "KEYDOWN":
                self.on_key_down(event)
            elif event.name == "KEYUP":
                self.on_key_up(event)
            elif event.name == "MOUSEMOTION":
                self.on_mouse_motion(event)
                if self.abs_rect.collidepoint(event.pos):
                    if not self.abs_rect.collidepoint(self._last_mouse_pos):
                        self.on_mouse_enter(event)
                    self._hovered = True
                    self.on_hover(event)
                else:
                    if self.abs_rect.collidepoint(self._last_mouse_pos):
                        self.on_mouse_leave(event)
                    self._hovered = False
                self._last_mouse_pos = event.pos
            elif event.name == "MOUSEBUTTONDOWN":
                if self.abs_rect.collidepoint(event.pos):
                    self.on_mouse_down(event)
                    self.on_focus(event)
                    self._focused = True
                    self._pressed = True
                else:
                    self.on_unfocus(event)
                    self._focused = False
                    self._pressed = False
            elif event.name == "MOUSEBUTTONUP":
                if self.abs_rect.collidepoint(event.pos):
                    self.on_mouse_up(event)
                    self._pressed = False
                else:
                    self._pressed = False

        self.on_update(delta)

    def render(self) -> None:
        """Render the widget.

        This internal method is called every frame to render the widget.
        NOTE: Do not override this method. Instead, override `on_render`.
        """
        if not self.visible:
            return

        self.on_render()
        if self.focused:  # pragma: no cover
            self.surface.fill("#0000FF")
        self.container.surface.blit(self.surface, self.rect.pos)
