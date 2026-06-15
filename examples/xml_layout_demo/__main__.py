# -*- coding: utf-8 -*-
"""Run the XML layout demo."""

from __future__ import annotations

import os
from dataclasses import dataclass

from puffkit import PkApp, PkScene, PkXmlLayoutLoader
from puffkit.widget import PkLabelWidget, PkTextInputWidget


@dataclass
class DemoViewModel:
    """View model for the XML layout demo."""

    title: str = "XML layout demo"
    status: str = "Waiting for input"
    layout: object | None = None

    def bind_layout(self, layout: object) -> None:
        """Attach the layout for widget updates."""
        self.layout = layout

    def on_start(self, widget: object, event: object) -> None:
        """Handle the Start button click."""
        self.status = "Start clicked"
        self._sync_status()

    def on_name_change(self, widget: PkTextInputWidget, event: object) -> None:
        """Handle text input changes."""
        if widget.text:
            self.status = f"Hello, {widget.text}!"
        else:
            self.status = "Waiting for input"
        self._sync_status()

    def _sync_status(self) -> None:
        """Push the status string into the status label widget."""
        if self.layout is None:
            return
        status_widget = self.layout.get_widget("status")
        if isinstance(status_widget, PkLabelWidget):
            status_widget.set_text(self.status)


class DemoScene(PkScene):
    """Scene that renders an XML layout."""

    def __init__(self, app: PkApp) -> None:
        """Initialize the demo scene."""
        super().__init__("xml_layout_demo", app, lazy=False, auto_unload=False)
        self.view_model = DemoViewModel()
        self.layout = None

    def on_load(self) -> None:
        """Load the XML layout and resources."""
        loader = PkXmlLayoutLoader()
        base_dir = os.path.dirname(__file__)
        layout_path = os.path.join(base_dir, "layout.xml")
        resources_path = os.path.join(base_dir, "resources.json")
        self.layout = loader.load_from_file(
            self,
            layout_path,
            view_model=self.view_model,
            resources_path=resources_path,
        )
        self.view_model.bind_layout(self.layout)

    def on_update(self, delta: float) -> None:
        """Update the layout widgets."""
        if self.layout is None:
            return
        self.layout.input(
            self._input["events"],
            self._input["keys"],
            self._input["mouse_pos"],
            self._input["mouse_buttons"],
        )
        self.layout.update(delta)

    def on_render(self) -> None:
        """Render the layout."""
        if self.layout is None:
            return
        self.layout.render()


class DemoApp(PkApp):
    """App that boots the XML layout demo scene."""

    def __init__(self) -> None:
        """Initialize the demo app and scene."""
        super().__init__(
            "puffkit XML demo",
            "0.1.0",
            (640, 360),
            {},
            (320, 180),
        )
        self.event_manager.add_handler("QUIT", lambda _: self.quit())
        self.scene_manager.add_scene(DemoScene(self))
        self.scene_manager.set_scene("xml_layout_demo")


if __name__ == "__main__":
    DemoApp().run()
