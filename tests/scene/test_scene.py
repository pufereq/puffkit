import pytest
from unittest.mock import Mock
from puffkit.scene.scene import PkScene
from puffkit.app import PkApp
from puffkit.geometry.coordinate import PkCoordinate
from puffkit.surface import PkSurface


@pytest.fixture
def mock_app() -> Mock:
    app = Mock(spec=PkApp)
    app.internal_screen_size = (800, 600)
    return app


@pytest.fixture
def scene(mock_app: Mock) -> PkScene:
    return PkScene(_id="test_scene", app=mock_app, lazy=False, auto_unload=True)


def test_scene_initialization(scene: PkScene, mock_app: Mock) -> None:
    assert scene.id == "test_scene"
    assert scene.lazy is False
    assert scene.auto_unload is True
    assert scene.app == mock_app
    assert scene.size == (800, 600)
    assert scene.pos == PkCoordinate(0, 0)
    assert isinstance(scene.surface, PkSurface)
    assert scene.loaded is False


def test_scene_load(scene: PkScene) -> None:
    scene.on_load = Mock()
    scene.load()
    scene.on_load.assert_called_once()
    assert scene.loaded is True


def test_scene_unload(scene: PkScene) -> None:
    scene.on_unload = Mock()
    scene.load()
    scene.unload()
    scene.on_unload.assert_called_once()
    assert scene.loaded is False


@pytest.mark.parametrize("delta", [0.0, 0.1, 1.0])
def test_scene_update(scene: PkScene, delta: float) -> None:
    scene.on_update = Mock()
    scene.update(delta)
    scene.on_update.assert_called_once_with(delta)


def test_scene_render(scene: PkScene) -> None:
    mock_surface = Mock(spec=PkSurface)
    scene.on_render = Mock()
    scene.draw = Mock()
    scene.render(mock_surface)
    scene.on_render.assert_called_once()
    scene.draw.assert_called_once_with(mock_surface)


def test_scene_on_load(scene: PkScene) -> None:
    # this is a no-op method, so it should not raise any exceptions
    scene.on_load()


def test_scene_on_unload(scene: PkScene) -> None:
    # this is a no-op method, so it should not raise any exceptions
    scene.on_unload()


@pytest.mark.parametrize("delta", [0.0, 0.1, 1.0])
def test_scene_on_update(scene: PkScene, delta: float) -> None:
    # this is a no-op method, so it should not raise any exceptions
    scene.on_update(delta)


def test_scene_on_render(scene: PkScene) -> None:
    # this is a no-op method, so it should not raise any exceptions
    scene.on_render()
