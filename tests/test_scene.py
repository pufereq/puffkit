import pygame
import pytest
from unittest import mock
from puffkit.scene import PkScene
from puffkit.app import PkApp
from puffkit.surface import PkSurface
from puffkit.font.sysfont import PkSysFont


@pytest.fixture(scope="module")
def mock_app() -> PkApp:
    app = mock.Mock(spec=PkApp)
    app.internal_screen_size = (800, 600)
    return app


@pytest.fixture
def scene(mock_app: PkApp) -> PkScene:
    pygame.font.init()
    return PkScene(mock_app)


def test_scene_initialization(scene: PkScene, mock_app: PkApp) -> None:
    """Test the initialization of the scene."""
    assert scene.id == "PkScene"
    assert scene.size == mock_app.internal_screen_size
    assert scene.pos == (0, 0)
    assert isinstance(scene.surface, PkSurface)


def test_pkscene_input(scene: PkScene) -> None:
    """Test the input method of the scene."""
    scene.input(
        events=[],
        keys={},
        mouse_pos=(0, 0),
        mouse_buttons=(False, False, False),
    )
    # ensure error-free execution


@pytest.mark.parametrize("delta", [0.0, 0.016, 1.0])
def test_scene_update(scene: PkScene, delta: float) -> None:
    """Test the update method of the scene."""
    scene.update(delta)
    # ensure error-free execution


def test_scene_render(scene: PkScene) -> None:
    """Test the render method of the scene."""
    mock_dest = mock.Mock(spec=PkSurface)
    with mock.patch.object(scene, "draw") as mock_draw:
        scene.render(mock_dest)
        mock_draw.assert_called_once_with(mock_dest)


def test_scene_draw(scene: PkScene) -> None:
    """Test the draw method of the scene."""
    mock_screen = mock.Mock(spec=PkSurface)
    scene.draw(mock_screen)
    mock_screen.blit.assert_called_once_with(scene.surface, scene.surface.pos)
