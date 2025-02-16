from unittest import mock
import pygame
import pytest

from puffkit.color.color import ColorValue, PkColor
from puffkit.font.font import PkFont
from puffkit.geometry import RectValue
from puffkit.geometry.rect import PkRect
from puffkit.surface import PkSurface


@pytest.fixture(scope="module")
def display() -> pygame.Surface:
    """Fixture for initializing Pygame."""
    pygame.init()
    yield pygame.display.set_mode((100, 100))
    pygame.quit()


@pytest.fixture
def surface(display: pygame.Surface) -> PkSurface:
    """Fixture for creating a PkSurface instance."""
    return PkSurface(size=(100, 100))


@pytest.fixture
def surface_8bit(display: pygame.Surface) -> PkSurface:
    """Fixture for creating a PkSurface instance with 8-bit depth."""
    return PkSurface(size=(100, 100), depth=8)


@pytest.mark.parametrize(
    "size, pos, expected_size, expected_pos",
    [
        ((100, 100), (0, 0), (100, 100), (0, 0)),
        ((200, 150), (10, 20), (200, 150), (10, 20)),
    ],
)
def test_pksurface_initialization(
    size: tuple[int, int],
    pos: tuple[int, int],
    expected_size: tuple[int, int],
    expected_pos: tuple[int, int],
) -> None:
    """Test the initialization of PkSurface."""
    surface = PkSurface(size=size, pos=pos)
    assert surface.size == expected_size
    assert surface.pos == expected_pos


def test_pksurface_transparent() -> None:
    """Test creating a transparent surface."""
    surface = PkSurface(size=(100, 100), transparent=True)
    surface.fill(PkColor(10, 0, 0, 10))
    assert surface.get_at((0, 0)) == (10, 0, 0, 10)


def test_pksurface_size(surface: PkSurface) -> None:
    """Test getting the size of the surface."""
    assert surface.size == (100, 100)


def test_pksurface_width(surface: PkSurface) -> None:
    """Test getting the width of the surface."""
    assert surface.width == 100


def test_pksurface_height(surface: PkSurface) -> None:
    """Test getting the height of the surface."""
    assert surface.height == 100


@pytest.mark.parametrize(
    "surfaces",
    [
        ([(PkSurface((100, 100)), (10, 10)), (PkSurface((50, 50)), (20, 20))]),
        (
            [
                (PkSurface((100, 100)), (10, 20)),
                (PkSurface((50, 50)), (20, 30)),
                (PkSurface((25, 25)), (30, 30)),
            ]
        ),
    ],
)
def test_pksurface_blits(surface: PkSurface, surfaces: list[PkSurface]) -> None:
    """Test blitting surfaces onto another surface."""
    surface = PkSurface((100, 100))
    surface.blits(surfaces)


@pytest.mark.parametrize(
    "new_surface",
    [
        None,
        PkSurface((100, 100), depth=24),
    ],
)
def test_pksurface_convert(surface: PkSurface, new_surface: PkSurface) -> None:
    """Test converting the surface to a new format."""
    surface.convert(new_surface)


def test_pksurface_convert_alpha(surface: PkSurface) -> None:
    """Test converting the surface to a new format with per-pixel alpha."""
    surface.convert_alpha()


def test_pksurface_copy(surface: PkSurface) -> None:
    """Test copying the surface."""
    surface.fill(PkColor(255, 0, 0))
    copy = surface.copy()
    assert copy.get_at((0, 0)) == (255, 0, 0, 255)


@pytest.mark.parametrize(
    "color, rect, expected_color",
    [
        (PkColor(255, 0, 0), None, (255, 0, 0, 255)),
        (PkColor(0, 255, 0), (10, 10, 50, 50), (0, 255, 0, 255)),
    ],
)
def test_pksurface_fill(
    surface: PkSurface,
    color: PkColor,
    rect: tuple[int, int, int, int] | None,
    expected_color: tuple[int, int, int, int],
) -> None:
    """Test filling the surface with a color."""
    surface.fill(color, rect)
    if rect is None:
        assert surface.get_at((0, 0)) == color
    else:
        assert surface.get_at((rect[0], rect[1])) == color


@pytest.mark.parametrize(
    "alpha, expected_alpha",
    [
        (128, 128),
        (255, 255),
    ],
)
def test_pksurface_alpha(surface: PkSurface, alpha: int, expected_alpha: int) -> None:
    """Test setting and getting the alpha value of the surface."""
    surface.set_alpha(alpha)
    assert surface.get_alpha() == expected_alpha


@pytest.mark.parametrize(
    "color, expected_colorkey",
    [
        (PkColor(255, 0, 0), (255, 0, 0, 255)),
        (PkColor(0, 255, 0), (0, 255, 0, 255)),
        ((0, 255, 0), (0, 255, 0, 255)),
    ],
)
def test_pksurface_colorkey(
    surface: PkSurface, color: PkColor, expected_colorkey: tuple[int, int, int, int]
) -> None:
    """Test setting and getting the colorkey of the surface."""
    surface.set_colorkey(color)
    assert surface.get_colorkey() == expected_colorkey


@pytest.mark.parametrize(
    "dx, dy, expected_pos",
    [
        (10, 0, (10, 0)),
        (0, 10, (0, 10)),
        (10, 10, (10, 10)),
    ],
)
def test_pksurface_scroll(
    surface: PkSurface, dx: int, dy: int, expected_pos: tuple[int, int]
) -> None:
    """Test scrolling the surface."""
    surface.fill(PkColor(255, 0, 255), (0, 0, 5, 5))
    assert surface.get_at(expected_pos) == (0, 0, 0, 255)
    surface.scroll(dx, dy)
    assert surface.get_at(expected_pos) == (255, 0, 255, 255)


def test_pksurface_lock(surface: PkSurface) -> None:
    """Test locking the surface."""
    surface.lock()


def test_pksurface_unlock(surface: PkSurface) -> None:
    """Test unlocking the surface."""
    surface.unlock()


def test_pksurface_mustlock(surface: PkSurface) -> None:
    """Test getting the mustlock status of the surface."""
    assert not surface.mustlock()


def test_pksurface_get_locked(surface: PkSurface) -> None:
    """Test getting the locked status of the surface."""
    surface.lock()
    assert surface.get_locked()
    surface.unlock()
    assert not surface.get_locked()


def test_pksurface_get_locks(surface: PkSurface) -> None:
    """Test getting the locks on the surface."""
    surface.lock()
    assert surface.get_locks() == (surface.internal_surface,)
    surface.unlock()
    assert surface.get_locks() == ()


def test_pksurface_get_at(surface: PkSurface) -> None:
    """Test getting the color of a pixel on the surface."""
    assert surface.get_at((0, 0)) == (0, 0, 0, 255)


@pytest.mark.parametrize(
    "color, expected_color",
    [
        (PkColor(255, 0, 0), (255, 0, 0, 255)),
        ((0, 255, 0), (0, 255, 0, 255)),
    ],
)
def test_pksurface_set_at(
    surface: PkSurface,
    color: PkColor | ColorValue,
    expected_color: PkColor | ColorValue,
) -> None:
    """Test setting the color of a pixel on the surface."""
    surface.set_at((0, 0), color)
    assert surface.get_at((0, 0)) == expected_color


def test_pksurface_get_at_mapped(surface: PkSurface) -> None:
    """Test getting the color of a pixel on the surface with color mapping."""
    assert surface.get_at_mapped((0, 0)) == 0


def test_pksurface_get_palette(surface_8bit: PkSurface) -> None:
    """Test getting the palette of the surface."""
    assert PkColor(0, 0, 0) in surface_8bit.get_palette()
    assert PkColor(255, 255, 255) in surface_8bit.get_palette()


def test_pksurface_set_palette(surface_8bit: PkSurface) -> None:
    """Test setting the palette of the surface."""
    surface_8bit.set_palette([PkColor(255, 0, 0), PkColor(0, 255, 0)])
    assert PkColor(255, 0, 0) in surface_8bit.get_palette()
    assert PkColor(0, 255, 0) in surface_8bit.get_palette()


@pytest.mark.parametrize(
    "index, color",
    [
        (0, PkColor(255, 0, 0)),
        (1, (0, 255, 0)),
    ],
)
def test_pksurface_set_palette_at(
    surface_8bit: PkSurface, index: int, color: PkColor | ColorValue
) -> None:
    """Test setting the palette of the surface."""
    surface_8bit.set_palette_at(index, color)
    assert surface_8bit.get_palette()[index] == color


def test_pksurface_map_rgb(surface: PkSurface) -> None:
    """Test mapping an RGB color to a pixel value."""
    assert surface.map_rgb((0, 0, 0)) == 0


def test_pksurface_unmap_rgb(surface: PkSurface) -> None:
    """Test mapping a pixel value to an RGB color."""
    assert surface.unmap_rgb(0) == (0, 0, 0)


def test_pksurface_set_clip(surface: PkSurface) -> None:
    """Test setting the clipping rectangle of the surface."""
    surface.set_clip(PkRect((10, 10), (50, 50)))
    assert surface.get_clip() == (10, 10, 50, 50)


def test_pksurface_get_clip(surface: PkSurface) -> None:
    """Test getting the clipping rectangle of the surface."""
    assert surface.get_clip() == (0, 0, 100, 100)


def test_pksurface_subsurface(surface: PkSurface) -> None:
    """Test creating a subsurface from the surface."""
    subsurface = surface.subsurface(PkRect((10, 10), (50, 50)))
    assert subsurface.size == (50, 50)


def test_pksurface_get_parent(surface: PkSurface) -> None:
    """Test getting the parent surface of the surface."""
    assert surface.get_parent() == surface


def test_pksurface_get_abs_parent(surface: PkSurface) -> None:
    """Test getting the absolute parent surface of the surface."""
    assert surface.get_abs_parent() == surface


def test_pksurface_get_offset(surface: PkSurface) -> None:
    """Test getting the offset of the surface."""
    assert surface.get_offset() == (0, 0)


def test_pksurface_get_size(surface: PkSurface) -> None:
    """Test getting the size of the surface."""
    assert surface.get_size() == (100, 100)


def test_pksurface_get_width(surface: PkSurface) -> None:
    """Test getting the width of the surface."""
    assert surface.get_width() == 100


def test_pksurface_get_height(surface: PkSurface) -> None:
    """Test getting the height of the surface."""
    assert surface.get_height() == 100


def test_pksurface_get_rect(surface: PkSurface) -> None:
    """Test getting the rect of the surface."""
    assert surface.get_rect() == (0, 0, 100, 100)
    assert surface.get_rect() == PkRect((0, 0), (100, 100))


def test_pksurface_get_bitsize(surface: PkSurface) -> None:
    """Test getting the bitsize of the surface."""
    assert surface.get_bitsize() == 32


def test_pksurface_get_bytesize(surface: PkSurface) -> None:
    """Test getting the bytesize of the surface."""
    assert surface.get_bytesize() == 4


def test_pksurface_get_flags(surface: PkSurface) -> None:
    """Test getting the flags of the surface."""
    assert surface.get_flags() == 0


def test_pksurface_get_masks(surface: PkSurface) -> None:
    """Test getting the masks of the surface."""
    assert surface.get_masks() == (16711680, 65280, 255, 0)


def test_pksurface_set_masks(surface: PkSurface) -> None:
    """Test setting the masks of the surface."""
    with pytest.raises(DeprecationWarning):
        surface.set_masks((255, 65280, 16711680, 0))


def test_pksurface_get_shifts(surface: PkSurface) -> None:
    """Test getting the shifts of the surface."""
    assert surface.get_shifts() == (16, 8, 0, 0)


def test_pksurface_set_shifts(surface: PkSurface) -> None:
    """Test setting the shifts of the surface."""
    with pytest.raises(DeprecationWarning):
        surface.set_shifts((0, 8, 16, 24))


def test_pksurface_get_losses(surface: PkSurface) -> None:
    """Test getting the losses of the surface."""
    assert surface.get_losses() == (0, 0, 0, 8)


def test_pksurface_get_bounding_rect(surface: PkSurface) -> None:
    """Test getting the bounding rect of the surface."""
    assert surface.get_bounding_rect() == (0, 0, 100, 100)


def test_pksurface_get_view(surface: PkSurface) -> None:
    """Test getting the view of the surface."""
    assert surface.get_view()  # check if does not raise an exception


def test_pksurface_get_buffer(surface: PkSurface) -> None:
    """Test getting the buffer of the surface."""
    assert surface.get_buffer()  # check if does not raise an exception


def test_pksurface__pixels_address(surface: PkSurface) -> None:
    """Test getting the address of the surface's pixel buffer."""
    assert surface._pixels_address  # check if does not raise an exception


def test_pksurface_premul_alpha(surface: PkSurface) -> None:
    """Test premultiplying the alpha of the surface."""
    surface = surface.convert_alpha()
    surface.fill(PkColor(255, 0, 0, 128))
    surface = surface.premul_alpha()
    assert surface.get_at((0, 0)) == (128, 0, 0, 128)


def test_pksurface_scale(surface: PkSurface) -> None:
    """Test scaling the surface."""
    surface.fill(PkColor(255, 0, 0))
    surface = surface.scale((50, 50))
    assert surface.size == (50, 50)


@pytest.mark.parametrize(
    "text, rect, wrap, text_align, vertical_align, tab_size, font_size, color, bg_color, antialias",
    [
        ("Hello, World!", (10, 10, 50, 50), False, "left", "top", 4, 12, PkColor(255, 0, 0), PkColor(0, 255, 0), True),  # fmt: skip
        ("Hello, World!", (10, 10, 50, 50), True, "center", "middle", 4, 12, (0, 255, 0), PkColor(255, 0, 0), False),  # fmt: skip
        ("Hello, World!", (10, 10, 50, 50), False, "right", "bottom", 4, 12, PkColor(0, 0, 255), (255, 255, 0), True),  # fmt: skip
        ("Hello, World!", (10, 10, 50, 50), True, "left", "top", 4, 16, PkColor(255, 255, 0), PkColor(0, 0, 255), False),  # fmt: skip
        ("Hello, World!", (10, 10, 50, 50), False, "center", "middle", 4, 16, (0, 255, 255), PkColor(255, 0, 255), True),  # fmt: skip
        ("Hello, World!", (10, 10, 50, 50), True, "right", "bottom", 4, 16, PkColor(255, 0, 255), PkColor(255, 255, 255), False),  # fmt: skip
    ],
)
def test_pksurface_blit_text(
    surface: PkSurface,
    text: str,
    rect: PkRect | RectValue,
    wrap: bool,
    text_align: str,
    vertical_align: str,
    tab_size: int,
    font_size: int,
    color: PkColor | ColorValue,
    bg_color: PkColor | ColorValue,
    antialias: bool,
) -> None:
    """Test blitting text onto the surface."""
    surface.blit_text(
        text=text,
        rect=rect,
        wrap=wrap,
        text_align=text_align,
        vertical_align=vertical_align,
        tab_size=tab_size,
        font=PkFont(None, font_size),
        color=color,
        bg_color=bg_color,
        antialias=antialias,
    )


@mock.patch("typing.TYPE_CHECKING", True)
def test_type_checking_imports() -> None:
    """Test importing PkSurface with TYPE_CHECKING."""
    from puffkit import surface
    import importlib

    importlib.reload(surface)

    assert PkSurface
