import pytest

from puffkit.geometry.rect import PkRect, RectValue


@pytest.mark.parametrize(
    "pos, size, expected_repr",
    [
        ((0, 0), (10, 10), "PkRect((0, 0), (10, 10))"),
        ((-5, -5), (15, 15), "PkRect((-5, -5), (15, 15))"),
        ((1, 1), (2, 2), "PkRect((1, 1), (2, 2))"),
        ((-10, -10), (20, 20), "PkRect((-10, -10), (20, 20))"),
    ],
)
def test_pkrect_repr(
    pos: tuple[float, float], size: tuple[float, float], expected_repr: str
) -> None:
    """Test the __repr__ method of PkRect."""
    rect = PkRect(pos, size)
    assert repr(rect) == expected_repr


@pytest.mark.parametrize(
    "pos, size, point, expected_result",
    [
        ((0, 0), (10, 10), (5, 5), True),
        ((0, 0), (10, 10), (15, 15), False),
        ((-5, -5), (15, 15), (0, 0), True),
        ((-5, -5), (15, 15), (-10, -10), False),
    ],
)
def test_pkrect_collidepoint(
    pos: tuple[float, float],
    size: tuple[float, float],
    point: tuple[float, float],
    expected_result: bool,
) -> None:
    """Test the collidepoint method of PkRect."""
    rect = PkRect(pos, size)
    assert rect.collidepoint(point) == expected_result


@pytest.mark.parametrize(
    "pos1, size1, pos2, size2, expected_result",
    [
        ((0, 0), (10, 10), (5, 5), (10, 10), True),
        ((0, 0), (10, 10), (15, 15), (10, 10), False),
        ((-5, -5), (15, 15), (0, 0), (10, 10), True),
        ((-5, -5), (15, 15), (20, 20), (10, 10), False),
    ],
)
def test_pkrect_colliderect(
    pos1: tuple[float, float],
    size1: tuple[float, float],
    pos2: tuple[float, float],
    size2: tuple[float, float],
    expected_result: bool,
) -> None:
    """Test the colliderect method of PkRect."""
    rect1 = PkRect(pos1, size1)
    rect2 = PkRect(pos2, size2)
    assert rect1.colliderect(rect2) == expected_result


@pytest.mark.parametrize(
    "pos, size, new_center, expected_center",
    [
        ((0, 0), (10, 10), (10, 10), (10, 10)),
        ((-5, -5), (15, 15), (0, 0), (0, 0)),
        ((1, 1), (2, 2), (2, 2), (2, 2)),
        ((-10, -10), (20, 20), (0, 0), (0, 0)),
    ],
)
def test_pkrect_center(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_center: tuple[float, float],
    expected_center: tuple[float, float],
) -> None:
    """Test the center property of PkRect."""
    rect = PkRect(pos, size)
    rect.center = new_center
    assert rect.center == expected_center


@pytest.mark.parametrize(
    "pos, size, new_topleft, expected_topleft",
    [
        ((0, 0), (10, 10), (10, 10), (10, 10)),
        ((-5, -5), (15, 15), (0, 0), (0, 0)),
        ((1, 1), (2, 2), (3, 3), (3, 3)),
        ((-10, -10), (20, 20), (-5, -5), (-5, -5)),
    ],
)
def test_pkrect_topleft(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_topleft: tuple[float, float],
    expected_topleft: tuple[float, float],
) -> None:
    """Test the topleft property of PkRect."""
    rect = PkRect(pos, size)
    rect.topleft = new_topleft
    assert rect.topleft == expected_topleft


@pytest.mark.parametrize(
    "pos, size, new_topright, expected_topright",
    [
        ((0, 0), (10, 10), (10, 10), (10, 10)),
        ((-5, -5), (15, 15), (0, 0), (0, 0)),
        ((1, 1), (2, 2), (3, 3), (3, 3)),
        ((-10, -10), (20, 20), (-5, -5), (-5, -5)),
    ],
)
def test_pkrect_topright(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_topright: tuple[float, float],
    expected_topright: tuple[float, float],
) -> None:
    """Test the topright property of PkRect."""
    rect = PkRect(pos, size)
    rect.topright = new_topright
    assert rect.topright == expected_topright


@pytest.mark.parametrize(
    "pos, size, new_bottomleft, expected_bottomleft",
    [
        ((0, 0), (10, 10), (10, 10), (10, 10)),
        ((-5, -5), (15, 15), (0, 0), (0, 0)),
        ((1, 1), (2, 2), (3, 3), (3, 3)),
        ((-10, -10), (20, 20), (-5, -5), (-5, -5)),
    ],
)
def test_pkrect_bottomleft(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_bottomleft: tuple[float, float],
    expected_bottomleft: tuple[float, float],
) -> None:
    """Test the bottomleft property of PkRect."""
    rect = PkRect(pos, size)
    rect.bottomleft = new_bottomleft
    assert rect.bottomleft == expected_bottomleft


@pytest.mark.parametrize(
    "pos, size, new_bottomright, expected_bottomright",
    [
        ((0, 0), (10, 10), (10, 10), (10, 10)),
        ((-5, -5), (15, 15), (0, 0), (0, 0)),
        ((1, 1), (2, 2), (3, 3), (3, 3)),
        ((-10, -10), (20, 20), (-5, -5), (-5, -5)),
    ],
)
def test_pkrect_bottomright(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_bottomright: tuple[float, float],
    expected_bottomright: tuple[float, float],
) -> None:
    """Test the bottomright property of PkRect."""
    rect = PkRect(pos, size)
    rect.bottomright = new_bottomright
    assert rect.bottomright == expected_bottomright


@pytest.mark.parametrize(
    "pos, size, new_left, expected_left",
    [
        ((0, 0), (10, 10), 10, 10),
        ((-5, -5), (15, 15), 0, 0),
        ((1, 1), (2, 2), 3, 3),
        ((-10, -10), (20, 20), -5, -5),
    ],
)
def test_pkrect_left(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_left: float,
    expected_left: float,
) -> None:
    """Test the left property of PkRect."""
    rect = PkRect(pos, size)
    rect.left = new_left
    assert rect.left == expected_left


@pytest.mark.parametrize(
    "pos, size, new_right, expected_right",
    [
        ((0, 0), (10, 10), 10, 10),
        ((-5, -5), (15, 15), 0, 0),
        ((1, 1), (2, 2), 3, 3),
        ((-10, -10), (20, 20), -5, -5),
    ],
)
def test_pkrect_right(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_right: float,
    expected_right: float,
) -> None:
    """Test the right property of PkRect."""
    rect = PkRect(pos, size)
    rect.right = new_right
    assert rect.right == expected_right


@pytest.mark.parametrize(
    "pos, size, new_top, expected_top",
    [
        ((0, 0), (10, 10), 10, 10),
        ((-5, -5), (15, 15), 0, 0),
        ((1, 1), (2, 2), 3, 3),
        ((-10, -10), (20, 20), -5, -5),
    ],
)
def test_pkrect_top(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_top: float,
    expected_top: float,
) -> None:
    """Test the top property of PkRect."""
    rect = PkRect(pos, size)
    rect.top = new_top
    assert rect.top == expected_top


@pytest.mark.parametrize(
    "pos, size, new_bottom, expected_bottom",
    [
        ((0, 0), (10, 10), 10, 10),
        ((-5, -5), (15, 15), 0, 0),
        ((1, 1), (2, 2), 3, 3),
        ((-10, -10), (20, 20), -5, -5),
    ],
)
def test_pkrect_bottom(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_bottom: float,
    expected_bottom: float,
) -> None:
    """Test the bottom property of PkRect."""
    rect = PkRect(pos, size)
    rect.bottom = new_bottom
    assert rect.bottom == expected_bottom


@pytest.mark.parametrize(
    "pos, size, new_topleft, expected_topleft",
    [
        ((0, 0), (10, 10), (10, 10), (10, 10)),
        ((-5, -5), (15, 15), (0, 0), (0, 0)),
        ((1, 1), (2, 2), (3, 3), (3, 3)),
        ((-10, -10), (20, 20), (-5, -5), (-5, -5)),
    ],
)
def test_pkrect_topleft(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_topleft: tuple[float, float],
    expected_topleft: tuple[float, float],
) -> None:
    """Test the topleft property of PkRect."""
    rect = PkRect(pos, size)
    rect.topleft = new_topleft
    assert rect.topleft == expected_topleft


@pytest.mark.parametrize(
    "pos, size, new_topright, expected_topright",
    [
        ((0, 0), (10, 10), (10, 10), (10, 10)),
        ((-5, -5), (15, 15), (0, 0), (0, 0)),
        ((1, 1), (2, 2), (3, 3), (3, 3)),
        ((-10, -10), (20, 20), (-5, -5), (-5, -5)),
    ],
)
def test_pkrect_topright(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_topright: tuple[float, float],
    expected_topright: tuple[float, float],
) -> None:
    """Test the topright property of PkRect."""
    rect = PkRect(pos, size)
    rect.topright = new_topright
    assert rect.topright == expected_topright


@pytest.mark.parametrize(
    "pos, size, new_bottomleft, expected_bottomleft",
    [
        ((0, 0), (10, 10), (10, 10), (10, 10)),
        ((-5, -5), (15, 15), (0, 0), (0, 0)),
        ((1, 1), (2, 2), (3, 3), (3, 3)),
        ((-10, -10), (20, 20), (-5, -5), (-5, -5)),
    ],
)
def test_pkrect_bottomleft(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_bottomleft: tuple[float, float],
    expected_bottomleft: tuple[float, float],
) -> None:
    """Test the bottomleft property of PkRect."""
    rect = PkRect(pos, size)
    rect.bottomleft = new_bottomleft
    assert rect.bottomleft == expected_bottomleft


@pytest.mark.parametrize(
    "pos, size, new_bottomright, expected_bottomright",
    [
        ((0, 0), (10, 10), (10, 10), (10, 10)),
        ((-5, -5), (15, 15), (0, 0), (0, 0)),
        ((1, 1), (2, 2), (3, 3), (3, 3)),
        ((-10, -10), (20, 20), (-5, -5), (-5, -5)),
    ],
)
def test_pkrect_bottomright(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_bottomright: tuple[float, float],
    expected_bottomright: tuple[float, float],
) -> None:
    """Test the bottomright property of PkRect."""
    rect = PkRect(pos, size)
    rect.bottomright = new_bottomright
    assert rect.bottomright == expected_bottomright


@pytest.mark.parametrize(
    "pos, size, new_center, expected_center",
    [
        ((0, 0), (10, 10), (10, 10), (10, 10)),
        ((-5, -5), (15, 15), (0, 0), (0, 0)),
        ((1, 1), (2, 2), (2, 2), (2, 2)),
        ((-10, -10), (20, 20), (0, 0), (0, 0)),
    ],
)
def test_pkrect_center(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_center: tuple[float, float],
    expected_center: tuple[float, float],
) -> None:
    """Test the center property of PkRect."""
    rect = PkRect(pos, size)
    rect.center = new_center
    assert rect.center == expected_center


@pytest.mark.parametrize(
    "pos, size, new_size, expected_size",
    [
        ((0, 0), (10, 10), (20, 20), (20, 20)),
        ((-5, -5), (15, 15), (10, 10), (10, 10)),
        ((1, 1), (2, 2), (3, 3), (3, 3)),
        ((-10, -10), (20, 20), (5, 5), (5, 5)),
    ],
)
def test_pkrect_size(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_size: tuple[float, float],
    expected_size: tuple[float, float],
) -> None:
    """Test the size property of PkRect."""
    rect = PkRect(pos, size)
    rect.size = new_size
    assert rect.size == expected_size


@pytest.mark.parametrize(
    "pos, size, new_width, expected_width",
    [
        ((0, 0), (10, 10), 20, 20),
        ((-5, -5), (15, 15), 10, 10),
        ((1, 1), (2, 2), 3, 3),
        ((-10, -10), (20, 20), 5, 5),
    ],
)
def test_pkrect_width(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_width: float,
    expected_width: float,
) -> None:
    """Test the width property of PkRect."""
    rect = PkRect(pos, size)
    rect.width = new_width
    assert rect.width == expected_width


@pytest.mark.parametrize(
    "pos, size, new_height, expected_height",
    [
        ((0, 0), (10, 10), 20, 20),
        ((-5, -5), (15, 15), 10, 10),
        ((1, 1), (2, 2), 3, 3),
        ((-10, -10), (20, 20), 5, 5),
    ],
)
def test_pkrect_height(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_height: float,
    expected_height: float,
) -> None:
    """Test the height property of PkRect."""
    rect = PkRect(pos, size)
    rect.height = new_height
    assert rect.height == expected_height


@pytest.mark.parametrize(
    "pos, size, new_pos, expected_pos",
    [
        ((0, 0), (10, 10), (10, 10), (10, 10)),
        ((-5, -5), (15, 15), (0, 0), (0, 0)),
        ((1, 1), (2, 2), (3, 3), (3, 3)),
        ((-10, -10), (20, 20), (-5, -5), (-5, -5)),
    ],
)
def test_pkrect_pos(
    pos: tuple[float, float],
    size: tuple[float, float],
    new_pos: tuple[float, float],
    expected_pos: tuple[float, float],
) -> None:
    """Test the pos property of PkRect."""
    rect = PkRect(pos, size)
    rect.pos = new_pos
    assert rect.pos == expected_pos


@pytest.mark.parametrize(
    "pos, size, new_x, expected_x",
    [
        ((0, 0), (10, 10), 10, 10),
        ((-5, -5), (15, 15), 0, 0),
        ((1, 1), (2, 2), 3, 3),
        ((-10, -10), (20, 20), -5, -5),
    ],
)
def test_pkrect_x(
    pos: tuple[float, float], size: tuple[float, float], new_x: float, expected_x: float
) -> None:
    """Test the x property of PkRect."""
    rect = PkRect(pos, size)
    rect.x = new_x
    assert rect.x == expected_x


@pytest.mark.parametrize(
    "pos, size, new_y, expected_y",
    [
        ((0, 0), (10, 10), 10, 10),
        ((-5, -5), (15, 15), 0, 0),
        ((1, 1), (2, 2), 3, 3),
        ((-10, -10), (20, 20), -5, -5),
    ],
)
def test_pkrect_y(
    pos: tuple[float, float], size: tuple[float, float], new_y: float, expected_y: float
) -> None:
    """Test the y property of PkRect."""
    rect = PkRect(pos, size)
    rect.y = new_y


@pytest.mark.parametrize(
    "pos, size, expected_copy",
    [
        ((0, 0), (10, 10), PkRect((0, 0), (10, 10))),
        ((-5, -5), (15, 15), PkRect((-5, -5), (15, 15))),
        ((1, 1), (2, 2), PkRect((1, 1), (2, 2))),
        ((-10, -10), (20, 20), PkRect((-10, -10), (20, 20))),
    ],
)
def test_pkrect_copy(
    pos: tuple[float, float], size: tuple[float, float], expected_copy: PkRect
) -> None:
    """Test the copy method of PkRect."""
    rect = PkRect(pos, size)
    rect_copy = rect.copy()
    assert rect_copy == expected_copy
    assert rect is not rect_copy


@pytest.mark.parametrize(
    "rect_value, expected_rect",
    [
        ((0, 0, 10, 10), PkRect((0, 0), (10, 10))),
        ((-5, -5, 15, 15), PkRect((-5, -5), (15, 15))),
        ((1, 1, 2, 2), PkRect((1, 1), (2, 2))),
        ((-10, -10, 20, 20), PkRect((-10, -10), (20, 20))),
    ],
)
def test_pkrect_from_tuple(rect_value: RectValue, expected_rect: PkRect) -> None:
    """Test the from_tuple method of PkRect."""
    rect = PkRect.from_tuple(rect_value)
    assert rect == expected_rect


@pytest.mark.parametrize(
    "pos, size, point, expected_result",
    [
        ((0, 0), (10, 10), (5, 5), True),
        ((0, 0), (10, 10), (15, 15), False),
        ((-5, -5), (15, 15), (0, 0), True),
        ((-5, -5), (15, 15), (-10, -10), False),
    ],
)
def test_pkrect_collidepoint(
    pos: tuple[float, float],
    size: tuple[float, float],
    point: tuple[float, float],
    expected_result: bool,
) -> None:
    """Test the collidepoint method of PkRect."""
    rect = PkRect(pos, size)
    assert rect.collidepoint(point) == expected_result


@pytest.mark.parametrize(
    "pos1, size1, pos2, size2, expected_result",
    [
        ((0, 0), (10, 10), (5, 5), (10, 10), True),
        ((0, 0), (10, 10), (15, 15), (10, 10), False),
        ((-5, -5), (15, 15), (0, 0), (10, 10), True),
        ((-5, -5), (15, 15), (20, 20), (10, 10), False),
    ],
)
def test_pkrect_colliderect(
    pos1: tuple[float, float],
    size1: tuple[float, float],
    pos2: tuple[float, float],
    size2: tuple[float, float],
    expected_result: bool,
) -> None:
    """Test the colliderect method of PkRect."""
    rect1 = PkRect(pos1, size1)
    rect2 = PkRect(pos2, size2)
    assert rect1.colliderect(rect2) == expected_result


@pytest.mark.parametrize(
    "pos, size, expected_midtop",
    [
        ((0, 0), (10, 10), (5, 0)),
        ((-5, -5), (15, 15), (2.5, -5)),
        ((1, 1), (2, 2), (2, 1)),
        ((-10, -10), (20, 20), (0, -10)),
    ],
)
def test_pkrect_midtop(
    pos: tuple[float, float],
    size: tuple[float, float],
    expected_midtop: tuple[float, float],
) -> None:
    """Test the midtop property of PkRect."""
    rect = PkRect(pos, size)
    assert rect.midtop == expected_midtop
    rect.midtop = (0, 0)
    assert rect.midtop == (0, 0)


@pytest.mark.parametrize(
    "pos, size, expected_midbottom",
    [
        ((0, 0), (10, 10), (5, 10)),
        ((-5, -5), (15, 15), (2.5, 10)),
        ((1, 1), (2, 2), (2, 3)),
        ((-10, -10), (20, 20), (0, 10)),
    ],
)
def test_pkrect_midbottom(
    pos: tuple[float, float],
    size: tuple[float, float],
    expected_midbottom: tuple[float, float],
) -> None:
    """Test the midbottom property of PkRect."""
    rect = PkRect(pos, size)
    assert rect.midbottom == expected_midbottom
    rect.midbottom = (0, 0)
    assert rect.midbottom == (0, 0)


@pytest.mark.parametrize(
    "pos, size, expected_midleft",
    [
        ((0, 0), (10, 10), (0, 5)),
        ((-5, -5), (15, 15), (-5, 2.5)),
        ((1, 1), (2, 2), (1, 2)),
        ((-10, -10), (20, 20), (-10, 0)),
    ],
)
def test_pkrect_midleft(
    pos: tuple[float, float],
    size: tuple[float, float],
    expected_midleft: tuple[float, float],
) -> None:
    """Test the midleft property of PkRect."""
    rect = PkRect(pos, size)
    assert rect.midleft == expected_midleft
    rect.midleft = (0, 0)
    assert rect.midleft == (0, 0)


@pytest.mark.parametrize(
    "pos, size, expected_midright",
    [
        ((0, 0), (10, 10), (10, 5)),
        ((-5, -5), (15, 15), (10, 2.5)),
        ((1, 1), (2, 2), (3, 2)),
        ((-10, -10), (20, 20), (10, 0)),
    ],
)
def test_pkrect_midright(
    pos: tuple[float, float],
    size: tuple[float, float],
    expected_midright: tuple[float, float],
) -> None:
    """Test the midright property of PkRect."""
    rect = PkRect(pos, size)
    assert rect.midright == expected_midright
    rect.midright = (0, 0)
    assert rect.midright == (0, 0)


def test_pkrect_iter() -> None:
    """Test the __iter__ method of PkRect."""
    rect = PkRect((0, 0), (10, 10))
    assert list(rect) == [0, 0, 10, 10]


@pytest.mark.parametrize(
    "rect, compare",
    [
        (PkRect((0, 0), (10, 10)), PkRect((0, 0), (10, 10))),
        (PkRect((-5, -5), (15, 15)), PkRect((-5, -5), (15, 15))),
        (PkRect((1, 1), (2, 2)), (1, 1, 2, 2)),
    ],
)
def test_pkrect_eq(rect: PkRect | RectValue, compare: PkRect | RectValue) -> None:
    """Test the __eq__ method of PkRect."""
    assert rect == compare


@pytest.mark.parametrize(
    "rect, compare",
    [
        (PkRect((0, 0), (10, 10)), PkRect((1, 1), (10, 10))),
        (PkRect((-5, -5), (15, 15)), PkRect((-5, -5), (10, 10))),
        (PkRect((1, 1), (2, 2)), (1, 1, 3, 3)),
    ],
)
def test_pkrect_ne(rect: PkRect | RectValue, compare: PkRect | RectValue) -> None:
    """Test the __ne__ method of PkRect."""
    assert rect != compare


def test_pkrect_getitem() -> None:
    """Test the __getitem__ method of PkRect."""
    rect = PkRect((0, 0), (10, 10))
    assert rect[0] == 0
    assert rect[1] == 0
    assert rect[2] == 10
    assert rect[3] == 10


def test_pkrect_str() -> None:
    """Test the __str__ method of PkRect."""
    rect = PkRect((0, 0), (10, 10))
    assert str(rect) == "PkRect((0, 0), (10, 10))"


def test_pkrect_from_pygame() -> None:
    """Test the from_pygame method of PkRect."""
    import pygame

    rect = pygame.Rect(0, 0, 10, 10)
    assert PkRect.from_pygame(rect) == PkRect((0, 0), (10, 10))
