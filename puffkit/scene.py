# -*- coding: utf-8 -*-
"""Scene module for simulat."""
from __future__ import annotations

import logging as lg

import pygame as pg

from puffkit.app import PkApp
from puffkit.font.sysfont import PkSysFont
from puffkit.object import PkObject
from puffkit.surface import PkSurface


class PkScene(PkObject):
    """Base class for scenes.

    A scene is a state of the game, e.g. the main menu, the game itself, the
    settings menu, etc. Each scene has its own class, which inherits from this
    class. The scenes are stored in the `scenes` dict in the `PkApp` class.
    A scene takes up the whole screen (minus the topbar).
    """

    def __init__(self, app: PkApp) -> None:
        """Initialize the scene.

        Args:
            size (tuple[int, int]): Size of the scene (px).
            pos (tuple[int, int]): Position of the scene (px).
        """
        self.id = type(self).__name__

        self.logger = lg.getLogger(f"{__name__}.{self.id}")

        self.logger.debug(f"Initializing scene {self.id}...")
        self.app = app
        self.size = app.internal_screen_size
        self.pos = (0, 0)

        self.surface = PkSurface(tuple(self.size), self.pos)

        self.surface.fill((255, 255, 255))

        # show fallback message if Scene called directly
        if type(self) is PkScene:
            self.logger.warning(
                "`PkScene` called directly, showing fallback message..."
            )
            self.surface.blit_text(
                "FALLBACK SCENE",
                (20, 20),
                color="#ff0000",
                font=PkSysFont("monospace", 12),
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
