import pytest

from puffkit.geometry.coordinate import PkCoordinate


@pytest.mark.parametrize(
    "x, y, expected_str",
    [
        (1, 2, "(1, 2)"),
        (0, 0, "(0, 0)"),
        (-1, -2, "(-1, -2)"),
    ],
)
def test_str(x: int, y: int, expected_str: str) -> None:
    """Test the __str__ method of PkCoordinate."""
    coord = PkCoordinate(x, y)
    assert str(coord) == expected_str


@pytest.mark.parametrize(
    "x, y, expected_repr",
    [
        (1, 2, "PkCoordinate(1, 2)"),
        (0, 0, "PkCoordinate(0, 0)"),
        (-1, -2, "PkCoordinate(-1, -2)"),
    ],
)
def test_repr(x: int, y: int, expected_repr: str) -> None:
    """Test the __repr__ method of PkCoordinate."""
    coord = PkCoordinate(x, y)
    assert repr(coord) == expected_repr


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (1, 2, 3, 4, PkCoordinate(4, 6)),
        (0, 0, 0, 0, PkCoordinate(0, 0)),
        (-1, -2, 1, 2, PkCoordinate(0, 0)),
    ],
)
def test_add(x1: int, y1: int, x2: int, y2: int, expected: PkCoordinate) -> None:
    """Test the __add__ method of PkCoordinate."""
    coord1 = PkCoordinate(x1, y1)
    coord2 = PkCoordinate(x2, y2)
    assert coord1 + coord2 == expected


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (1, 2, 3, 4, PkCoordinate(-2, -2)),
        (0, 0, 0, 0, PkCoordinate(0, 0)),
        (-1, -2, 1, 2, PkCoordinate(-2, -4)),
    ],
)
def test_sub(x1: int, y1: int, x2: int, y2: int, expected: PkCoordinate) -> None:
    """Test the __sub__ method of PkCoordinate."""
    coord1 = PkCoordinate(x1, y1)
    coord2 = PkCoordinate(x2, y2)
    assert coord1 - coord2 == expected


@pytest.mark.parametrize(
    "x, y, scalar, expected",
    [
        (1, 2, 3, PkCoordinate(3, 6)),
        (0, 0, 5, PkCoordinate(0, 0)),
        (-1, -2, 2, PkCoordinate(-2, -4)),
    ],
)
def test_mul(x: int, y: int, scalar: int, expected: PkCoordinate) -> None:
    """Test the __mul__ method of PkCoordinate."""
    coord = PkCoordinate(x, y)
    assert coord * scalar == expected


@pytest.mark.parametrize(
    "x, y, scalar, expected",
    [
        (4, 8, 2, PkCoordinate(2, 4)),
        (0, 0, 1, PkCoordinate(0, 0)),
        (-4, -8, 2, PkCoordinate(-2, -4)),
    ],
)
def test_truediv(x: int, y: int, scalar: int, expected: PkCoordinate) -> None:
    """Test the __truediv__ method of PkCoordinate."""
    coord = PkCoordinate(x, y)
    assert coord / scalar == expected


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 2, (1, 2)),
        (0, 0, (0, 0)),
        (-1, -2, (-1, -2)),
    ],
)
def test_to_tuple(x: int, y: int, expected: tuple[int, int]) -> None:
    """Test the to_tuple method of PkCoordinate."""
    coord = PkCoordinate(x, y)
    assert coord.to_tuple() == expected


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 3, 4, 5.0),
        (1, 1, 4, 5, 5.0),
        (-1, -1, 2, 2, 4.242640687119285),
    ],
)
def test_distance_to(x1: int, y1: int, x2: int, y2: int, expected: float) -> None:
    """Test the distance_to method of PkCoordinate."""
    coord1 = PkCoordinate(x1, y1)
    coord2 = PkCoordinate(x2, y2)
    assert coord1.distance_to(coord2) == pytest.approx(expected)


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (1, 2, 1, 2, True),
        (0, 0, 0, 0, True),
        (1, 2, 2, 1, False),
    ],
)
def test_eq(x1: int, y1: int, x2: int, y2: int, expected: bool) -> None:
    """Test the __eq__ method of PkCoordinate."""
    coord1 = PkCoordinate(x1, y1)
    coord2 = PkCoordinate(x2, y2)
    assert (coord1 == coord2) == expected


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (1, 2, 1, 2, False),
        (0, 0, 0, 0, False),
        (1, 2, 2, 1, True),
    ],
)
def test_ne(x1: int, y1: int, x2: int, y2: int, expected: bool) -> None:
    """Test the __ne__ method of PkCoordinate."""
    coord1 = PkCoordinate(x1, y1)
    coord2 = PkCoordinate(x2, y2)
    assert (coord1 != coord2) == expected


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 2, [1, 2]),
        (0, 0, [0, 0]),
        (-1, -2, [-1, -2]),
    ],
)
def test_iter(x: int, y: int, expected: list[int]) -> None:
    """Test the __iter__ method of PkCoordinate."""
    coord = PkCoordinate(x, y)
    assert list(coord) == expected


@pytest.mark.parametrize(
    "x, y, index, expected",
    [
        (1, 2, 0, 1),
        (1, 2, 1, 2),
        (0, 0, 0, 0),
    ],
)
def test_getitem(x: int, y: int, index: int, expected: int) -> None:
    """Test the __getitem__ method of PkCoordinate."""
    coord = PkCoordinate(x, y)
    assert coord[index] == expected


@pytest.mark.parametrize(
    "coord_tuple, expected",
    [
        ((1, 2), PkCoordinate(1, 2)),
        ((0, 0), PkCoordinate(0, 0)),
        ((-1, -2), PkCoordinate(-1, -2)),
    ],
)
def test_from_tuple(coord_tuple: tuple[int, int], expected: PkCoordinate) -> None:
    """Test the from_tuple class method of PkCoordinate."""
    coord = PkCoordinate.from_tuple(coord_tuple)
    assert coord == expected
