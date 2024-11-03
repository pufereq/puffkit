# -*- coding: utf-8 -*-
"""puffkit App module."""
from __future__ import annotations

import pygame as pg

from puffkit.color.palettes import PkBasicPalette
from puffkit.font.font import PkFont
from puffkit.font.sysfont import PkSysFont
from puffkit.geometry.size import PkSize
from puffkit.object import PkObject
from puffkit.scene import PkScene
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
        fps: int = 60,
    ) -> None:
        """Initialize the app.

        Args:
            app_name (str): Name of the app.
            display_size (tuple[int, int]): Size of the display window.
            internal_screen_size (tuple[int, int]): Size of the internal screen.
            fps (int, optional): Frames per second. Defaults to 60.
        """
        super().__init__()

        if type(self) is PkApp:
            raise TypeError("PkApp class must be subclassed.")

        # set app info
        self.app_name: str = app_name
        self.app_version: str = app_version
        self.display_size: PkSize = PkSize(*display_size)
        self.internal_screen_size: PkSize = PkSize(*internal_screen_size)

        self.fps: int = fps
        self.delta_time: float = 1

        self.logger.info(f"Initializing {self.app_name} {self.app_version}...")

        # intialize pygame
        pg.init()

        # set up display
        self.display = pg.display.set_mode(self.display_size.tuple, **display_arguments)
        self.internal_screen = PkSurface(self.internal_screen_size)

        # set up fonts
        pg.font.init()
        self.fonts: dict[str, PkFont] = {}
        self.add_font("default", None, 12)

        # set up scenes
        self.scenes: dict[str, PkScene] = {}
        self.active_scene_id: str = "fallback"
        self.add_scene(PkScene("fallback", self, lazy=True))
        self.set_scene("fallback")

        # set up clock
        self.clock = pg.time.Clock()

        self.running: bool = False

    @property
    def active_scene(self) -> PkScene:
        """Get the active scene.

        Returns:
            PkScene: Active scene.
        """
        return self.scenes[self.active_scene_id]

    def add_scene(self, scene: PkScene) -> None:
        """Add a scene to the app.

        Args:
            scene (PkScene): Scene to add.
        """
        self.logger.debug(f"Adding scene {scene.id}...")
        self.scenes[scene.id] = scene

    def set_scene(self, scene_id: str) -> None:
        """Change the active scene.

        Args:
            scene_id (str): ID of the scene to change to.
        """
        self.logger.info(f"Changing scene to {scene_id}...")
        if scene_id not in self.scenes:
            raise ValueError(f"Scene {scene_id} not found.")

        self.active_scene_id = scene_id

        if not self.active_scene.initialized:
            self.active_scene.init()

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

    def handle_events(self) -> None:
        """Handle events."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            self.active_scene.input(
                events=pg.event.get(),
                keys=pg.key.get_pressed(),
                mouse_pos=pg.mouse.get_pos(),
                mouse_buttons=pg.mouse.get_pressed(),
            )

    def update(self, delta_time: float) -> None:
        """Run update hooks."""
        self.active_scene.update(delta_time)

    def render(self) -> None:
        """Render the app."""
        self.internal_screen.fill(PkBasicPalette.WHITE)
        self.active_scene.render(self.internal_screen)

        self.display.blit(self.internal_screen.internal_surface, (0, 0))
        pg.display.flip()

    def run(self, *, run_once: bool = False) -> None:
        """Run the app."""
        self.logger.info("Running app...")
        self.running = True

        while self.running:
            if run_once:
                self.quit()
            self.handle_events()
            self.update(self.delta_time)
            self.render()
            self.delta_time = self.clock.tick(self.fps) / 1000  # [seconds]

        pg.quit()

    def quit(self) -> None:
        """Quit the app."""
        self.logger.info(f"Quitting {self.app_name}...")
        self.running = False
