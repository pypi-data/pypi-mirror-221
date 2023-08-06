#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Explorer                                                                            #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.11                                                                             #
# Filename   : /explorer/application/ports/driven/identity.py                                      #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/explorer                                           #
# ------------------------------------------------------------------------------------------------ #
# Created    : Thursday June 22nd 2023 11:59:19 pm                                                 #
# Modified   : Friday June 23rd 2023 02:16:26 am                                                   #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
from abc import ABC, abstractmethod


# ------------------------------------------------------------------------------------------------ #
class IDGenPort(ABC):
    """Defines the port for identity generation"""

    @abstractmethod
    def generate_id(self) -> str:
        """Returns a random unique numeric identifier in string format."""
