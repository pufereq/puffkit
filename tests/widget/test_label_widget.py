import pygame
import pytest
from unittest.mock import MagicMock, Mock
from puffkit import ColorValue, PkApp, PkColor, PkContainer, PkRect, PkSurface
from puffkit.font import PkFont
from puffkit.geometry import RectValue
from puffkit.widget.label_widget import PkLabelWidget


@pytest.fixture
def container() -> PkContainer:
    pygame.init()
    app = MagicMock(spec=PkApp)
    app.fonts = {"default": PkFont(None, 12)}

    parent_surface = MagicMock(spec=PkSurface)
    parent_surface.get_width.return_value = 100
    parent_surface.get_height.return_value = 100
    container = PkContainer(app, parent_surface, "test_container", (0, 0, 100, 100))
    return container


@pytest.fixture
def label_widget(container: PkContainer) -> PkLabelWidget:
    return PkLabelWidget(
        container=container,
        text="Test Label",
        rect=PkRect(0, 0, 100, 30),
        font_id="default",
        text_color=PkColor(0, 0, 0),
        background_color=PkColor(255, 255, 255),
        text_wrap=True,
        text_align="left",
    )


@pytest.mark.parametrize(
    "text, rect, font_id, text_color, background_color, text_wrap, text_align",
    [
        (
            "Test Label",
            PkRect(0, 0, 100, 30),
            "default",
            PkColor(0, 0, 0),
            PkColor(255, 255, 255),
            True,
            "left",
        ),
        (
            "Another Label",
            PkRect(10, 10, 50, 20),
            "default",
            (255, 0, 0),
            (0, 0, 0),
            False,
            "center",
        ),
        ("", PkRect(0, 0, 100, 30), "default", PkColor(0, 0, 0), None, True, "left"),
    ],
)
def test_initialization(
    container: PkContainer,
    text: str,
    rect: PkRect | RectValue,
    font_id: str,
    text_color: PkColor | ColorValue,
    background_color: PkColor | ColorValue | None,
    text_wrap: bool,
    text_align: str,
):
    label_widget = PkLabelWidget(
        container,
        text,
        rect,
        font_id=font_id,
        text_color=text_color,
        background_color=background_color,
        text_wrap=text_wrap,
        text_align=text_align,
    )
    if background_color is None:
        background_color = PkColor(0, 0, 0, 0)

    assert label_widget.get_text() == text
    assert label_widget.font_id == font_id
    assert label_widget.text_color == text_color
    assert label_widget.font == container.app.fonts[font_id]
    assert label_widget.background_color == background_color
    assert label_widget.text_wrap == text_wrap
    assert label_widget.text_align == text_align


def test_set_text(label_widget: PkLabelWidget):
    label_widget.set_text("New Text")
    assert label_widget.get_text() == "New Text"
    assert label_widget.needs_redraw is True


def test_find_font_existing(container: Mock):
    container.app.fonts["existing"] = Mock()
    label_widget = PkLabelWidget(
        container=container,
        text="Test Label",
        rect=PkRect(0, 0, 100, 30),
        font_id="existing",
    )
    assert label_widget.font == container.app.fonts["existing"]


def test_find_font_non_existing(container: Mock):
    label_widget = PkLabelWidget(
        container=container,
        text="Test Label",
        rect=PkRect(0, 0, 100, 30),
        font_id="non_existing",
    )
    assert label_widget.font.path is None


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Short Text", "Short Text"),
        ("Another Text", "Another Text"),
        ("", ""),
    ],
)
def test_set_text_various(label_widget: PkLabelWidget, text, expected):
    label_widget.set_text(text)
    assert label_widget.get_text() == expected
    assert label_widget.needs_redraw is True


def test_on_render(label_widget: PkLabelWidget):
    label_widget.on_render()
    assert label_widget.needs_redraw is False


def test_on_render_needs_redraw(label_widget: PkLabelWidget):
    label_widget.needs_redraw = False
    label_widget.on_render()
    assert label_widget.needs_redraw is False
