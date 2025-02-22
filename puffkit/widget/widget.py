# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

from puffkit import PkObject, PkSurface
from puffkit.geometry import PkRect, RectValue

if TYPE_CHECKING:  # pragma: no cover
    from puffkit.container import PkContainer


class PkWidget(PkObject):
    """Class to represent a widget in a container.

    The class is used to represent a widget in a container. Widgets are used to
    display information on the screen, and can be used to create user interfaces.
    """

    def __init__(
        self,
        container: PkContainer,
        rect: PkRect | RectValue,
    ):
        """Initialize the widget.

        Args:
            container (PkContainer): The container that the widget belongs to.
            rect (PkRect | RectValue): The rectangle that the widget occupies.
                Relative to the container.
        """
        super().__init__()
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
        self.on_update(delta)

    def render(self) -> None:
        """Render the widget.

        This internal method is called every frame to render the widget.
        NOTE: Do not override this method. Instead, override `on_render`.
        """
        self.on_render()
        self.container.parent_surface.blit(self.surface, self.abs_rect.pos)
