#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Explorer                                                                            #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.11                                                                             #
# Filename   : /explorer/adapter/repo/file_visual.py                                               #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/explorer                                           #
# ------------------------------------------------------------------------------------------------ #
# Created    : Friday June 23rd 2023 03:10:02 am                                                   #
# Modified   : Friday June 23rd 2023 05:00:12 am                                                   #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
import os

from explorer.application.ports.driven.repo import RepoPort


# ------------------------------------------------------------------------------------------------ #
class FileVisualRepo(RepoPort):
    """File repository for storing visualizations in image format."""

    def __init__(self, location: str) -> None:
        super().__init__()
        self._location = location
        os.makedirs(self._location, exist_ok=True)

    def add(self, *args, **kwargs) -> None:
        """Adds an entity to the repository"""

    def get(self, id: str) -> Any:
        """Retrieves an entity from the repository."""

    def remove(self, id: str) -> None:
        """Removes an entity from the repository"""

    def registry(self) -> pd.DataFrame:
        """Returns the registry of entities from the repository"""
