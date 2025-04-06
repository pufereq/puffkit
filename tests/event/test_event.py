import pytest
from unittest import mock
import pygame as pg
from puffkit.event.event import PkEvent


@pytest.mark.parametrize(
    "name, event_dict, kwargs",
    [
        ("test_event", {"key1": "value1"}, {}),
        ("another_event", {"key2": "value2"}, {"extra": "extra_value"}),
    ],
)
def test_pk_event_initialization(name: str, event_dict: dict, kwargs: dict) -> None:
    """Test the initialization of PkEvent."""
    event = PkEvent(name, event_dict, **kwargs)
    assert event.name == name
    assert event.dict == event_dict
    for key, value in kwargs.items():
        assert getattr(event, key) == value


def test_pk_event_from_pygame() -> None:
    """Test creating a PkEvent from a Pygame event."""
    mock_event = mock.Mock()
    mock_event.type = pg.USEREVENT
    mock_event.dict = {"key": "value"}
    pg_event_name = "USEREVENT"

    event = PkEvent.from_pygame(mock_event)
    assert event.name == pg_event_name
    assert event.dict == mock_event.dict


def test_pk_event_getattribute() -> None:
    """Test getting an attribute from PkEvent."""
    event = PkEvent("test_event", {"key": "value"})
    assert event.__getattribute__("name") == "test_event"


def test_pk_event_setattr() -> None:
    """Test setting an attribute in PkEvent."""
    event = PkEvent("test_event", {"key": "value"})
    event.__setattr__("new_attr", "new_value")
    assert event.new_attr == "new_value"


def test_pk_event_delattr() -> None:
    """Test deleting an attribute from PkEvent."""
    event = PkEvent("test_event", {"key": "value"})
    event.__setattr__("new_attr", "new_value")
    event.__delattr__("new_attr")
    with pytest.raises(AttributeError):
        getattr(event, "new_attr")


def test_pk_event_bool() -> None:
    """Test the truthiness of PkEvent."""
    event = PkEvent("test_event", {"key": "value"})
    assert bool(event) is True
