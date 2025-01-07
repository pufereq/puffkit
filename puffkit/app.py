# -*- coding: utf-8 -*-
"""puffkit App module."""
from __future__ import annotations

import pygame as pg

from typing import Final

from puffkit.color.palettes import PkBasicPalette
from puffkit.event import PkEventManager
from puffkit.font.font import PkFont
from puffkit.font.sysfont import PkSysFont
from puffkit.geometry.size import PkSize
from puffkit.object import PkObject
from puffkit.scene import PkScene, PkSceneManager
from puffkit.surface import PkSurface


class PkApp(PkObject):
    """App class.

    The app is the main object of an application. It is responsible for
    initializing the app, running the main loop, and handling events.

    The class has to be subclassed to create custom apps.
    """

    def __init__(
        self,
        app_name: str,
        app_version: str,
        display_size: tuple[int, int],
        display_arguments: dict[str, bool],
        internal_screen_size: tuple[int, int],
        fps_limit: int = 60,
    ) -> None:
        """Initialize the app.

        Args:
            app_name (str): Name of the app.
            app_version (str): Version of the app.
            display_size (tuple[int, int]): Size of the display window.
            display_arguments (dict[str, bool]): Arguments for the display window.
            internal_screen_size (tuple[int, int]): Size of the internal screen.
            fps_limit (int, optional): Frame rate cap. Defaults to 60.
        """
        super().__init__()

        if type(self) is PkApp:
            raise TypeError("PkApp class must be subclassed.")

        # set app info
        self.app_name: str = app_name
        self.app_version: str = app_version
        self.display_size: PkSize = PkSize(*display_size)
        self.internal_screen_size: PkSize = PkSize(*internal_screen_size)

        self.fps_limit: int = fps_limit
        self.delta_time: float = 1

        self.logger.info(f"Initializing {self.app_name} {self.app_version}...")

        # intialize pygame
        pg.init()

        # set up display
        self.display = pg.display.set_mode(self.display_size.tuple, **display_arguments)
        self.internal_screen = PkSurface(self.internal_screen_size)

        # set up event manager
        self.event_manager = PkEventManager(self)

        # set window title
        self.title: str = f"{self.app_name} {self.app_version}"
        pg.display.set_caption(self.title)

        # set up fonts
        pg.font.init()
        self.fonts: dict[str, PkFont] = {}
        self.add_font("default", None, 14)

        # set up scenes
        self.scene_manager = PkSceneManager(self)

        # set up clock
        self.clock = pg.time.Clock()

        self.running: bool = False

    @classmethod
    def get_instance(cls) -> PkApp:
        """Get the instance of the app.

        Returns:
            PkApp: The instance of the app.
        """
        if cls._instance is None:
            raise RuntimeError("PkApp instance does not exist.")
        return cls._instance

    def add_font(self, name: str, path: str | None, size: int) -> None:
        """Add a font to the app.

        Args:
            name (str): Name of the font.
            path (str | None): Path to the font file. If None, use system font.
            size (int): Size of the font (px).
        """
        self.logger.debug(f"Adding font {name}...")
        self.fonts[name] = PkFont(path, size)

    def add_sysfont(self, name: str, size: int) -> None:
        """Add a system font to the app.

        Args:
            name (str): Name of the system font.
            size (int): Size of the font (px).
        """
        self.logger.debug(f"Adding system font {name}...")
        self.fonts[name] = PkSysFont(name, size)

    def update(self, delta_time: float) -> None:
        """Run update hooks."""
        pg.display.set_caption(f"{self.title} - {round(self.clock.get_fps(), 2)} FPS")
        self.event_manager.update(delta_time)
        self.scene_manager.current_scene.update(delta_time)

    def render(self) -> None:
        """Render the app."""
        self.internal_screen.fill(PkBasicPalette.WHITE)
        self.scene_manager.current_scene.render(self.internal_screen)

        scaled = pg.transform.scale(
            self.internal_screen.internal_surface, self.display_size.tuple
        )
        self.display.blit(scaled, (0, 0))
        pg.display.flip()

    def run(self, *, run_once: bool = False) -> None:
        """Run the app."""
        self.logger.info("Running app...")
        self.running = True

        while self.running:
            if run_once:
                self.quit()
            self.update(self.delta_time)
            self.render()
            self.delta_time = self.clock.tick(self.fps_limit) / 1000  # [seconds]

        pg.quit()

    def quit(self) -> None:
        """Quit the app."""
        self.logger.info(f"Quitting {self.app_name}...")
        self.running = False
