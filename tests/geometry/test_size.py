import pytest

from puffkit.geometry.size import PkSize


@pytest.mark.parametrize(
    "w, h, expected_str",
    [
        (10, 20, "(10, 20)"),
        (0, 0, "(0, 0)"),
        (-5, 15, "(-5, 15)"),
    ],
)
def test_pksize_str(w: int, h: int, expected_str: str) -> None:
    """Test the __str__ method of PkSize."""
    size = PkSize(w, h)
    assert str(size) == expected_str


@pytest.mark.parametrize(
    "w, h, expected_repr",
    [
        (10, 20, "PkSize(10, 20)"),
        (0, 0, "PkSize(0, 0)"),
        (-5, 15, "PkSize(-5, 15)"),
    ],
)
def test_pksize_repr(w: int, h: int, expected_repr: str) -> None:
    """Test the __repr__ method of PkSize."""
    size = PkSize(w, h)
    assert repr(size) == expected_repr


@pytest.mark.parametrize(
    "size1, size2, expected",
    [
        (PkSize(10, 20), PkSize(10, 20), True),
        (PkSize(10, 20), PkSize(5, 20), False),
        (PkSize(10, 20), (10, 15), False),
    ],
)
def test_pksize_eq(
    size1: PkSize, size2: PkSize | tuple[int | float, int | float], expected: bool
) -> None:
    """Test the __eq__ method of PkSize."""
    assert (size1 == size2) == expected


@pytest.mark.parametrize(
    "size1, size2, expected",
    [
        (PkSize(10, 20), PkSize(10, 20), False),
        (PkSize(10, 20), PkSize(5, 20), True),
        (PkSize(10, 20), (10, 15), True),
    ],
)
def test_pksize_ne(
    size1: PkSize, size2: PkSize | tuple[int | float, int | float], expected: bool
) -> None:
    """Test the __ne__ method of PkSize."""
    assert (size1 != size2) == expected


@pytest.mark.parametrize(
    "size1, size2, expected",
    [
        (PkSize(10, 20), PkSize(5, 10), PkSize(15, 30)),
        (PkSize(0, 0), PkSize(5, 10), PkSize(5, 10)),
        (PkSize(-5, 15), PkSize(5, -15), PkSize(0, 0)),
    ],
)
def test_pksize_add(size1: PkSize, size2: PkSize, expected: PkSize) -> None:
    """Test the __add__ method of PkSize."""
    assert size1 + size2 == expected


@pytest.mark.parametrize(
    "size1, size2, expected",
    [
        (PkSize(10, 20), PkSize(5, 10), PkSize(5, 10)),
        (PkSize(0, 0), PkSize(5, 10), PkSize(-5, -10)),
        (PkSize(-5, 15), PkSize(5, -15), PkSize(-10, 30)),
    ],
)
def test_pksize_sub(size1: PkSize, size2: PkSize, expected: PkSize) -> None:
    """Test the __sub__ method of PkSize."""
    assert size1 - size2 == expected


@pytest.mark.parametrize(
    "size, scalar, expected",
    [
        (PkSize(10, 20), 2, PkSize(20, 40)),
        (PkSize(0, 0), 5, PkSize(0, 0)),
        (PkSize(-5, 15), 3, PkSize(-15, 45)),
    ],
)
def test_pksize_mul(size: PkSize, scalar: int, expected: PkSize) -> None:
    """Test the __mul__ method of PkSize."""
    assert size * scalar == expected


@pytest.mark.parametrize(
    "size, scalar, expected",
    [
        (PkSize(10, 20), 2, PkSize(5, 10)),
        (PkSize(0, 0), 5, PkSize(0, 0)),
        (PkSize(-6, 15), 3, PkSize(-2, 5)),
    ],
)
def test_pksize_truediv(size: PkSize, scalar: int, expected: PkSize) -> None:
    """Test the __truediv__ method of PkSize."""
    assert size / scalar == expected


@pytest.mark.parametrize(
    "size, expected",
    [
        (PkSize(10, 20), [10, 20]),
        (PkSize(0, 0), [0, 0]),
        (PkSize(-5, 15), [-5, 15]),
    ],
)
def test_pksize_iter(size: PkSize, expected: list[int]) -> None:
    """Test the __iter__ method of PkSize."""
    assert list(size) == expected


@pytest.mark.parametrize(
    "size, index, expected",
    [
        (PkSize(10, 20), 0, 10),
        (PkSize(10, 20), 1, 20),
        (PkSize(-5, 15), 0, -5),
        (PkSize(-5, 15), 1, 15),
    ],
)
def test_pksize_getitem(size: PkSize, index: int, expected: int) -> None:
    """Test the __getitem__ method of PkSize."""
    assert size[index] == expected


def test_pksize_width() -> None:
    """Test the width property of PkSize."""
    size = PkSize(10, 20)
    assert size.width == 10


def test_pksize_height() -> None:
    """Test the height property of PkSize."""
    size = PkSize(10, 20)
    assert size.height == 20
