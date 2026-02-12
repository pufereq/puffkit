# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Final, override

from puffkit.color import ColorValue, PkBasicPalette, PkColor
from puffkit.container import PkContainer
from puffkit.event.event import PkEvent
from puffkit.geometry import PkSize
from puffkit.image import PkImage
from puffkit.surface import PkSurface
from puffkit.widget import PkWidget

if TYPE_CHECKING:  # pragma: no cover
    from puffkit.geometry import PkRect, RectValue


class PkImageWidget(PkWidget):
    """A widget that displays an image with various resizing options."""

    RESIZE_MODES: set[str | None] = {"stretch", "fit", "fill", "tile", None}

    def __init__(
        self,
        id_: str,
        container: PkContainer,
        image: PkImage,
        rect: PkRect | RectValue,
        resize_mode: str | None = "stretch",
        *,
        click_hook: Callable[[PkImageWidget, PkEvent], None] | None = None,
        hover_hook: Callable[[PkImageWidget, PkEvent], None] | None = None,
        disabled: bool = False,
        background_color: PkColor | ColorValue = PkBasicPalette.TRANSPARENT,
        border_radius: int = 0,
    ) -> None:
        """Initialize a PkImageWidget.
        Args:
            id_ (str): The ID of the image widget.
            container (PkContainer): The container that the widget belongs to.
            image (PkImage): The image to display in the widget.
            rect (PkRect | RectValue): The rectangle that the widget occupies.
                Relative to the container.
            resize_mode (str | None, optional): The resize mode for the image.
                Options are "stretch", "fit", "fill", "tile", and None.
                Defaults to "stretch".
            click_hook (Callable[[PkImageWidget, PkEvent], None] | None, optional):
                The action to perform when the widget is clicked. Defaults to None.
            hover_hook (Callable[[PkImageWidget, PkEvent], None] | None, optional):
                The action to perform when the widget is hovered. Defaults to None.
            disabled (bool, optional): Whether the widget is disabled. Defaults to False.
            background_color (PkColor | ColorValue, optional): The background color
                of the widget. Defaults to transparent.
            border_radius (int, optional): The border radius of the widget. Defaults to 0.
        """
        if resize_mode not in self.RESIZE_MODES:
            raise ValueError(
                f"Invalid resize mode: {resize_mode}. "
                + f"Valid options are: {self.RESIZE_MODES}",
            )
        super().__init__(id_, container, rect, focusable=False)

        self._image: PkImage = image

        self.click_hook: Callable[[PkImageWidget, PkEvent], None] | None = (
            click_hook
        )
        self.hover_hook: Callable[[PkImageWidget, PkEvent], None] | None = (
            hover_hook
        )
        self._disabled: bool = disabled

        self.background_color: PkColor = PkColor.from_value(background_color)
        self.border_radius: int = border_radius
        self.resize_mode: str | None = resize_mode

        self.resized_image: PkImage = self._resize_image(self.resize_mode)

    @property
    def image(self) -> PkImage:  # pragma: no cover
        """The image displayed in the widget."""
        return self._image

    @image.setter
    def image(self, new_image: PkImage) -> None:
        """Set a new image for the widget and update the resized image."""
        self._image = new_image
        self.resized_image = self._resize_image(self.resize_mode)

    @override
    def __str__(self) -> str:  # pragma: no cover
        return (
            f"PkImageWidget(id_={self.id}, rect={self.rect}, "
            f"image={self.image}, resize_mode={self.resize_mode})"
        )

    @override
    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"PkImageWidget(id_={self.id}, rect={self.rect}, "
            f"image={self.image}, resize_mode={self.resize_mode})"
        )

    def _resize_image(self, resize_mode: str | None = None) -> PkImage:
        """Resize the image according to the resize mode.

        Args:
            resize_mode (str | None, optional): The resize mode to use.
                If None, use the widget's resize mode. Defaults to None.

        Returns:
            PkImage: The resized image.
        """
        match resize_mode:
            case "stretch":
                resized_surface = self.image.image.resize(
                    self.rect.size,
                )
                return PkImage(self.image.id, resized_surface)
            case "fit":
                # maintain aspect ratio
                image_aspect_ratio = self.image.width / self.image.height
                rect_aspect_ratio = self.rect.width / self.rect.height
                if image_aspect_ratio > rect_aspect_ratio:
                    # fit to width
                    new_width = self.rect.width
                    new_height = new_width / image_aspect_ratio
                else:
                    # fit to height
                    new_height = self.rect.height
                    new_width = new_height * image_aspect_ratio
                resized_surface = self.image.image.resize(
                    (int(new_width), int(new_height)),
                )
                return PkImage(self.image.id, resized_surface)
            case "fill":
                # maintain aspect ratio, cover entire rect
                image_aspect_ratio = self.image.width / self.image.height
                rect_aspect_ratio = self.rect.width / self.rect.height
                if image_aspect_ratio < rect_aspect_ratio:
                    # cover width
                    new_width = self.rect.width
                    new_height = new_width / image_aspect_ratio
                else:
                    # cover height
                    new_height = self.rect.height
                    new_width = new_height * image_aspect_ratio
                resized_surface = self.image.image.resize(
                    (int(new_width), int(new_height)),
                )
                return PkImage(self.image.id, resized_surface)
            case "tile":
                surface: PkSurface = PkSurface(
                    self.rect.size, transparent=True
                )
                for x in range(0, int(self.rect.width), int(self.image.width)):
                    for y in range(
                        0, int(self.rect.height), int(self.image.height)
                    ):
                        surface.blit(self.image.image, (x, y))
                return PkImage(self.image.id, surface)
            case None:
                return self.image
            case _:
                raise ValueError(
                    f"Invalid resize mode: {resize_mode}. "
                    + f"Valid options are: {self.RESIZE_MODES}",
                )

    @override
    def on_click(self, event: PkEvent) -> None:
        if callable(self.click_hook):
            self.click_hook(self, event)

    @override
    def on_hover(self, event: PkEvent) -> None:
        if callable(self.hover_hook):
            self.hover_hook(self, event)

    @override
    def on_render(self) -> None:
        # fill the surface with a background color
        self.surface.fill(self.background_color)

        # draw the image at the center of the widget
        image_x = (self.rect.width - self.resized_image.width) // 2
        image_y = (self.rect.height - self.resized_image.height) // 2
        self.surface.blit(self.resized_image.image, (image_x, image_y))
