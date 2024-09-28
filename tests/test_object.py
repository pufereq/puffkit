from typing import Any
from unittest import mock

import pytest

from puffkit.object import PkObject


@pytest.fixture
def pk_object() -> PkObject:
    """Fixture for creating a PkObject instance."""
    return PkObject()


def test_pkobject_initialization(pk_object: PkObject) -> None:
    """Test the initialization of PkObject."""
    assert pk_object.class_name == "PkObject"
    assert pk_object.full_class_name == "puffkit.object.PkObject"
    assert pk_object._input == {
        "events": [],
        "keys": {},
        "mouse_pos": (0, 0),
        "mouse_buttons": (False, False, False),
    }


@pytest.mark.parametrize(
    "events, keys, mouse_pos, mouse_buttons",
    [
        ([], {}, (0, 0), (False, False, False)),
        (["event1"], {"key1": True}, (100, 200), (True, False, False)),
        (["event2"], {"key2": False}, (300, 400), (False, True, True)),
    ],
)
def test_pkobject_input(
    pk_object: PkObject,
    events: list[Any],
    keys: dict[str, bool],
    mouse_pos: tuple[int, int],
    mouse_buttons: tuple[bool, bool, bool],
) -> None:
    """Test the input method of PkObject."""
    pk_object.input(events, keys, mouse_pos, mouse_buttons)
    assert pk_object._input == {
        "events": events,
        "keys": keys,
        "mouse_pos": mouse_pos,
        "mouse_buttons": mouse_buttons,
    }


def test_pkobject_update_not_implemented(pk_object: PkObject) -> None:
    """Test that update method raises NotImplementedError."""
    with pytest.raises(NotImplementedError):
        pk_object.update()


def test_pkobject_render_not_implemented(pk_object: PkObject) -> None:
    """Test that render method raises NotImplementedError."""
    with pytest.raises(NotImplementedError):
        pk_object.render()


def test_pkobject_str_not_implemented_log(pk_object: PkObject) -> None:
    """Test that __str__ method logs a warning."""
    with mock.patch.object(pk_object.logger, "warning") as mock_warning:
        str(pk_object)
        mock_warning.assert_called()


def test_pkobject_repr_not_implemented_log(pk_object: PkObject) -> None:
    """Test that __repr__ method logs a warning."""
    with mock.patch.object(pk_object.logger, "warning") as mock_warning:
        repr(pk_object)
        mock_warning.assert_called()
