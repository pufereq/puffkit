import pytest
from unittest.mock import Mock
from puffkit import PkApp, PkScene, PkSurface
from puffkit.event import PkEvent
from puffkit.scene import PkSceneManager


@pytest.fixture(scope="module")
def mock_app() -> PkApp:
    class PkAppSubclass(PkApp):
        def __init__(self):
            super().__init__(
                app_name="TestApp",
                app_version="1.0",
                display_size=(10, 10),
                display_arguments={},
                internal_screen_size=(10, 10),
                fps_limit=60,
            )

    return PkAppSubclass()


@pytest.fixture
def scene_manager(mock_app: PkApp) -> PkSceneManager:
    return PkSceneManager(app=mock_app)


@pytest.fixture
def mock_scene() -> PkScene:
    scene = Mock(spec=PkScene)
    scene.id = "test_scene"
    scene.loaded = False
    scene.lazy = False
    scene.auto_unload = False
    return scene


@pytest.fixture
def scene(mock_app: PkApp) -> PkScene:
    class PkSceneSubclass(PkScene):
        def __init__(self):
            super().__init__(
                app=mock_app,
                _id="test_scene",
                lazy=False,
                auto_unload=False,
            )

    return PkSceneSubclass()


def test_loaded_scenes(scene_manager: PkSceneManager, mock_scene: PkScene) -> None:
    scene_manager.add_scene(mock_scene)
    assert scene_manager.loaded_scenes == ["fallback"]
    mock_scene.loaded = True
    assert scene_manager.loaded_scenes == ["fallback", "test_scene"]


def test_add_scene(scene_manager: PkSceneManager, mock_scene: PkScene) -> None:
    scene_manager.add_scene(mock_scene)
    assert "test_scene" in scene_manager.scenes


def test_add_scene_existing_id(
    scene_manager: PkSceneManager, mock_scene: PkScene
) -> None:
    scene_manager.add_scene(mock_scene)
    scene_manager.set_scene("test_scene")

    # add duplicate scene
    scene_manager.add_scene(mock_scene)

    # scene manager should change to fallback scene and display a warning
    assert scene_manager.current_scene.id == "fallback"


def test_set_scene(scene_manager: PkSceneManager, mock_scene: PkScene) -> None:
    scene_manager.add_scene(mock_scene)
    scene_manager.set_scene("test_scene")
    assert scene_manager.current_scene == mock_scene


def test_set_scene_nonexistent_id(scene_manager: PkSceneManager) -> None:
    with pytest.raises(ValueError, match="Scene with ID 'nonexistent' does not exist."):
        scene_manager.set_scene("nonexistent")


def test_set_scene_load_error(
    scene_manager: PkSceneManager, mock_scene: PkScene
) -> None:
    mock_scene.load.side_effect = ValueError("Test error")
    scene_manager.add_scene(mock_scene)
    scene_manager.set_scene("test_scene")
    assert scene_manager.current_scene.id == "fallback"


def test_set_scene_lazy(scene_manager: PkSceneManager, scene: PkScene) -> None:
    scene.lazy = True
    scene_manager.add_scene(scene)
    assert not scene_manager.scenes["test_scene"].loaded
    scene_manager.set_scene("test_scene")
    assert scene_manager.scenes["test_scene"].loaded


def test_set_scene_auto_unload(scene_manager: PkSceneManager, scene: PkScene) -> None:
    scene.auto_unload = True
    scene_manager.add_scene(scene)
    scene_manager.set_scene("test_scene")
    assert scene_manager.scenes["test_scene"].loaded
    scene_manager.set_scene("fallback")
    assert not scene_manager.scenes["test_scene"].loaded


def test_unload_scene(scene_manager: PkSceneManager, mock_scene: PkScene) -> None:
    scene_manager.add_scene(mock_scene)
    scene_manager.unload_scene("test_scene")
    mock_scene.unload.assert_called_once()


def test_unload_scene_nonexistent_id(scene_manager: PkSceneManager) -> None:
    with pytest.raises(ValueError, match="Scene with ID 'nonexistent' does not exist."):
        scene_manager.unload_scene("nonexistent")


def test_remove_scene(scene_manager: PkSceneManager, mock_scene: PkScene) -> None:
    scene_manager.add_scene(mock_scene)
    scene_manager.remove_scene("test_scene")
    assert "test_scene" not in scene_manager.scenes


def test_remove_scene_nonexistent_id(scene_manager: PkSceneManager) -> None:
    with pytest.raises(ValueError, match="Scene with ID 'nonexistent' does not exist."):
        scene_manager.remove_scene("nonexistent")


def test_input(scene_manager: PkSceneManager, mock_scene: PkScene) -> None:
    scene_manager.add_scene(mock_scene)
    scene_manager.set_scene("test_scene")
    events = [Mock(spec=PkEvent)]
    keys = {"key": True}
    mouse_pos = (100, 200)
    mouse_buttons = (True, False, False)
    scene_manager.input(events, keys, mouse_pos, mouse_buttons)
    mock_scene.input.assert_called_once_with(
        events=events, keys=keys, mouse_pos=mouse_pos, mouse_buttons=mouse_buttons
    )


def test_update(scene_manager: PkSceneManager, mock_scene: PkScene) -> None:
    scene_manager.add_scene(mock_scene)
    scene_manager.set_scene("test_scene")
    dt = 0.016
    scene_manager.update(dt)
    mock_scene.update.assert_called_once_with(dt)


def test_render(scene_manager: PkSceneManager, mock_scene: PkScene) -> None:
    scene_manager.add_scene(mock_scene)
    scene_manager.set_scene("test_scene")
    dest = Mock(spec=PkSurface)
    scene_manager.render(dest)
    mock_scene.render.assert_called_once_with(dest)
