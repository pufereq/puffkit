import pytest
from unittest.mock import Mock, patch
from puffkit.event.event_manager import PkEventManager
from puffkit.event import PkEvent
from puffkit.app import PkApp


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


@pytest.fixture
def event_manager(app: PkAppSubclass) -> PkEventManager:
    return PkEventManager(app)


def test_add_handler(event_manager: PkEventManager):
    handler = Mock()
    event_manager.add_handler("test_event", handler)
    assert "test_event" in event_manager.handlers
    assert event_manager.handlers["test_event"] == handler


def test_add_handler_overwrite(event_manager: PkEventManager):
    handler1 = Mock()
    handler2 = Mock()
    event_manager.add_handler("test_event", handler1)
    event_manager.add_handler("test_event", handler2)
    assert event_manager.handlers["test_event"] == handler2


def test_remove_handler(event_manager: PkEventManager):
    handler = Mock()
    event_manager.add_handler("test_event", handler)
    event_manager.remove_handler("test_event")
    assert "test_event" not in event_manager.handlers


def test_remove_nonexistent_handler(event_manager: PkEventManager):
    event_manager.remove_handler("nonexistent_event")
    assert "nonexistent_event" not in event_manager.handlers


def test_handle_events(event_manager: PkEventManager):
    handler = Mock()
    event_manager.add_handler("test_event", handler)
    event = Mock(spec=PkEvent)
    event.name = "test_event"
    event_manager.handle_events([event])
    handler.assert_called_once_with(event)


def test_handle_events_no_handler(event_manager: PkEventManager):
    event = Mock(spec=PkEvent)
    event.name = "test_event"
    event_manager.handle_events([event])
    assert event_manager.handlers.get("test_event") is None


@patch("puffkit.event.event_manager.pg.event.get")
@patch("puffkit.event.event_manager.pg.key.get_pressed")
@patch("puffkit.event.event_manager.pg.mouse.get_pos")
@patch("puffkit.event.event_manager.pg.mouse.get_pressed")
@patch("puffkit.scene.scene_manager.PkSceneManager.input")
def test_update(
    mock_get_pressed: Mock,
    mock_get_pos: Mock,
    mock_get_mouse_pressed: Mock,
    mock_pg_event_get: Mock,
    mock_input: Mock,
    event_manager: PkEventManager,
):
    mock_pg_event_get.return_value = []
    mock_get_pressed.return_value = []
    mock_get_pos.return_value = (0, 0)
    mock_get_mouse_pressed.return_value = []

    event_manager.update(0.1)
    event_manager.app.active_scene.input.assert_called_once()
