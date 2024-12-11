import pytest
from puffkit.event.event import PkEvent


@pytest.mark.parametrize(
    "type, _dict, kwargs, expected_str",
    [
        (1, {"key": "value"}, {}, "<PkEvent type=1 dict={'key': 'value'}>"),
        (
            2,
            {"another_key": 123},
            {"extra": "data"},
            "<PkEvent type=2 dict={'another_key': 123}>",
        ),
    ],
)
def test_pkevent_initialization(
    type: int, _dict: dict, kwargs: dict, expected_str: str
) -> None:
    """Test the initialization of PkEvent."""
    event = PkEvent(type, _dict, **kwargs)
    assert event.type == type
    assert event.dict == _dict
    for key, value in kwargs.items():
        assert getattr(event, key) == value
    assert str(event) == expected_str


def test_pkevent_from_pygame() -> None:
    """Test creating a PkEvent from a Pygame event."""

    class MockPygameEvent:
        def __init__(self, type: int, _dict: dict):
            self.type = type
            self.dict = _dict

    pygame_event = MockPygameEvent(3, {"pygame_key": "pygame_value"})
    event = PkEvent.from_pygame(pygame_event)
    assert event.type == pygame_event.type
    assert event.dict == pygame_event.dict


def test_pkevent_str() -> None:
    """Test the string representation of PkEvent."""
    event = PkEvent(4, {"test_key": "test_value"})
    assert str(event) == "<PkEvent type=4 dict={'test_key': 'test_value'}>"


def test_pkevent_repr() -> None:
    """Test the repr representation of PkEvent."""
    event = PkEvent(5, {"repr_key": "repr_value"})
    assert repr(event) == "<PkEvent type=5 dict={'repr_key': 'repr_value'}>"


def test_pkevent_getattribute() -> None:
    """Test getting an attribute from PkEvent."""
    event = PkEvent(6, {"attr_key": "attr_value"})
    assert event.__getattribute__("attr_key") == "attr_value"


def test_pkevent_setattr() -> None:
    """Test setting an attribute in PkEvent."""
    event = PkEvent(7, {})
    event.__setattr__("new_attr", "new_value")
    assert event.new_attr == "new_value"


def test_pkevent_delattr() -> None:
    """Test deleting an attribute from PkEvent."""
    event = PkEvent(8, {"del_key": "del_value"})
    event.__delattr__("del_key")
    with pytest.raises(AttributeError):
        _ = event.del_key


def test_pkevent_bool() -> None:
    """Test the truthiness of PkEvent."""
    event = PkEvent(9, {})
    assert bool(event) is True
