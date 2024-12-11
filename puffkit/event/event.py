# -*- coding: utf-8 -*-
"""Event manager module for puffkit."""

from __future__ import annotations

from typing import Any


class PkEvent:
    """Event class for puffkit.

    Represents an event in the event queue.
    """

    def __init__(self, type: int, dict: dict[str, Any], **kwargs: Any) -> None:
        """Initialize the event class.

        Args:
            type (int): The type of the event.
            dict (dict[str, Any]): The event dictionary.
            **kwargs (Any): Additional arguments.
        """
        self.type = type
        self.dict = dict
        self.__dict__.update(dict)

        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def from_pygame(cls, event: Any) -> PkEvent:
        """Create a PkEvent from a Pygame event.

        Args:
            event (Any): The Pygame event.

        Returns:
            PkEvent: The PkEvent.
        """
        return cls(event.type, event.dict)

    def __str__(self) -> str:
        """Return the string representation of the event.

        Returns:
            str: The string representation of the event.
        """
        return f"<PkEvent type={self.type} dict={self.dict}>"

    def __repr__(self) -> str:
        """Return the string representation of the event.

        Returns:
            str: The string representation of the event.
        """
        return f"<PkEvent type={self.type} dict={self.dict}>"

    def __getattribute__(self, name: str) -> Any:
        """Get an attribute from the event.

        Args:
            name (str): The name of the attribute to get.

        Returns:
            any: The attribute value.
        """
        return super().__getattribute__(name)

    def __setattr__(self, name: str, value: Any) -> None:
        """Set an attribute in the event.

        Args:
            name (str): The name of the attribute to set.
            value (any): The value to set the attribute to.
        """
        super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        """Delete an attribute from the event.

        Args:
            name (str): The name of the attribute to delete.
        """
        super().__delattr__(name)

    def __bool__(self) -> bool:
        """Return whether the event is truthy.

        Returns:
            bool: Whether the event is truthy.
        """
        return True
