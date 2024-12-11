# -*- coding: utf-8 -*-

from typing import Final
import pygame


class PkEventConstants:  # pragma: no cover
    """Event constants class for puffkit.

    Contains constants for Pygame events.
    """

    QUIT: Final[int] = pygame.QUIT
    ACTIVEEVENT: Final[int] = pygame.ACTIVEEVENT
    KEYDOWN: Final[int] = pygame.KEYDOWN
    KEYUP: Final[int] = pygame.KEYUP
    MOUSEMOTION: Final[int] = pygame.MOUSEMOTION
    MOUSEBUTTONUP: Final[int] = pygame.MOUSEBUTTONUP
    MOUSEBUTTONDOWN: Final[int] = pygame.MOUSEBUTTONDOWN
    JOYAXISMOTION: Final[int] = pygame.JOYAXISMOTION
    JOYBALLMOTION: Final[int] = pygame.JOYBALLMOTION
    JOYHATMOTION: Final[int] = pygame.JOYHATMOTION
    JOYBUTTONUP: Final[int] = pygame.JOYBUTTONUP
    JOYBUTTONDOWN: Final[int] = pygame.JOYBUTTONDOWN
    VIDEORESIZE: Final[int] = pygame.VIDEORESIZE
    VIDEOEXPOSE: Final[int] = pygame.VIDEOEXPOSE
    USEREVENT: Final[int] = pygame.USEREVENT
    NUMEVENTS: Final[int] = pygame.NUMEVENTS
