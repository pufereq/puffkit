import pygame
import pytest
from unittest.mock import Mock
from puffkit import PkApp
from puffkit.event import PkEvent
from puffkit.event.event_manager import PkEventManager


@pytest.fixture
def mock_app() -> Mock:
    return Mock(spec=PkApp)


@pytest.fixture
def event_manager(mock_app: Mock) -> PkEventManager:
    pygame.init()
    return PkEventManager(mock_app)


def test_add_handler(event_manager: PkEventManager) -> None:
    handler = Mock()
    event_manager.add_handler(1, handler)
    assert event_manager.handlers[1] == handler


def test_add_handler_overwrite(event_manager: PkEventManager) -> None:
    handler1 = Mock()
    handler2 = Mock()
    event_manager.add_handler(1, handler1)
    event_manager.add_handler(1, handler2)
    assert event_manager.handlers[1] == handler2


def test_remove_handler(event_manager: PkEventManager) -> None:
    handler = Mock()
    event_manager.add_handler(1, handler)
    event_manager.remove_handler(1)
    assert 1 not in event_manager.handlers


def test_remove_handler_no_handler(event_manager: PkEventManager) -> None:
    event_manager.remove_handler(1)
    # No handler should be removed, so nothing to assert


def test_handle_events(event_manager: PkEventManager) -> None:
    handler = Mock()
    event_manager.add_handler(1, handler)
    event = PkEvent(type=1, dict={})
    event_manager.handle_events([event])
    handler.assert_called_once_with(event)


def test_handle_events_no_handler(event_manager: PkEventManager) -> None:
    event = PkEvent(type=1, dict={})
    event_manager.handle_events([event])
    # No handler should be called, so nothing to assert


def test_update(event_manager: PkEventManager, monkeypatch: pytest.MonkeyPatch) -> None:
    mock_event = Mock(type=1, dict={})
    monkeypatch.setattr("pygame.event.get", lambda: [mock_event])
    handler = Mock()
    event_manager.add_handler(1, handler)
    event_manager.update(0.1)
    handler.assert_called_once_with(event_manager.events[0])
