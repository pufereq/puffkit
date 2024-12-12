# -*- coding: utf-8 -*-
"""Scene manager module for puffkit."""

from __future__ import annotations

from typing import TYPE_CHECKING

from puffkit.object import PkObject

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
        self.current_scene: PkScene | None = None

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

    def add_scene(self, scene: PkScene) -> None:
        """Add a scene to the scene manager.

        Args:
            scene (PkScene): Scene to add.

        Raises:
            ValueError: If a scene with the same ID already exists.
        """
        self.logger.debug(f"Adding scene {scene.id}...")
        if scene.id in self.scenes:
            raise ValueError(f"Scene with ID '{scene.id}' already exists.")

        if not scene.loaded and not scene.lazy:
            scene.load()

        self.scenes[scene.id] = scene

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
            self.logger.debug(f"Loading scene {scene_id}...")
            new_scene.load()

        self.current_scene = new_scene

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
        if self.current_scene is not None:
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
        if self.current_scene is not None:
            self.current_scene.update(dt)

    def render(self, dest: PkSurface) -> None:
        """Render the current scene."""
        if self.current_scene is not None:
            self.current_scene.render(dest)
