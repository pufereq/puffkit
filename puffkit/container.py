# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TYPE_CHECKING

import random as rnd

from puffkit import PkObject, PkSurface
from puffkit.color import PkBasicPalette
from puffkit.geometry import PkRect, RectValue

if TYPE_CHECKING:  # pragma: no cover
    from puffkit import PkApp
    from puffkit.widget import PkWidget


class PkContainer(PkObject):
    """Class to represent a container for widgets.

    The class is used to group widgets together and manage their layout.
    """

    def __init__(
        self,
        app: PkApp,
        parent_surface: PkSurface,
        name: str,
        rect: PkRect | RectValue,
        *,
        draw_outline: bool = False,
    ):
        """Initialize the container.

        Args:
            app (PkApp): The app instance.
            parent_surface (PkSurface): The parent surface.
            name (str): The name of the container.
            rect (PkRect | RectValue): The rectangle that the container occupies.
            draw_outline (bool): Whether to draw an outline around the container.
        """
        super().__init__()
        self.app: PkApp = app
        self.name: str = name
        self.draw_outline: bool = draw_outline
        self.parent_surface: PkSurface = parent_surface

        if isinstance(rect, PkRect):
            self.rect: PkRect = rect
        else:
            self.rect: PkRect = PkRect.from_tuple(rect)

        # check if the container is out of bounds
        if self.rect.x < 0:
            raise ValueError(
                "Container is out of bounds. "
                f"Container x: {self.rect.x} < 0, "
                "Container must be within the parent surface."
            )
        if self.rect.y < 0:
            raise ValueError(
                "Container is out of bounds. "
                f"Container y: {self.rect.y} < 0, "
                "Container must be within the parent surface."
            )
        if self.rect.right > self.parent_surface.get_width():
            raise ValueError(
                "Container is out of bounds. "
                f"Container right: {self.rect.right} > {self.parent_surface.get_width()}, "
                "Container must be within the parent surface."
            )
        if self.rect.bottom > self.parent_surface.get_height():
            raise ValueError(
                "Container is out of bounds. "
                f"Container bottom: {self.rect.bottom} > {self.parent_surface.get_height()}, "
                "Container must be within the parent surface."
            )

        # create an outline surface if needed (for debugging)
        if self.draw_outline:
            self.outline_surface: PkSurface = PkSurface(
                self.rect.size, transparent=True
            )
            self.outline_surface.draw_rect(
                PkRect((0, 0), (self.rect.width, self.rect.height)),
                (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255), 128),
                4,
            )

        self.children: list[PkWidget] = []

    def __str__(self) -> str:
        """Return a human-friendly representation of the container."""
        return (
            f"PkContainer({self.name} on {self.parent_surface},"
            f" {len(self.children)} children, {self.rect})"
        )

    def __repr__(self) -> str:
        """Return a string representation of the container."""
        return (
            f"PkContainer({self.app}, {self.parent_surface},"
            f" {self.name}, {self.rect})"
        )

    def add_widget(self, widget: PkWidget) -> None:
        """Add a widget to the container.

        Args:
            widget (PkWidget): The widget to add.
        """
        self.logger.debug(f"Adding widget {widget} to container {self}")
        self.children.append(widget)

    def remove_widget(self, widget: PkWidget) -> None:
        """Remove a widget from the container.

        Args:
            widget (PkWidget): The widget to remove.
        """
        self.logger.debug(f"Removing widget {widget} from container {self}")
        self.children.remove(widget)

    def update(self, delta: float) -> None:
        """Update the container.

        Args:
            delta (float): The time delta.
        """
        for child in self.children:
            child.input(
                self._input["events"],
                self._input["keys"],
                self._input["mouse_pos"],
                self._input["mouse_buttons"],
            )
            child.update(delta)

    def render(self) -> None:
        """Render the container."""
        if self.draw_outline:
            self.parent_surface.blit(self.outline_surface, self.rect.pos)
        for child in self.children:
            child.render()
