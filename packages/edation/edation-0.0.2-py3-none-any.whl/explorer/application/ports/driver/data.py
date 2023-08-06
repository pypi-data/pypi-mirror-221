#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Explorer                                                                            #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.11                                                                             #
# Filename   : /explorer/application/ports/driver/data.py                                          #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/explorer                                           #
# ------------------------------------------------------------------------------------------------ #
# Created    : Thursday June 22nd 2023 08:44:23 pm                                                 #
# Modified   : Friday June 23rd 2023 08:05:32 am                                                   #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
from abc import ABC, abstractmethod
from datetime import datetime

from dependency_injector import inject, Provide
import pandas as pd

from explorer.container import ExplorerContainer
from explorer.adapter.identity import IDGenerator
from explorer.domain.data import Dataset
from .base import DTO


# ------------------------------------------------------------------------------------------------ #
#                                DATASET REQUEST DTO                                               #
# ------------------------------------------------------------------------------------------------ #
class DatasetRequestDTO(DTO):
    name: str
    dataset: pd.DataFrame
    stage: str = "raw"
    created: datetime = datetime.now()
    id: str = None

    def __post_init__(
        self, id_gen: IDGenerator = Provide[ExplorerContainer.adapters.idgen]
    ) -> None:
        self.id = id_gen.generate_id()


# ------------------------------------------------------------------------------------------------ #
#                               DATASET REQUEST COMMAND                                            #
# ------------------------------------------------------------------------------------------------ #
class DatasetRequest:
    """Command to request the creation of the Dataset entity."""
    def __init__(self, dto: DatasetRequestDTO) -> None:
        self._dto = dto

    def __call__(self) -> Dataset:
        



class DataService(ABC):
    """Provides interface for Data related services"""

    @abstractmethod
    def create_dataset(self, data: pd.DataFrame, name: str, version: str = None) -> Dataset:
        """Creates a Dataset object."""

    @abstractmethod
    def get_dataset(self, id: str) -> Dataset:
        """Retrives a Dataset object from the repository."""

    @abstractmethod
    def view_datasets(self) -> pd.DataFrame:
        """Returns a DataFrame of datasets in the repository."""
