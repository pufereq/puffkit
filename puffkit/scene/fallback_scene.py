# -*- coding: utf-8 -*-

from sys import version as py_version

from puffkit import PkApp, PkScene, __version__ as puffkit_version


class PkFallbackScene(PkScene):
    """Fallback scene class.

    The fallback scene is used when no scene is active. It displays information
    about the app, puffkit, and Python. It can also display an error message.
    """

    def __init__(self, app: PkApp) -> None:
        """Initialize the fallback scene.

        Args:
            app (PkApp): App instance.
        """
        super().__init__("fallback", app, lazy=False, auto_unload=False)
        self.message: str = ""

    def set_message(self, message: str) -> None:
        """Set the message to display.

        Args:
            message (str): Message to display.
        """
        self.message = message
        self.on_load()

    def on_render(self) -> None:
        """Render the scene."""
        self.surface.fill("#ffffff")

        text: str = (
            "puffkit Fallback Scene\n"
            f"App: {self.app.app_name} {self.app.app_version}\n"
            f"puffkit {puffkit_version}\n"
            f"Python {py_version}\n"
        )

        if self.message:
            text += f"\n{self.message}"

        self.surface.blit_text(
            text,
            (10, 10, self.size[0] - 20, self.size[1] - 20),
            font=self.app.fonts["default"],
            color="#ff0000",
            antialias=True,
        )
