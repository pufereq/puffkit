# -*- coding: utf-8 -*-
"""Event manager module for puffkit."""

from __future__ import annotations

import logging as lg
import pygame as pg

from typing import TYPE_CHECKING, Any

from puffkit.event import PkEvent

if TYPE_CHECKING:  # pragma: no cover
    from puffkit.app import PkApp


class PkEventManager:
    """Event manager class for puffkit.

    The event manager is responsible for managing the events in the app.
    """

    def __init__(self, app: PkApp) -> None:
        """Initialize the event manager class."""
        self.logger = lg.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.debug("Initializing event manager...")

        self.app = app

        self.events: list[PkEvent] = []
        self.handlers: dict[int, Any] = {}

    def add_handler(self, event_type: int, handler: Any) -> None:
        """Add (or overwrite) a handler to the event manager."""
        if event_type in self.handlers:
            self.logger.warning(f"Overwriting handler for event type {event_type}...")
        self.handlers[event_type] = handler

    def remove_handler(self, event_type: int) -> None:
        """Remove a handler from the event manager."""
        if event_type in self.handlers:
            del self.handlers[event_type]
            self.logger.info(f"Removed handler for event type {event_type}.")
        else:
            self.logger.warning(f"No handler found for event type {event_type}.")

    def handle_events(self, event_list: list[PkEvent]) -> None:
        """Handle the events in the event manager."""
        for event in event_list:
            if event.type in self.handlers:
                self.handlers[event.type](event)

    def update(self, dt: float) -> None:
        """Update the event manager."""
        self.events = [PkEvent.from_pygame(e) for e in pg.event.get()]
        self.app.active_scene.input(
            events=self.events,
            keys=pg.key.get_pressed(),
            mouse_pos=pg.mouse.get_pos(),
            mouse_buttons=pg.mouse.get_pressed(),
        )
        self.handle_events(self.events)
