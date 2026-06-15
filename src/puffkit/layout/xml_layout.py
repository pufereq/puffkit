# -*- coding: utf-8 -*-
"""XML-based layout loader for puffkit."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
import re
import xml.etree.ElementTree as ET
from typing import Any, Callable

from puffkit.container import PkContainer
from puffkit.image import PkImage
from puffkit.object import PkObject
from puffkit.scene import PkScene
from puffkit.widget import (
    PkButtonWidget,
    PkImageWidget,
    PkLabelWidget,
    PkTextInputWidget,
    PkWidget,
)


_BINDING_PATTERN = re.compile(
    r"^\{\s*(?P<kind>Binding|Resource)\s+(?P<value>.+?)\s*\}$"
)
_CAMEL_TO_SNAKE = re.compile(r"([a-z0-9])([A-Z])")


@dataclass(frozen=True)
class _WidgetSpec:
    """Definition of a widget type and its constructor requirements."""

    class_ref: type[PkWidget]
    required_attrs: set[str]
    arg_parsers: dict[str, Callable[[Any], Any]]
    event_attr_map: dict[str, str]


class PkLayout(PkObject):
    """Represents a parsed layout with a root container."""

    def __init__(
        self,
        root_container: PkContainer,
        containers: dict[str, PkContainer],
        widgets: dict[str, PkWidget],
    ) -> None:
        """Initialize the layout.

        Args:
            root_container (PkContainer): Root layout container.
            containers (dict[str, PkContainer]): Container registry by ID.
            widgets (dict[str, PkWidget]): Widget registry by ID.
        """
        super().__init__()
        self.root_container = root_container
        self.containers = containers
        self.widgets = widgets

    def get_widget(self, widget_id: str) -> PkWidget:
        """Get a widget by its ID.

        Args:
            widget_id (str): Widget identifier.

        Returns:
            PkWidget: The requested widget.
        """
        if widget_id not in self.widgets:
            raise ValueError(f"Widget with ID '{widget_id}' not found.")
        return self.widgets[widget_id]

    def get_container(self, container_id: str) -> PkContainer:
        """Get a container by its ID.

        Args:
            container_id (str): Container identifier.

        Returns:
            PkContainer: The requested container.
        """
        if container_id not in self.containers:
            raise ValueError(f"Container with ID '{container_id}' not found.")
        return self.containers[container_id]

    def update(self, delta: float) -> None:
        """Update the layout widgets.

        Args:
            delta (float): Time since last update in seconds.
        """
        self.root_container.input(
            self._input["events"],
            self._input["keys"],
            self._input["mouse_pos"],
            self._input["mouse_buttons"],
        )
        self.root_container.update(delta)

    def render(self) -> None:
        """Render the layout to its parent surface."""
        self.root_container.render()


class PkXmlLayoutLoader:
    """Load layouts from XML similar to XAML."""

    def __init__(
        self,
        *,
        resources: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the loader.

        Args:
            resources (dict[str, Any] | None): Default resources dictionary.
        """
        self._default_resources: dict[str, Any] = resources or {}

    def load_from_file(
        self,
        scene: PkScene,
        file_path: str,
        *,
        view_model: Any | None = None,
        resources_path: str | None = None,
    ) -> PkLayout:
        """Load a layout from a file path.

        Args:
            scene (PkScene): Target scene to attach the layout.
            file_path (str): Path to the XML layout file.
            view_model (Any | None): View model used for bindings.
            resources_path (str | None): Optional resources file path.

        Returns:
            PkLayout: Parsed layout.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            xml_text = file.read()

        base_path = os.path.dirname(os.path.abspath(file_path))
        return self.load_from_string(
            scene,
            xml_text,
            view_model=view_model,
            resources_path=resources_path,
            base_path=base_path,
        )

    def load_from_string(
        self,
        scene: PkScene,
        xml_text: str,
        *,
        view_model: Any | None = None,
        resources_path: str | None = None,
        base_path: str | None = None,
    ) -> PkLayout:
        """Load a layout from an XML string.

        Args:
            scene (PkScene): Target scene to attach the layout.
            xml_text (str): XML layout string.
            view_model (Any | None): View model used for bindings.
            resources_path (str | None): Optional resources file path.
            base_path (str | None): Base path for relative assets.

        Returns:
            PkLayout: Parsed layout.
        """
        root = ET.fromstring(xml_text)
        layout_tag = _strip_namespace(root.tag)
        if layout_tag.lower() != "layout":
            raise ValueError("Layout XML root element must be <Layout>.")

        resources = dict(self._default_resources)

        root_attrs = _normalize_attributes(root.attrib)
        layout_resources = root_attrs.get("resources")
        if resources_path:
            resources.update(self._load_resources(resources_path, base_path))
        elif layout_resources:
            resources.update(self._load_resources(layout_resources, base_path))

        layout_id = root_attrs.get("id", "layout_root")
        rect = _parse_rect(
            root_attrs,
            default_rect=(0, 0, scene.size.width, scene.size.height),
        )

        root_container = PkContainer(
            scene.app,
            scene.surface,
            layout_id,
            rect,
            draw_outline=_parse_bool(root_attrs.get("draw_outline", "false")),
        )

        containers: dict[str, PkContainer] = {layout_id: root_container}
        widgets: dict[str, PkWidget] = {}

        for child in root:
            self._parse_element(
                child,
                parent_container=root_container,
                scene=scene,
                view_model=view_model,
                resources=resources,
                base_path=base_path,
                containers=containers,
                widgets=widgets,
            )

        return PkLayout(root_container, containers, widgets)

    def _parse_element(
        self,
        element: ET.Element,
        *,
        parent_container: PkContainer,
        scene: PkScene,
        view_model: Any | None,
        resources: dict[str, Any],
        base_path: str | None,
        containers: dict[str, PkContainer],
        widgets: dict[str, PkWidget],
    ) -> None:
        """Parse a single XML element into a container or widget."""
        tag = _strip_namespace(element.tag).lower()
        attributes = _normalize_attributes(element.attrib)
        resolved_attrs = _resolve_attribute_values(
            attributes,
            view_model=view_model,
            resources=resources,
        )

        if tag == "container":
            self._parse_container(
                resolved_attrs,
                element,
                parent_container=parent_container,
                scene=scene,
                view_model=view_model,
                resources=resources,
                base_path=base_path,
                containers=containers,
                widgets=widgets,
            )
            return

        widget_spec = _WIDGET_SPECS.get(tag)
        if not widget_spec:
            raise ValueError(f"Unsupported element '{element.tag}'.")

        widget = self._parse_widget(
            resolved_attrs,
            widget_spec,
            parent_container=parent_container,
            view_model=view_model,
            resources=resources,
            base_path=base_path,
        )

        if widget.id in widgets:
            raise ValueError(f"Widget ID '{widget.id}' is already used.")
        widgets[widget.id] = widget
        parent_container.add_widget(widget)

    def _parse_container(
        self,
        attributes: dict[str, Any],
        element: ET.Element,
        *,
        parent_container: PkContainer,
        scene: PkScene,
        view_model: Any | None,
        resources: dict[str, Any],
        base_path: str | None,
        containers: dict[str, PkContainer],
        widgets: dict[str, PkWidget],
    ) -> None:
        """Create a container and parse its children."""
        container_id = attributes.get("id")
        if not container_id:
            raise ValueError("Container element requires an 'id' attribute.")

        rect = _parse_rect(attributes, default_rect=None)
        if rect is None:
            raise ValueError(
                f"Container '{container_id}' requires rect or x/y/width/height."
            )

        container = PkContainer(
            scene.app,
            parent_container.surface,
            container_id,
            rect,
            draw_outline=_parse_bool(attributes.get("draw_outline", False)),
        )

        if container_id in containers:
            raise ValueError(f"Container ID '{container_id}' is already used.")

        containers[container_id] = container
        parent_container.add_container(container)

        for child in element:
            self._parse_element(
                child,
                parent_container=container,
                scene=scene,
                view_model=view_model,
                resources=resources,
                base_path=base_path,
                containers=containers,
                widgets=widgets,
            )

    def _parse_widget(
        self,
        attributes: dict[str, Any],
        widget_spec: _WidgetSpec,
        *,
        parent_container: PkContainer,
        view_model: Any | None,
        resources: dict[str, Any],
        base_path: str | None,
    ) -> PkWidget:
        """Create a widget from attributes and spec."""
        widget_id = attributes.get("id")
        if not widget_id:
            raise ValueError("Widget element requires an 'id' attribute.")

        rect = _parse_rect(attributes, default_rect=None)
        if rect is None:
            raise ValueError(
                f"Widget '{widget_id}' requires rect or x/y/width/height."
            )

        style_attrs = _resolve_style_attributes(
            attributes.get("style"),
            resources=resources,
            view_model=view_model,
        )
        merged_attrs = dict(style_attrs)
        merged_attrs.update(attributes)

        kwargs: dict[str, Any] = {}
        for required in widget_spec.required_attrs:
            if required not in merged_attrs:
                raise ValueError(
                    f"Widget '{widget_id}' is missing required attribute '{required}'."
                )

        for attr_name, value in merged_attrs.items():
            if attr_name in {
                "id",
                "style",
                "x",
                "y",
                "width",
                "height",
                "rect",
                "source",
                "image",
            }:
                continue
            parser = widget_spec.arg_parsers.get(attr_name, _parse_literal)
            parsed = parser(value)
            kwargs[attr_name] = parsed

        kwargs = _apply_event_bindings(
            kwargs,
            widget_spec.event_attr_map,
            view_model=view_model,
        )

        if widget_spec.class_ref is PkImageWidget:
            if "image" in merged_attrs:
                kwargs["image"] = _resolve_image(
                    merged_attrs["image"],
                    base_path=base_path,
                    resources=resources,
                )
            elif "source" in merged_attrs:
                kwargs["image"] = _resolve_image(
                    merged_attrs["source"],
                    base_path=base_path,
                    resources=resources,
                )
            if "image" not in kwargs:
                raise ValueError(
                    f"Image widget '{widget_id}' requires 'source' or 'image'."
                )

        widget = widget_spec.class_ref(
            id_=widget_id,
            container=parent_container,
            rect=rect,
            **kwargs,
        )

        _apply_widget_state(widget, merged_attrs)
        return widget

    def _load_resources(
        self, resource_path: str, base_path: str | None
    ) -> dict[str, Any]:
        """Load resource definitions from JSON or XML."""
        resolved_path = _resolve_file_path(resource_path, base_path)
        _, ext = os.path.splitext(resolved_path)
        ext = ext.lower()

        if ext == ".json":
            with open(resolved_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, dict):
                raise ValueError("JSON resources must be a dictionary.")
            return data

        if ext in {".xml", ".resources"}:
            return _parse_xml_resources(resolved_path)

        raise ValueError("Unsupported resources file type.")


def _apply_event_bindings(
    kwargs: dict[str, Any],
    event_attr_map: dict[str, str],
    *,
    view_model: Any | None,
) -> dict[str, Any]:
    """Resolve event handler names to callables."""
    if not event_attr_map:
        return kwargs

    for xml_attr, ctor_arg in event_attr_map.items():
        if xml_attr not in kwargs:
            continue
        handler_name = kwargs[xml_attr]
        if not isinstance(handler_name, str):
            raise ValueError(f"Event handler '{xml_attr}' must be a string.")
        if view_model is None:
            raise ValueError(
                f"Event handler '{handler_name}' requires a view_model."
            )
        handler = _resolve_member(view_model, handler_name)
        if not callable(handler):
            raise ValueError(
                f"Handler '{handler_name}' on view_model is not callable."
            )
        kwargs[ctor_arg] = handler
        if xml_attr in kwargs and xml_attr != ctor_arg:
            del kwargs[xml_attr]
    return kwargs


def _resolve_style_attributes(
    style_name: Any,
    *,
    resources: dict[str, Any],
    view_model: Any | None,
) -> dict[str, Any]:
    """Resolve style resources into attribute dict."""
    if not style_name:
        return {}

    if not isinstance(style_name, str):
        raise ValueError("Style name must be a string.")
    if style_name not in resources:
        raise ValueError(f"Style '{style_name}' not found in resources.")

    style = resources[style_name]
    if not isinstance(style, dict):
        raise ValueError(f"Style '{style_name}' must be a dict.")

    normalized: dict[str, Any] = {}
    for key, value in style.items():
        normalized_key = _normalize_attr_name(key)
        normalized[normalized_key] = _resolve_value(
            value,
            view_model=view_model,
            resources=resources,
        )
    return normalized


def _resolve_attribute_values(
    attributes: dict[str, Any],
    *,
    view_model: Any | None,
    resources: dict[str, Any],
) -> dict[str, Any]:
    """Resolve binding and resource expressions in attributes."""
    resolved: dict[str, Any] = {}
    for key, value in attributes.items():
        normalized_key = _normalize_attr_name(key)
        resolved[normalized_key] = _resolve_value(
            value,
            view_model=view_model,
            resources=resources,
        )
    return resolved


def _resolve_value(
    value: Any,
    *,
    view_model: Any | None,
    resources: dict[str, Any],
) -> Any:
    """Resolve bindings and resource references inside values."""
    if not isinstance(value, str):
        return value

    match = _BINDING_PATTERN.match(value.strip())
    if not match:
        return value

    kind = match.group("kind").lower()
    token = match.group("value").strip()

    if kind == "binding":
        if view_model is None:
            raise ValueError("Binding requires a view_model.")
        return _resolve_member_path(view_model, token)

    if kind == "resource":
        if token not in resources:
            raise ValueError(f"Resource '{token}' not found.")
        return resources[token]

    return value


def _resolve_image(
    value: Any,
    *,
    base_path: str | None,
    resources: dict[str, Any],
) -> PkImage:
    """Resolve image references into a PkImage."""
    if isinstance(value, PkImage):
        return value

    if isinstance(value, str):
        if value in resources:
            value = resources[value]
        else:
            path = _resolve_file_path(value, base_path)
            return PkImage.from_file(os.path.basename(path), path)

    if isinstance(value, dict):
        path = value.get("path") or value.get("value")
        if path:
            resolved = _resolve_file_path(path, base_path)
            return PkImage.from_file(os.path.basename(resolved), resolved)

    raise ValueError("Invalid image reference.")


def _resolve_member(source: Any, name: str) -> Any:
    """Resolve a member from a dict or object by name."""
    if isinstance(source, dict):
        if name not in source:
            raise ValueError(f"Key '{name}' not found in view_model.")
        return source[name]
    if not hasattr(source, name):
        raise ValueError(f"Attribute '{name}' not found in view_model.")
    return getattr(source, name)


def _resolve_member_path(source: Any, path: str) -> Any:
    """Resolve a dotted path from a dict or object."""
    current = source
    for part in path.split("."):
        current = _resolve_member(current, part)
    return current


def _parse_rect(
    attributes: dict[str, Any],
    *,
    default_rect: tuple[float, float, float, float] | None,
) -> tuple[float, float, float, float] | None:
    """Parse rectangle values from attributes."""
    if "rect" in attributes:
        return _parse_rect_value(attributes["rect"])

    if all(key in attributes for key in ("x", "y", "width", "height")):
        return (
            _parse_number(attributes["x"]),
            _parse_number(attributes["y"]),
            _parse_number(attributes["width"]),
            _parse_number(attributes["height"]),
        )

    return default_rect


def _parse_rect_value(value: Any) -> tuple[float, float, float, float]:
    """Parse a rect tuple string into numeric values."""
    if isinstance(value, (tuple, list)) and len(value) == 4:
        return (
            _parse_number(value[0]),
            _parse_number(value[1]),
            _parse_number(value[2]),
            _parse_number(value[3]),
        )

    if not isinstance(value, str):
        raise ValueError("Rect value must be a comma-separated string.")

    parts = [part.strip() for part in value.split(",")]
    if len(parts) != 4:
        raise ValueError("Rect must contain 4 comma-separated values.")
    return (
        _parse_number(parts[0]),
        _parse_number(parts[1]),
        _parse_number(parts[2]),
        _parse_number(parts[3]),
    )


def _parse_literal(value: Any) -> Any:
    """Parse common literal types from strings."""
    if not isinstance(value, str):
        return value

    if value == "":
        return value

    lowered = value.strip().lower()
    if lowered in {"true", "false"}:
        return lowered == "true"
    if lowered in {"none", "null"}:
        return None

    if "," in value:
        parts = [part.strip() for part in value.split(",")]
        return tuple(_parse_number(part) for part in parts)

    try:
        if "." in value or "e" in lowered:
            return float(value)
        return int(value)
    except ValueError:
        return value


def _parse_bool(value: Any) -> bool:
    """Parse a boolean value."""
    if isinstance(value, bool):
        return value
    if not isinstance(value, str):
        return bool(value)
    lowered = value.strip().lower()
    if lowered in {"true", "1", "yes"}:
        return True
    if lowered in {"false", "0", "no"}:
        return False
    raise ValueError(f"Invalid boolean value: {value}")


def _parse_int(value: Any) -> int:
    """Parse an integer value."""
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if not isinstance(value, str):
        raise ValueError(f"Invalid integer value: {value}")
    return int(float(value))


def _parse_number(value: Any) -> float:
    """Parse a numeric value."""
    if isinstance(value, (int, float)):
        return float(value)
    if not isinstance(value, str):
        raise ValueError(f"Invalid number: {value}")
    return float(value)


_WIDGET_SPECS: dict[str, _WidgetSpec] = {
    "label": _WidgetSpec(
        class_ref=PkLabelWidget,
        required_attrs=set(),
        arg_parsers={
            "text": str,
            "font_id": str,
            "text_color": _parse_literal,
            "background_color": _parse_literal,
            "text_wrap": _parse_bool,
            "text_align": str,
            "vertical_align": str,
        },
        event_attr_map={},
    ),
    "button": _WidgetSpec(
        class_ref=PkButtonWidget,
        required_attrs={"label"},
        arg_parsers={
            "label": str,
            "on_click": str,
            "on_hover": str,
            "disabled": _parse_bool,
            "font_id": str,
            "background_color": _parse_literal,
            "background_color_disabled": _parse_literal,
            "background_color_pressed": _parse_literal,
            "background_color_hovered": _parse_literal,
            "text_color": _parse_literal,
            "text_align": str,
            "border_radius": _parse_int,
        },
        event_attr_map={
            "on_click": "on_click",
            "on_hover": "on_hover",
        },
    ),
    "textinput": _WidgetSpec(
        class_ref=PkTextInputWidget,
        required_attrs=set(),
        arg_parsers={
            "text": str,
            "on_change": str,
            "on_focus": str,
            "on_unfocus": str,
            "disabled": _parse_bool,
            "font_id": str,
            "background_color": _parse_literal,
            "background_color_disabled": _parse_literal,
            "background_color_focused": _parse_literal,
            "text_color": _parse_literal,
            "text_align": str,
            "border_radius": _parse_int,
            "padding": _parse_int,
            "max_length": _parse_int,
            "placeholder": str,
            "placeholder_color": _parse_literal,
            "placeholder_color_disabled": _parse_literal,
            "placeholder_color_focused": _parse_literal,
        },
        event_attr_map={
            "on_change": "change_hook",
            "on_focus": "focus_hook",
            "on_unfocus": "unfocus_hook",
        },
    ),
    "image": _WidgetSpec(
        class_ref=PkImageWidget,
        required_attrs=set(),
        arg_parsers={
            "resize_mode": str,
            "on_click": str,
            "on_hover": str,
            "disabled": _parse_bool,
            "background_color": _parse_literal,
            "border_radius": _parse_int,
        },
        event_attr_map={
            "on_click": "click_hook",
            "on_hover": "hover_hook",
        },
    ),
}


def _apply_widget_state(widget: PkWidget, attrs: dict[str, Any]) -> None:
    """Apply state flags after widget creation."""
    if "visible" in attrs:
        widget.visible = _parse_bool(attrs["visible"])
    if "disabled" in attrs and hasattr(widget, "disabled"):
        setattr(widget, "disabled", _parse_bool(attrs["disabled"]))


def _normalize_attributes(attributes: dict[str, Any]) -> dict[str, Any]:
    """Normalize attribute names to snake_case."""
    normalized: dict[str, Any] = {}
    for key, value in attributes.items():
        normalized_key = _normalize_attr_name(key)
        normalized[normalized_key] = value
    return normalized


def _normalize_attr_name(name: str) -> str:
    """Normalize an attribute name to snake_case."""
    snake = _CAMEL_TO_SNAKE.sub(r"\1_\2", name)
    return snake.replace("-", "_").lower()


def _strip_namespace(tag: str) -> str:
    """Remove XML namespace from a tag name."""
    if "}" in tag:
        return tag.split("}", 1)[1]
    return tag


def _resolve_file_path(path: str, base_path: str | None) -> str:
    """Resolve a path relative to base_path if needed."""
    if os.path.isabs(path):
        return path
    if base_path:
        return os.path.normpath(os.path.join(base_path, path))
    return path


def _parse_xml_resources(path: str) -> dict[str, Any]:
    """Parse XML resources into a dictionary."""
    tree = ET.parse(path)
    root = tree.getroot()
    tag = _strip_namespace(root.tag).lower()
    if tag != "resources":
        raise ValueError("Resources XML must have <Resources> root.")

    resources: dict[str, Any] = {}
    for child in root:
        child_tag = _strip_namespace(child.tag).lower()
        key = child.attrib.get("key")
        if not key:
            raise ValueError("Resource entries require a 'key' attribute.")

        if child_tag in {"value", "resource"}:
            resources[key] = child.attrib.get("value")
            continue

        if child_tag == "image":
            resources[key] = {"path": child.attrib.get("path")}
            continue

        if child_tag == "style":
            setters: dict[str, Any] = {}
            for setter in child:
                setter_tag = _strip_namespace(setter.tag).lower()
                if setter_tag != "setter":
                    raise ValueError("Style entries must contain <Setter>.")
                name = setter.attrib.get("name")
                if not name:
                    raise ValueError(
                        "Style setter requires a 'name' attribute."
                    )
                setters[name] = setter.attrib.get("value")
            resources[key] = setters
            continue

        raise ValueError(f"Unsupported resource element '{child.tag}'.")

    return resources
