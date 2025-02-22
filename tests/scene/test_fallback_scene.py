import pytest
from unittest.mock import Mock
from puffkit.scene.fallback_scene import PkFallbackScene
from puffkit import PkApp


@pytest.fixture
def mock_app() -> Mock:
    app = Mock(spec=PkApp)
    app.app_name = "TestApp"
    app.app_version = "1.0"
    app.fonts = {"default": Mock()}
    app.internal_screen_size = (200, 150)
    return app


@pytest.fixture
def fallback_scene(mock_app: Mock) -> PkFallbackScene:
    return PkFallbackScene(mock_app)


def test_initialization(fallback_scene: PkFallbackScene, mock_app: Mock) -> None:
    """Test the initialization of the fallback scene."""
    assert fallback_scene.app == mock_app
    assert fallback_scene.message == ""


def test_set_message(fallback_scene: PkFallbackScene) -> None:
    """Test setting a message in the fallback scene."""
    message = "Error occurred"
    fallback_scene.set_message(message)
    assert fallback_scene.message == message


@pytest.mark.parametrize("message", ["", "Error occurred", "Another message"])
def test_on_render(fallback_scene: PkFallbackScene, message: str) -> None:
    """Test rendering the fallback scene with different messages."""
    fallback_scene.set_message(message)
    fallback_scene.surface = Mock()
    fallback_scene.size = (200, 150)
    fallback_scene.on_render()
    fallback_scene.surface.fill.assert_called_once_with("#ffffff")
    fallback_scene.surface.blit_text.assert_called_once()
