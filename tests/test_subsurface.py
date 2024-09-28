import pytest

from puffkit.subsurface import PkSubSurface
from puffkit.surface import PkSurface


@pytest.fixture
def surface():
    """Fixture for creating a PkSurface."""
    return PkSurface((100, 100), (0, 0))


@pytest.mark.parametrize(
    "pos, size",
    [
        ((0, 0), (10, 10)),
        ((10, 10), (20, 20)),
        ((0, 0), (0, 0)),
        ((0, 0), (100, 100)),
    ],
)
def test_pksubsurface_initialization(
    surface: PkSurface, pos: tuple[int, int], size: tuple[int, int]
):
    """Test the initialization of PkSubSurface."""
    subsurface = PkSubSurface(parent=surface, pos=pos, size=size)
    assert subsurface.parent == surface
    # assert subsurface.surface == surface.internal_surface.subsurface(pos, size)


def test_pksubsurface_get_parent(surface: PkSurface):
    """Test the get_parent method."""
    subsurface = PkSubSurface(parent=surface, pos=(0, 0))
    assert subsurface.get_parent() == surface


def test_pksubsurface_get_abs_parent(surface: PkSurface):
    """Test the get_abs_parent method."""
    subsurface = PkSubSurface(parent=surface, pos=(0, 0))
    assert subsurface.get_abs_parent() == surface
