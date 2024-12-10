# -*- coding: utf-8 -*-
"""Scene module for simulat."""
from __future__ import annotations

import logging as lg

import pygame as pg

from typing import TYPE_CHECKING
from puffkit.font.sysfont import PkSysFont
from puffkit.geometry.coordinate import PkCoordinate
from puffkit.object import PkObject
from puffkit.surface import PkSurface

if TYPE_CHECKING:
    from puffkit.app import PkApp


class PkScene(PkObject):
    """Base class for scenes.

    A scene is a state of the game, e.g. the main menu, the game itself, the
    settings menu, etc. Each scene has its own class, which inherits from this
    class. The scenes are stored in the `scenes` dict in the `PkApp` class.
    A scene takes up the whole screen (minus the topbar).
    """

    def __init__(self, _id: str, app: PkApp, *, lazy: bool) -> None:
        """Initialize the scene class.

        Args:
            _id (str): The ID of the scene.
            app (PkApp): The app instance.
            lazy (bool): Whether to initialize the scene lazily.
        """
        super().__init__()
        self.id = _id
        self.lazy = lazy

        self.logger = lg.getLogger(f"{__name__}.{self.id}")

        self.logger.debug(f"Initializing scene {self.id}...")
        self.app = app
        self.size = app.internal_screen_size
        self.pos = PkCoordinate(0, 0)

        self.surface = PkSurface(self.size, self.pos)

        self.loaded: bool = False

        if not self.lazy:
            self.init()
            self.loaded = True

    def __str__(self) -> str:
        return f"{self.class_name} {self.id}"

    def __repr__(self) -> str:
        return (
            f"<{self.class_name} id={self.id} lazy={self.lazy}"
            f" loaded={self.loaded}>"
        )

    def init(self) -> None:
        """Initialize the scene fully. Should be called even if subclassed."""
        self.surface.fill((255, 255, 255))

        if type(self) is PkScene:
            self.logger.warning("PkScene class should be subclassed.")

        # draw fallback text
        if self.id == "fallback":
            self.surface.blit_text(
                "FALLBACK SCENE",
                (20, 20),
                color="#ff0000",
                font=self.app.fonts["default"],
            )

    def input(
        self,
        *,
        events: list[pg.event.Event],
        keys: dict[int, bool],
        mouse_pos: tuple[int, int],
        mouse_buttons: tuple[bool, bool, bool],
    ) -> None:
        pass

    def update(self, delta: float) -> None:
        """Update the scene.

        Args:
            delta (float): The time passed since the last frame.
        """
        pass

    def render(self, dest: PkSurface) -> None:
        """Render the scene."""
        self.draw(dest)

    def draw(self, screen: PkSurface) -> None:
        """Draw the scene to the screen."""
        screen.blit(self.surface, self.surface.pos)
