from unittest import mock

import pygame as pg
import pytest

from puffkit.app import PkApp
from puffkit.scene import PkScene


class PkAppSubclass(PkApp):
    """Subclass of PkApp for testing."""

    def __init__(self):
        super().__init__(
            app_name="TestApp",
            app_version="1.0",
            display_size=(800, 600),
            display_arguments={},
            internal_screen_size=(800, 600),
            fps_limit=60,
        )


@pytest.fixture(scope="module")
def app() -> PkAppSubclass:
    """Fixture for creating a PkApp instance."""
    return PkAppSubclass()


def test_pkapp_initialization(app: PkApp):
    """Test the initialization of the PkApp."""
    assert app.app_name == "TestApp"
    assert app.app_version == "1.0"
    assert app.display_size == (800, 600)
    assert app.internal_screen_size == (800, 600)
    assert app.fps_limit == 60
    assert app.running is False


def test_pkapp_exception():
    """Test raising an exception when instantiating PkApp."""
    with pytest.raises(TypeError):
        PkApp(
            app_name="TestApp",
            app_version="1.0",
            display_size=(800, 600),
            display_arguments={},
            internal_screen_size=(800, 600),
            fps_limit=60,
        )


def test_pkapp_add_scene(app: PkApp):
    """Test adding a scene to the app."""
    scene = mock.Mock(spec=PkScene)
    scene.id = "test_pkapp_scene"
    app.add_scene(scene)
    assert "test_pkapp_scene" in app.scenes


def test_pkapp_set_scene(app: PkApp):
    """Test changing the active scene."""
    scene = mock.Mock(spec=PkScene)
    scene.id = "test_pkapp_scene"
    app.add_scene(scene)
    scene.loaded = False
    app.set_scene("test_pkapp_scene")
    assert app.active_scene_id == "test_pkapp_scene"


def test_pkapp_set_scene_nonlazy(app: PkApp):
    """Test changing the active scene non-lazily."""
    scene = PkScene("test_pkapp_scene", app=app, lazy=False)
    app.add_scene(scene)
    assert app.scenes[scene.id].loaded is True
    app.set_scene("test_pkapp_scene")
    assert app.active_scene_id == "test_pkapp_scene"


def test_pkapp_set_scene_nonexistent(app: PkApp):
    """Test changing the active scene to a nonexistent scene."""
    with pytest.raises(ValueError):
        app.set_scene("nonexistent_scene")


def test_pkapp_add_font(app: PkApp):
    """Test adding a font to the app."""
    with mock.patch("puffkit.font.font.PkFont", autospec=True) as MockFont:
        with pytest.raises(FileNotFoundError):
            app.add_font("test_pkapp_font", "path/to/font.ttf", 12)
        MockFont.assert_not_called()


@mock.patch("puffkit.font.sysfont.pg.font.SysFont", autospec=True)
def test_pkapp_add_sysfont(MockSysFont: mock.Mock, app: PkApp):
    """Test adding a system font to the app."""
    app.add_sysfont("test_pkapp_sysfont", 12)
    assert "test_pkapp_sysfont" in app.fonts
    MockSysFont.assert_called_once()


def test_pkapp_update(app: PkApp):
    """Test updating the app."""
    scene = mock.Mock(spec=PkScene)
    scene.id = "test_pkapp_scene"
    app.add_scene(scene)
    scene.loaded = False
    app.set_scene("test_pkapp_scene")
    app.update(0.016)
    scene.update.assert_called_once_with(0.016)


def test_pkapp_render(app: PkApp):
    """Test rendering the app."""
    scene = mock.Mock(spec=PkScene)
    scene.id = "test_pkapp_scene"
    app.add_scene(scene)
    scene.loaded = False
    app.set_scene("test_pkapp_scene")
    with (
        mock.patch("pygame.display.flip"),
        mock.patch("puffkit.surface.PkSurface.fill"),
        mock.patch("puffkit.surface.PkSurface.blit"),
    ):
        app.render()
        scene.render.assert_called_once_with(app.internal_screen)


def test_pkapp_quit(app: PkApp):
    """Test quitting the app."""
    app.quit()
    assert app.running is False


def test_pkapp_run(app: PkApp):
    """Test running the app."""
    with (
        mock.patch("puffkit.app.PkApp.update"),
        mock.patch("puffkit.app.PkApp.render"),
    ):
        app.run(run_once=True)


def test_type_checking_imports():
    """Test importing PkApp with TYPE_CHECKING."""
    with mock.patch("typing.TYPE_CHECKING", True):
        from puffkit import app
        import importlib

        importlib.reload(app)

        assert PkScene
