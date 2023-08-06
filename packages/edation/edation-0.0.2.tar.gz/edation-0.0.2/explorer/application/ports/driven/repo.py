#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Explorer                                                                            #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.11                                                                             #
# Filename   : /explorer/application/ports/driven/repo.py                                          #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/explorer                                           #
# ------------------------------------------------------------------------------------------------ #
# Created    : Thursday June 22nd 2023 11:59:43 pm                                                 #
# Modified   : Friday June 23rd 2023 03:31:03 am                                                   #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
from abc import ABC, abstractmethod
from typing import Any
import logging

import pandas as pd


# ------------------------------------------------------------------------------------------------ #
class RepoPort(ABC):
    """Port defining the interface for repositories."""

    def __init__(self) -> None:
        self._logger = logging.getLogger(f"{self.__class__.__name__}")

    @abstractmethod
    def add(self, *args, **kwargs) -> None:
        """Adds an entity to the repository"""

    @abstractmethod
    def get(self, id: str) -> Any:
        """Retrieves an entity from the repository."""

    @abstractmethod
    def remove(self, id: str) -> None:
        """Removes an entity from the repository"""

    @abstractmethod
    def registry(self) -> pd.DataFrame:
        """Returns the registry of entities from the repository"""
