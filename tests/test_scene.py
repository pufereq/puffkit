from unittest import mock

import pygame as pg
import pytest

pg.font.init()
from puffkit.scene import PkScene
from puffkit.surface import PkSurface


@pytest.fixture
def scene():
    size = (800, 600)
    pos = (0, 0)
    pg.init()
    pg.font.init()
    return PkScene(size, pos)


def test_pkscene_initialization(scene: PkScene):
    assert scene.size == (800, 600)
    assert scene.pos == (0, 0)
    assert isinstance(scene.surface, PkSurface)


def test_pkscene_input(scene: PkScene):
    events = [pg.event.Event(pg.KEYDOWN, key=pg.K_a)]
    keys = {pg.K_a: True}
    mouse_pos = (100, 100)
    mouse_buttons = (False, False, False)
    scene.input(
        events=events, keys=keys, mouse_pos=mouse_pos, mouse_buttons=mouse_buttons
    )
    # check if runs without error


def test_pkscene_update(scene: PkScene):
    scene.update(0.016)  # Assuming 60 FPS, delta would be around 0.016 seconds
    # check if runs without error


def test_pkscene_render(scene: PkScene):
    with mock.patch.object(scene, "draw") as mock_draw:
        screen = mock.Mock(spec=pg.Surface)
        scene.render(screen)
        mock_draw.assert_called_once_with(screen)


def test_pkscene_draw(scene: PkScene):
    screen = mock.Mock(spec=pg.Surface)
    scene.draw(screen)
    screen.blit.assert_called_once_with(scene.surface, scene.surface.pos)
