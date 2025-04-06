import math

import pygame
import pytest

from puffkit.color.color import ColorValue, PkColor


@pytest.mark.parametrize(
    "hex_color, expected",
    [
        ("#000", (0, 0, 0, 255)),
        ("#fff", (255, 255, 255, 255)),
        ("#123456", (18, 52, 86, 255)),
        ("#12345678", (18, 52, 86, 120)),
        ("#abc", (170, 187, 204, 255)),
    ],
)
def test_pkcolor_hex_to_rgba(hex_color: str, expected: tuple[int, int, int, int]):
    assert PkColor.hex_to_rgba(hex_color) == expected


@pytest.mark.parametrize(
    "c, m, y, expected",
    [
        (0, 0, 0, (255, 255, 255, 255)),
        (255, 255, 255, (0, 0, 0, 255)),
        (127, 127, 127, (128, 128, 128, 255)),
    ],
)
def test_pkcolor_cmy_to_rgba(
    c: int, m: int, y: int, expected: tuple[int, int, int, int]
):
    assert PkColor.cmy_to_rgba(c, m, y) == expected


@pytest.mark.parametrize(
    "h, s, v, a, expected",
    [
        (0, 1, 1, 1, (255, 0, 0, 255)),
        (120, 1, 1, 1, (0, 255, 0, 255)),
        (240, 1, 1, 1, (0, 0, 255, 255)),
        (360, 1, 1, 1, (255, 0, 0, 255)),
    ],
)
def test_pkcolor_hsva_to_rgba(
    h: int, s: int, v: int, a: int, expected: tuple[int, int, int, int]
):
    assert PkColor.hsva_to_rgba(h, s, v, a) == expected


@pytest.mark.parametrize(
    "h, s, l, a, expected",
    [
        (0, 1, 0.5, 1, (255, 0, 0, 255)),
        (120, 1, 0.5, 1, (0, 255, 0, 255)),
        (240, 1, 0.5, 1, (0, 0, 255, 255)),
        (360, 1, 0.5, 1, (255, 0, 0, 255)),
    ],
)
def test_pkcolor_hsla_to_rgba(
    h: int, s: float, l: float, a: int, expected: tuple[int, int, int, int]
):
    assert PkColor.hsla_to_rgba(h, s, l, a) == expected


@pytest.mark.parametrize(
    "pygame_color, expected",
    [
        (pygame.Color(0, 0, 0, 255), (0, 0, 0, 255)),
        (pygame.Color(255, 255, 255, 255), (255, 255, 255, 255)),
        (pygame.Color(18, 52, 86, 255), (18, 52, 86, 255)),
        (pygame.Color(18, 52, 86, 120), (18, 52, 86, 120)),
        (pygame.Color(170, 187, 204, 255), (170, 187, 204, 255)),
    ],
)
def test_pkcolor_from_pygame(
    pygame_color: tuple[int, int, int, int], expected: tuple[int, int, int, int]
):
    assert PkColor.from_pygame(pygame_color) == expected


@pytest.mark.parametrize(
    "hex_color, expected",
    [
        ("#000", PkColor(0, 0, 0, 255)),
        ("#fff", PkColor(255, 255, 255, 255)),
        ("#123456", PkColor(18, 52, 86, 255)),
        ("#12345678", PkColor(18, 52, 86, 120)),
        ("#abc", PkColor(170, 187, 204, 255)),
    ],
)
def test_pkcolor_from_hex(hex_color: str, expected: tuple[int, int, int, int]):
    assert PkColor.from_hex(hex_color) == expected


@pytest.mark.parametrize(
    "c, m, y, expected",
    [
        (0, 0, 0, PkColor(255, 255, 255, 255)),
        (255, 255, 255, PkColor(0, 0, 0, 255)),
        (127, 127, 127, PkColor(128, 128, 128, 255)),
    ],
)
def test_pkcolor_from_cmy(c: int, m: int, y: int, expected: tuple[int, int, int, int]):
    assert PkColor.from_cmy(c, m, y) == expected


@pytest.mark.parametrize(
    "h, s, v, a, expected",
    [
        (0, 1.0, 1.0, 1.0, (255, 0, 0, 255)),  # Red
        (120, 1.0, 1.0, 1.0, (0, 255, 0, 255)),  # Green
        (240, 1.0, 1.0, 1.0, (0, 0, 255, 255)),  # Blue
        (60, 1.0, 1.0, 0.5, (255, 255, 0, 127)),  # Yellow (50% transparent)
        (180, 0.5, 0.5, 1.0, (63, 127, 127, 255)),  # Cyan (reduced saturation)
        (300, 0.75, 0.75, 0.75, (191, 47, 191, 191)),  # Magenta (semi-transparent)
        (30, 0.8, 0.9, 0.9, (229, 137, 45, 229)),  # Orange
        (0, 0.0, 0.5, 1.0, (127, 127, 127, 255)),  # Gray (50% brightness)
        (180, 1.0, 0.0, 1.0, (0, 0, 0, 255)),  # Black (no brightness)
        (360, 0.5, 1.0, 0.0, (255, 127, 127, 0)),  # Light Red (fully transparent)
    ],
)
def test_pkcolor_from_hsva(
    h: int, s: float, v: float, a: float, expected: tuple[int, int, int, int]
):
    assert PkColor.from_hsva(h, s, v, a) == expected


@pytest.mark.parametrize(
    "h, s, l, a, expected",
    [
        (0, 1, 0.5, 1, PkColor(255, 0, 0, 255)),
        (120, 1, 0.5, 1, PkColor(0, 255, 0, 255)),
        (240, 1, 0.5, 1, PkColor(0, 0, 255, 255)),
        (360, 1, 0.5, 1, PkColor(255, 0, 0, 255)),
    ],
)
def test_pkcolor_from_hsla(
    h: int, s: float, l: float, a: float, expected: tuple[int, int, int, int]
):
    assert PkColor.from_hsla(h, s, l, a) == expected


@pytest.mark.parametrize(
    "color_value, expected",
    [
        ((0, 0, 0, 255), PkColor(0, 0, 0, 255)),
        ((255, 255, 255, 255), PkColor(255, 255, 255, 255)),
        ((18, 52, 86, 255), PkColor(18, 52, 86, 255)),
        ((18, 52, 86, 120), PkColor(18, 52, 86, 120)),
        ((170, 187, 204), PkColor(170, 187, 204, 255)),
        ("#000", PkColor(0, 0, 0, 255)),
        ("#fff", PkColor(255, 255, 255, 255)),
        (PkColor(18, 52, 86, 255), PkColor(18, 52, 86, 255)),
    ],
)
def test_pkcolor_from_value(color_value: ColorValue, expected: PkColor):
    assert PkColor.from_value(color_value) == expected


@pytest.mark.parametrize(
    "invalid_value",
    [
        (256, 0, 0, 255),  # Invalid red value
        (0, -1, 0, 255),  # Invalid green value
        (0, 0, 300, 255),  # Invalid blue value
        (0, 0, 0, -1),  # Invalid alpha value
        (0.5, 0, 0, 255),  # Invalid red value type
        (0, 0.5, 0, 255),  # Invalid green value type
        (0, 0, 0.5, 255),  # Invalid blue value type
        (0, 0, 0, 0.5),  # Invalid alpha value type
        (0, "a", 0, 255),  # Invalid green value type
        ("xyz",),  # Invalid hex color
        None,  # None value
        (0, 0, 0, 255, 255),  # Extra value
        (0, 0, 0, 255, "extra"),  # Extra value with string
        (0, 0),  # Too few values
    ],
)
def test_pkcolor_from_value_invalid(invalid_value: ColorValue):
    with pytest.raises((ValueError, TypeError)):
        PkColor.from_value(invalid_value)


@pytest.mark.parametrize(
    "color, expected",
    [
        (PkColor(0, 0, 0, 255), "#000000"),
        (PkColor(255, 255, 255, 255), "#ffffff"),
        (PkColor(18, 52, 86, 255), "#123456"),
    ],
)
def test_pkcolor_hex(color: PkColor, expected: tuple[int, int, int, int]):
    assert color.hex == expected


@pytest.mark.parametrize(
    "color, expected",
    [
        (PkColor(0, 0, 0, 255), "#000000ff"),
        (PkColor(255, 255, 255, 255), "#ffffffff"),
        (PkColor(18, 52, 86, 120), "#12345678"),
    ],
)
def test_pkcolor_hexa(color: PkColor, expected: tuple[int, int, int, int]):
    assert color.hexa == expected


@pytest.mark.parametrize(
    "color, expected",
    [
        (PkColor(0, 0, 0, 255), (0, 0, 0, 255)),
        (PkColor(255, 255, 255, 255), (255, 255, 255, 255)),
        (PkColor(18, 52, 86, 120), (18, 52, 86, 120)),
    ],
)
def test_pkcolor_rgba(color: PkColor, expected: tuple[int, int, int, int]):
    assert color.rgba == expected


@pytest.mark.parametrize(
    "color, expected",
    [
        (PkColor(0, 0, 0, 255), (0, 0, 0)),
        (PkColor(255, 255, 255, 255), (255, 255, 255)),
        (PkColor(18, 52, 86, 120), (18, 52, 86)),
    ],
)
def test_pkcolor_rgb(color: PkColor, expected: PkColor):
    assert color.rgb == expected


@pytest.mark.parametrize(
    "color, expected",
    [
        (PkColor(0, 0, 0, 255), (255, 255, 255)),
        (PkColor(255, 255, 255, 255), (0, 0, 0)),
        (PkColor(18, 52, 86, 120), (237, 203, 169)),
    ],
)
def test_pkcolor_cmy(color: PkColor, expected: PkColor):
    assert color.cmy == expected


@pytest.mark.parametrize(
    "color, expected",
    [
        (PkColor(255, 0, 0, 255), (0, 1, 1, 1)),
        (PkColor(0, 255, 0, 255), (120, 1, 1, 1)),
        (PkColor(0, 0, 255, 255), (240, 1, 1, 1)),
    ],
)
def test_pkcolor_hsva(color: PkColor, expected: PkColor):
    assert color.hsva == expected


@pytest.mark.parametrize(
    "color, expected",
    [
        (PkColor(255, 0, 0, 255), (0, 1, 0.5, 1)),
        (PkColor(0, 255, 0, 255), (120, 1, 0.5, 1)),
        (PkColor(0, 0, 255, 255), (240, 1, 0.5, 1)),
    ],
)
def test_pkcolor_hsla(color: PkColor, expected: PkColor):
    assert color.hsla == expected


@pytest.mark.parametrize(
    "color, other, t, expected",
    [
        (
            PkColor(0, 0, 0, 255),
            PkColor(255, 255, 255, 255),
            0.5,
            PkColor(127, 127, 127, 255),
        ),
        (
            PkColor(255, 0, 0, 255),
            PkColor(0, 255, 0, 255),
            0.5,
            PkColor(127, 127, 0, 255),
        ),
    ],
)
def test_pkcolor_lerp(color: PkColor, other: PkColor, t: float, expected: PkColor):
    assert color.lerp(other, t) == expected


@pytest.mark.parametrize(
    "color, expected",
    [
        (PkColor(255, 0, 0, 128), PkColor(128, 0, 0, 128)),
        (PkColor(0, 255, 0, 128), PkColor(0, 128, 0, 128)),
    ],
)
def test_pkcolor_premul_alpha(color: PkColor, expected: PkColor):
    assert color.premul_alpha() == expected


@pytest.mark.parametrize(
    "color, r, g, b, a, expected",
    [
        (PkColor(255, 0, 0, 255), 0, 255, 0, 255, PkColor(0, 255, 0, 255)),
        (PkColor(0, 0, 255, 255), 255, 255, 0, 255, PkColor(255, 255, 0, 255)),
    ],
)
def test_pkcolor_update(
    color: PkColor, r: int, g: int, b: int, a: int, expected: PkColor
):
    color.update(r, g, b, a)
    assert color == expected


@pytest.mark.parametrize(
    "color, other, expected",
    [
        (
            PkColor(255, 0, 0, 255),
            PkColor(0, 255, 0, 255),
            PkColor(255, 255, 0, 255),
        ),
        (
            PkColor(0, 0, 255, 255),
            PkColor(255, 255, 0, 255),
            PkColor(255, 255, 255, 255),
        ),
    ],
)
def test_pkcolor_add(color: PkColor, other: PkColor, expected: PkColor):
    assert color + other == expected


@pytest.mark.parametrize(
    "color, other, expected",
    [
        (PkColor(255, 0, 0, 255), PkColor(0, 255, 0, 255), PkColor(255, 0, 0, 255)),
        (PkColor(0, 0, 255, 255), PkColor(255, 255, 0, 255), PkColor(0, 0, 255, 255)),
    ],
)
def test_pkcolor_sub(color: PkColor, other: PkColor, expected: PkColor):
    assert color - other == expected


@pytest.mark.parametrize(
    "color, other, expected",
    [
        (PkColor(255, 0, 0, 255), PkColor(0, 255, 0, 255), PkColor(0, 0, 0, 255)),
        (PkColor(0, 0, 255, 255), PkColor(255, 255, 0, 255), PkColor(0, 0, 0, 255)),
    ],
)
def test_pkcolor_mul(color: PkColor, other: PkColor, expected: PkColor):
    assert color * other == expected


@pytest.mark.parametrize(
    "invalid_cmy",
    [
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
        (256, 0, 0),
        (0, 256, 0),
        (0, 0, 256),
    ],
)
def test_pkcolor_invalid_cmy(invalid_cmy: tuple[int, int, int]):
    with pytest.raises(ValueError):
        PkColor.from_cmy(*invalid_cmy)


@pytest.mark.parametrize(
    "invalid_hex",
    [
        "#",  # only hash
        "#0",  # invalid length
        "#01",  # invalid length
        "#0123",  # invalid length
        "#01234",  # invalid length
        "#0123456",  # invalid length
        "#loremips",  # invalid characters
        "000",  # no hash
    ],
)
def test_pkcolor_invalid_hex(invalid_hex: str):
    with pytest.raises(ValueError):
        PkColor.from_hex(invalid_hex)


@pytest.mark.parametrize(
    "gamma_value_to_correct, expected",
    [
        (0.003, 12.92 * 0.003),  # Less than threshold
        (0.0031308, 12.92 * 0.0031308),  # At threshold
        (0.005, 1.055 * (0.005 ** (1 / 2.4)) - 0.055),  # Greater than threshold
        (0, 0),  # Zero value
        (1.0, 1.0),  # Close to 1.0
    ],
)
def test_pkcolor_correct_gamma(gamma_value_to_correct: float, expected: float):
    assert math.isclose(PkColor.correct_gamma(gamma_value_to_correct), expected)


@pytest.mark.parametrize(
    "pk_color, expected",
    [
        (PkColor(0, 0, 0, 255), 0),
        (PkColor(255, 255, 255, 255), 255),
        (PkColor(18, 52, 86, 255), 46),
        (PkColor(170, 187, 204, 255), 184),
    ],
)
def test_pkcolor_grayscale(pk_color: PkColor, expected: int):
    assert pk_color.grayscale() == expected


def test_pkcolor_str():
    assert str(PkColor(0, 0, 0, 255)) == "PkColor(0, 0, 0, 255)"


def test_pkcolor_repr():
    assert repr(PkColor(0, 0, 0, 255)) == "PkColor(0, 0, 0, 255)"
