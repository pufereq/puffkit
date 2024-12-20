# -*- coding: utf-8 -*-
"""Scene manager module for puffkit."""

from __future__ import annotations

from typing import TYPE_CHECKING

import traceback

from puffkit.object import PkObject
from puffkit.decorators.timing import Timer

if TYPE_CHECKING:  # pragma: no cover
    from puffkit import PkSurface, PkApp, PkScene
    from puffkit.event import PkEvent


class PkSceneManager(PkObject):
    """Scene manager class.

    The scene manager is responsible for managing scenes. It keeps track of all
    scenes and the current scene. It also handles input, updates, and rendering
    of the current scene.
    """

    def __init__(self, app: PkApp) -> None:
        """Initialize the scene manager.

        Args:
            app (PkApp): App instance.
        """
        super().__init__()
        self.app = app
        self.scenes: dict[str, PkScene] = {}

        from puffkit.scene.fallback_scene import PkFallbackScene

        self.fallback_scene: PkFallbackScene = PkFallbackScene(app)
        self.add_scene(self.fallback_scene)
        self.current_scene: PkScene = self.fallback_scene
        self.set_scene("fallback")

    def __str__(self) -> str:  # pragma: no cover
        return (
            f"<PkSceneManager current: {self.current_scene},"
            f" {len(self.scenes)} scenes, {len(self.loaded_scenes)} loaded>"
        )

    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"<PkSceneManager current={self.current_scene}, scene_count="
            f"{len(self.scenes)}, loaded_count={len(self.loaded_scenes)}>"
        )

    @property
    def loaded_scenes(self) -> list[str]:
        """Return a list of loaded scenes."""
        return [scene for scene in self.scenes if self.scenes[scene].loaded]

    def show_error_on_fallback(self, message: str) -> None:
        """Show an error message on the fallback scene.

        Args:
            message (str): Error message to show.
        """
        self.fallback_scene.set_message(message)
        self.set_scene("fallback")

    def add_scene(self, scene: PkScene) -> None:
        """Add a scene to the scene manager.

        Args:
            scene (PkScene): Scene to add.

        Raises:
            ValueError: If a scene with the same ID already exists.
        """
        self.logger.debug(f"Adding scene {scene.id}...")
        if scene.id in self.scenes:
            try:
                raise ValueError(f"Scene with ID '{scene.id}' already exists.")
            except ValueError as e:
                self.logger.exception(e)
                self.show_error_on_fallback(
                    f"Error adding scene: {e}\n\n{traceback.format_exc()}"
                )

        self.scenes[scene.id] = scene

        if not scene.loaded and not scene.lazy:
            self.load_scene(scene.id)

        self.logger.debug(f"Added scene {scene.id}. Scene count: {len(self.scenes)}")

    def set_scene(self, scene_id: str) -> None:
        """Set the current scene.

        Args:
            scene_id (str): ID of the scene to set as current.

        Raises:
            ValueError: If the scene ID does not exist.
        """
        self.logger.info(f"Setting scene to {scene_id}...")
        if scene_id not in self.scenes:
            raise ValueError(f"Scene with ID '{scene_id}' does not exist.")

        new_scene: PkScene = self.scenes[scene_id]

        if not new_scene.loaded:
            self.load_scene(scene_id, supress_error=True)

        if self.current_scene.auto_unload:
            self.logger.debug(f"Unloading scene {self.current_scene.id}...")
            self.current_scene.unload()
            self.logger.debug(
                f"Unloaded scene {self.current_scene.id}. Loaded scenes: {self.loaded_scenes}"
            )

        self.current_scene = new_scene

    def load_scene(self, scene_id: str, *, supress_error: bool = False) -> None:
        """Load a scene.

        Args:
            scene_id (str): ID of the scene to load.
            supress_error (bool): Whether to suppress errors. Defaults to False.

        Raises:
            ValueError: If the scene ID does not exist.
            Exception: If an error occurs while loading the scene.
        """
        self.logger.debug(f"Loading scene {scene_id}...")
        if scene_id not in self.scenes:
            raise ValueError(f"Scene with ID '{scene_id}' does not exist.")

        try:
            with Timer() as t:
                self.scenes[scene_id].load()
        except Exception as e:
            self.logger.exception(e)
            self.show_error_on_fallback(
                f"Error loading scene: {e}\n\n{traceback.format_exc()}"
            )
            if not supress_error:
                raise e
        else:
            self.logger.debug(f"Loaded scene {scene_id}. Took {t.elapsed} seconds.")

    def unload_scene(self, scene_id: str) -> None:
        """Unload a scene.

        Args:
            scene_id (str): ID of the scene to unload.

        Raises:
            ValueError: If the scene ID does not exist.
        """
        self.logger.debug(f"Unloading scene {scene_id}...")
        if scene_id not in self.scenes:
            raise ValueError(f"Scene with ID '{scene_id}' does not exist.")
        self.scenes[scene_id].unload()

    def remove_scene(self, scene_id: str) -> None:
        """Remove a scene from the scene manager.

        Args:
            scene_id (str): ID of the scene to remove.

        Raises:
            ValueError: If the scene ID does not exist.
        """
        self.logger.debug(f"Removing scene {scene_id}...")
        if scene_id not in self.scenes:
            raise ValueError(f"Scene with ID '{scene_id}' does not exist.")
        del self.scenes[scene_id]
        self.logger.debug(f"Removed scene {scene_id}. Scene count: {len(self.scenes)}")

    def input(
        self,
        events: list[PkEvent],
        keys: dict[str, bool],
        mouse_pos: tuple[int, int],
        mouse_buttons: tuple[bool, bool, bool],
    ) -> None:
        """Handle input for the current scene.

        Args:
            events (list[PkEvent]): Current event.
            keys (dict[str, bool]): Dictionary of keys and their states.
            mouse_pos (tuple[int, int]): Current mouse position.
            mouse_buttons (tuple[bool, bool, bool]): Dictionary of mouse buttons and their states.
        """
        self.current_scene.input(
            events=events,
            keys=keys,
            mouse_pos=mouse_pos,
            mouse_buttons=mouse_buttons,
        )

    def update(self, dt: float) -> None:
        """Update the current scene.

        Args:
            dt (float): Time since the last update.
        """
        self.current_scene.update(dt)

    def render(self, dest: PkSurface) -> None:
        """Render the current scene."""
        self.current_scene.render(dest)
