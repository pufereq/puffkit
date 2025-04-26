# -*- coding: utf-8 -*-
"""Scene module for simulat."""

from __future__ import annotations

import logging as lg

from typing import TYPE_CHECKING

from puffkit.color import PkBasicPalette
from puffkit.geometry.coordinate import PkCoordinate
from puffkit.object import PkObject
from puffkit.surface import PkSurface

if TYPE_CHECKING:  # pragma: no cover
    from puffkit.app import PkApp


class PkScene(PkObject):
    """Base class for scenes.

    A scene is a state of the game, e.g. the main menu, the game itself, the
    settings menu, etc. Each scene has its own class, which inherits from this
    class. The scenes are stored in the `scenes` dict in the `PkApp` class.
    A scene takes up the whole screen (minus the topbar).
    """

    def __init__(
        self, _id: str, app: PkApp, *, lazy: bool, auto_unload: bool
    ) -> None:
        """Initialize the scene class.

        Args:
            _id (str): The ID of the scene.
            app (PkApp): The app instance.
            lazy (bool): Whether to initialize the scene lazily.
            auto_unload (bool): Whether to automatically unload the scene.
        """
        super().__init__()
        self.id = _id
        self.lazy = lazy
        self.auto_unload = auto_unload

        self.logger = lg.getLogger(f"{__name__}.{self.id}")

        self.logger.debug(f"Initializing scene {self.id}...")
        self.app = app
        self.size = app.internal_screen_size
        self.pos = PkCoordinate(0, 0)

        self.surface = PkSurface(self.size, self.pos)

        self.loaded: bool = False

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.class_name} {self.id}"

    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"<{self.class_name} id={self.id} lazy={self.lazy}"
            f" loaded={self.loaded}>"
        )

    def on_load(self) -> None:
        """Loading hook. Load the scene here."""
        pass

    def on_unload(self) -> None:
        """Unloading hook. Handle scene unloading here."""
        pass

    def on_update(self, delta: float) -> None:
        """Update hook.

        Args:
            delta (float): The time passed since the last frame.
        """
        pass

    def on_render(self) -> None:
        """Render hook."""
        pass

    def load(self) -> None:
        """Load the scene. NOTE: The method you should override is `on_load`."""
        self.surface.fill((255, 255, 255))

        if type(self) is PkScene:
            self.logger.warning("PkScene class should be subclassed.")

        self.on_load()
        self.loaded = True

    def unload(self) -> None:
        """Unload the scene. NOTE: The method you should override is `on_unload`."""
        self.logger.debug(f"Unloading scene {self.id}...")
        self.on_unload()
        self.loaded = False

    def update(self, delta: float) -> None:
        """Update the scene. NOTE: The method you should override is `on_update`.

        Args:
            delta (float): The time passed since the last frame.
        """
        self.on_update(delta)

    def render(self, dest: PkSurface) -> None:
        """Render the scene. NOTE: The method you should override is `on_render`."""
        # draw a checkerboard pattern
        _checkerboard_rect_size: int = 16
        self.surface.fill(PkBasicPalette.WHITE)
        for x in range(0, int(self.size.width), _checkerboard_rect_size):
            for y in range(0, int(self.size.height), _checkerboard_rect_size):
                if (x + y) % (_checkerboard_rect_size * 2) == 0:
                    self.surface.fill(
                        PkBasicPalette.DARK_GREY,
                        (
                            x,
                            y,
                            _checkerboard_rect_size,
                            _checkerboard_rect_size,
                        ),
                    )

        self.on_render()
        self.draw(dest)

    def draw(self, screen: PkSurface) -> None:
        """Draw the scene to the screen."""
        screen.blit(self.surface, self.surface.pos)
