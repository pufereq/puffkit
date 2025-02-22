import pytest

from puffkit.geometry.rect import PkRect, RectValue


@pytest.mark.parametrize(
    "x, y, w, h, expected_repr",
    [
        (0, 0, 10, 10, "PkRect(0, 0, 10, 10)"),
        (-5, -5, 15, 15, "PkRect(-5, -5, 15, 15)"),
        (1, 1, 2, 2, "PkRect(1, 1, 2, 2)"),
        (-10, -10, 20, 20, "PkRect(-10, -10, 20, 20)"),
    ],
)
def test_pkrect_repr(
    x: float, y: float, w: float, h: float, expected_repr: str
) -> None:
    """Test the __repr__ method of PkRect."""
    rect = PkRect(x, y, w, h)
    assert repr(rect) == expected_repr


@pytest.mark.parametrize(
    "x, y, w, h, point, expected_result",
    [
        (0, 0, 10, 10, (5, 5), True),
        (0, 0, 10, 10, (15, 15), False),
        (-5, -5, 15, 15, (0, 0), True),
        (-5, -5, 15, 15, (-10, -10), False),
    ],
)
def test_pkrect_collidepoint(
    x: float,
    y: float,
    w: float,
    h: float,
    point: tuple[float, float],
    expected_result: bool,
) -> None:
    """Test the collidepoint method of PkRect."""
    rect = PkRect(x, y, w, h)
    assert rect.collidepoint(point) == expected_result


@pytest.mark.parametrize(
    "x1, y1, w1, h1, x2, y2, w2, h2, expected_result",
    [
        (0, 0, 10, 10, 5, 5, 10, 10, True),
        (0, 0, 10, 10, 15, 15, 10, 10, False),
        (-5, -5, 15, 15, 0, 0, 10, 10, True),
        (-5, -5, 15, 15, 20, 20, 10, 10, False),
    ],
)
def test_pkrect_colliderect(
    x1: float,
    y1: float,
    w1: float,
    h1: float,
    x2: float,
    y2: float,
    w2: float,
    h2: float,
    expected_result: bool,
) -> None:
    """Test the colliderect method of PkRect."""
    rect1 = PkRect(x1, y1, w1, h1)
    rect2 = PkRect(x2, y2, w2, h2)
    assert rect1.colliderect(rect2) == expected_result


@pytest.mark.parametrize(
    "x, y, w, h, new_center, expected_center",
    [
        (0, 0, 10, 10, (10, 10), (10, 10)),
        (-5, -5, 15, 15, (0, 0), (0, 0)),
        (1, 1, 2, 2, (2, 2), (2, 2)),
        (-10, -10, 20, 20, (0, 0), (0, 0)),
    ],
)
def test_pkrect_center(
    x: float,
    y: float,
    w: float,
    h: float,
    new_center: tuple[float, float],
    expected_center: tuple[float, float],
) -> None:
    """Test the center property of PkRect."""
    rect = PkRect(x, y, w, h)
    rect.center = new_center
    assert rect.center == expected_center


@pytest.mark.parametrize(
    "x, y, w, h, new_topleft, expected_topleft",
    [
        (0, 0, 10, 10, (10, 10), (10, 10)),
        (-5, -5, 15, 15, (0, 0), (0, 0)),
        (1, 1, 2, 2, (3, 3), (3, 3)),
        (-10, -10, 20, 20, (-5, -5), (-5, -5)),
    ],
)
def test_pkrect_topleft(
    x: float,
    y: float,
    w: float,
    h: float,
    new_topleft: tuple[float, float],
    expected_topleft: tuple[float, float],
) -> None:
    """Test the topleft property of PkRect."""
    rect = PkRect(x, y, w, h)
    rect.topleft = new_topleft
    assert rect.topleft == expected_topleft


@pytest.mark.parametrize(
    "x, y, w, h, new_topright, expected_topright",
    [
        (0, 0, 10, 10, (10, 10), (10, 10)),
        (-5, -5, 15, 15, (0, 0), (0, 0)),
        (1, 1, 2, 2, (3, 3), (3, 3)),
        (-10, -10, 20, 20, (-5, -5), (-5, -5)),
    ],
)
def test_pkrect_topright(
    x: float,
    y: float,
    w: float,
    h: float,
    new_topright: tuple[float, float],
    expected_topright: tuple[float, float],
) -> None:
    """Test the topright property of PkRect."""
    rect = PkRect(x, y, w, h)
    rect.topright = new_topright
    assert rect.topright == expected_topright


@pytest.mark.parametrize(
    "x, y, w, h, new_bottomleft, expected_bottomleft",
    [
        (0, 0, 10, 10, (10, 10), (10, 10)),
        (-5, -5, 15, 15, (0, 0), (0, 0)),
        (1, 1, 2, 2, (3, 3), (3, 3)),
        (-10, -10, 20, 20, (-5, -5), (-5, -5)),
    ],
)
def test_pkrect_bottomleft(
    x: float,
    y: float,
    w: float,
    h: float,
    new_bottomleft: tuple[float, float],
    expected_bottomleft: tuple[float, float],
) -> None:
    """Test the bottomleft property of PkRect."""
    rect = PkRect(x, y, w, h)
    rect.bottomleft = new_bottomleft
    assert rect.bottomleft == expected_bottomleft


@pytest.mark.parametrize(
    "x, y, w, h, new_bottomright, expected_bottomright",
    [
        (0, 0, 10, 10, (10, 10), (10, 10)),
        (-5, -5, 15, 15, (0, 0), (0, 0)),
        (1, 1, 2, 2, (3, 3), (3, 3)),
        (-10, -10, 20, 20, (-5, -5), (-5, -5)),
    ],
)
def test_pkrect_bottomright(
    x: float,
    y: float,
    w: float,
    h: float,
    new_bottomright: tuple[float, float],
    expected_bottomright: tuple[float, float],
) -> None:
    """Test the bottomright property of PkRect."""
    rect = PkRect(x, y, w, h)
    rect.bottomright = new_bottomright
    assert rect.bottomright == expected_bottomright


@pytest.mark.parametrize(
    "x, y, w, h, new_left, expected_left",
    [
        (0, 0, 10, 10, 10, 10),
        (-5, -5, 15, 15, 0, 0),
        (1, 1, 2, 2, 3, 3),
        (-10, -10, 20, 20, -5, -5),
    ],
)
def test_pkrect_left(
    x: float, y: float, w: float, h: float, new_left: float, expected_left: float
) -> None:
    """Test the left property of PkRect."""
    rect = PkRect(x, y, w, h)
    rect.left = new_left
    assert rect.left == expected_left


@pytest.mark.parametrize(
    "x, y, w, h, new_right, expected_right",
    [
        (0, 0, 10, 10, 10, 10),
        (-5, -5, 15, 15, 0, 0),
        (1, 1, 2, 2, 3, 3),
        (-10, -10, 20, 20, -5, -5),
    ],
)
def test_pkrect_right(
    x: float, y: float, w: float, h: float, new_right: float, expected_right: float
) -> None:
    """Test the right property of PkRect."""
    rect = PkRect(x, y, w, h)
    rect.right = new_right
    assert rect.right == expected_right


@pytest.mark.parametrize(
    "x, y, w, h, new_top, expected_top",
    [
        (0, 0, 10, 10, 10, 10),
        (-5, -5, 15, 15, 0, 0),
        (1, 1, 2, 2, 3, 3),
        (-10, -10, 20, 20, -5, -5),
    ],
)
def test_pkrect_top(
    x: float, y: float, w: float, h: float, new_top: float, expected_top: float
) -> None:
    """Test the top property of PkRect."""
    rect = PkRect(x, y, w, h)
    rect.top = new_top
    assert rect.top == expected_top


@pytest.mark.parametrize(
    "x, y, w, h, new_bottom, expected_bottom",
    [
        (0, 0, 10, 10, 10, 10),
        (-5, -5, 15, 15, 0, 0),
        (1, 1, 2, 2, 3, 3),
        (-10, -10, 20, 20, -5, -5),
    ],
)
def test_pkrect_bottom(
    x: float, y: float, w: float, h: float, new_bottom: float, expected_bottom: float
) -> None:
    """Test the bottom property of PkRect."""
    rect = PkRect(x, y, w, h)
    rect.bottom = new_bottom
    assert rect.bottom == expected_bottom


@pytest.mark.parametrize(
    "x, y, w, h, new_pos, expected_pos",
    [
        (0, 0, 10, 10, (10, 10), (10, 10)),
        (-5, -5, 15, 15, (0, 0), (0, 0)),
        (1, 1, 2, 2, (3, 3), (3, 3)),
        (-10, -10, 20, 20, (-5, -5), (-5, -5)),
    ],
)
def test_pkrect_pos(
    x: float,
    y: float,
    w: float,
    h: float,
    new_pos: tuple[float, float],
    expected_pos: tuple[float, float],
) -> None:
    """Test the pos property of PkRect."""
    rect = PkRect(x, y, w, h)
    rect.pos = new_pos
    assert rect.pos == expected_pos


@pytest.mark.parametrize(
    "x, y, w, h, new_x, expected_x",
    [
        (0, 0, 10, 10, 10, 10),
        (-5, -5, 15, 15, 0, 0),
        (1, 1, 2, 2, 3, 3),
        (-10, -10, 20, 20, -5, -5),
    ],
)
def test_pkrect_x(
    x: float, y: float, w: float, h: float, new_x: float, expected_x: float
) -> None:
    """Test the x property of PkRect."""
    rect = PkRect(x, y, w, h)
    rect.x = new_x
    assert rect.x == expected_x


@pytest.mark.parametrize(
    "x, y, w, h, new_y, expected_y",
    [
        (0, 0, 10, 10, 10, 10),
        (-5, -5, 15, 15, 0, 0),
        (1, 1, 2, 2, 3, 3),
        (-10, -10, 20, 20, -5, -5),
    ],
)
def test_pkrect_y(
    x: float, y: float, w: float, h: float, new_y: float, expected_y: float
) -> None:
    """Test the y property of PkRect."""
    rect = PkRect(x, y, w, h)
    rect.y = new_y
    assert rect.y == expected_y


@pytest.mark.parametrize(
    "x, y, w, h, expected_copy",
    [
        (0, 0, 10, 10, PkRect(0, 0, 10, 10)),
        (-5, -5, 15, 15, PkRect(-5, -5, 15, 15)),
        (1, 1, 2, 2, PkRect(1, 1, 2, 2)),
        (-10, -10, 20, 20, PkRect(-10, -10, 20, 20)),
    ],
)
def test_pkrect_copy(
    x: float, y: float, w: float, h: float, expected_copy: PkRect
) -> None:
    """Test the copy method of PkRect."""
    rect = PkRect(x, y, w, h)
    rect_copy = rect.copy()
    assert rect_copy == expected_copy
    assert rect is not rect_copy


@pytest.mark.parametrize(
    "x, y, w, h, expected_midtop",
    [
        (0, 0, 10, 10, (5, 0)),
        (-5, -5, 15, 15, (2.5, -5)),
        (1, 1, 2, 2, (2, 1)),
        (-10, -10, 20, 20, (0, -10)),
    ],
)
def test_pkrect_midtop(
    x: float, y: float, w: float, h: float, expected_midtop: tuple[float, float]
) -> None:
    """Test the midtop property of PkRect."""
    rect = PkRect(x, y, w, h)
    assert rect.midtop == expected_midtop
    rect.midtop = (0, 0)
    assert rect.midtop == (0, 0)


@pytest.mark.parametrize(
    "x, y, w, h, expected_midbottom",
    [
        (0, 0, 10, 10, (5, 10)),
        (-5, -5, 15, 15, (2.5, 10)),
        (1, 1, 2, 2, (2, 3)),
        (-10, -10, 20, 20, (0, 10)),
    ],
)
def test_pkrect_midbottom(
    x: float, y: float, w: float, h: float, expected_midbottom: tuple[float, float]
) -> None:
    """Test the midbottom property of PkRect."""
    rect = PkRect(x, y, w, h)
    assert rect.midbottom == expected_midbottom
    rect.midbottom = (0, 0)
    assert rect.midbottom == (0, 0)


@pytest.mark.parametrize(
    "x, y, w, h, expected_midleft",
    [
        (0, 0, 10, 10, (0, 5)),
        (-5, -5, 15, 15, (-5, 2.5)),
        (1, 1, 2, 2, (1, 2)),
        (-10, -10, 20, 20, (-10, 0)),
    ],
)
def test_pkrect_midleft(
    x: float, y: float, w: float, h: float, expected_midleft: tuple[float, float]
) -> None:
    """Test the midleft property of PkRect."""
    rect = PkRect(x, y, w, h)
    assert rect.midleft == expected_midleft
    rect.midleft = (0, 0)
    assert rect.midleft == (0, 0)


@pytest.mark.parametrize(
    "x, y, w, h, expected_midright",
    [
        (0, 0, 10, 10, (10, 5)),
        (-5, -5, 15, 15, (10, 2.5)),
        (1, 1, 2, 2, (3, 2)),
        (-10, -10, 20, 20, (10, 0)),
    ],
)
def test_pkrect_midright(
    x: float, y: float, w: float, h: float, expected_midright: tuple[float, float]
) -> None:
    """Test the midright property of PkRect."""
    rect = PkRect(x, y, w, h)
    assert rect.midright == expected_midright
    rect.midright = (0, 0)
    assert rect.midright == (0, 0)


def test_pkrect_iter() -> None:
    """Test the __iter__ method of PkRect."""
    rect = PkRect(0, 0, 10, 10)
    assert list(rect) == [0, 0, 10, 10]


def test_pkrect_eq() -> None:
    """Test the __eq__ method of PkRect."""
    rect1 = PkRect(0, 0, 10, 10)
    rect2 = PkRect(0, 0, 10, 10)
    rect3 = PkRect(0, 0, 5, 5)
    assert rect1 == rect2
    assert rect1 == (0, 0, 10, 10)
    assert rect1 != rect3
    assert rect2 != rect3
    with pytest.raises(TypeError):
        assert rect1 != 0


def test_pkrect_getitem() -> None:
    """Test the __getitem__ method of PkRect."""
    rect = PkRect(0, 0, 10, 10)
    assert rect[0] == 0
    assert rect[1] == 0
    assert rect[2] == 10
    assert rect[3] == 10
    with pytest.raises(IndexError):
        rect[4]


def test_pkrect_width_height() -> None:
    """Test the width and height properties of PkRect."""
    rect = PkRect(0, 0, 10, 10)
    assert rect.width == 10
    assert rect.height == 10
    rect.width = 5
    rect.height = 5
    assert rect.width == 5
    assert rect.height == 5


def test_pkrect_size() -> None:
    """Test the size property of PkRect."""
    rect = PkRect(0, 0, 10, 10)
    assert rect.size == (10, 10)
    rect.size = (5, 5)
    assert rect.size == (5, 5)
