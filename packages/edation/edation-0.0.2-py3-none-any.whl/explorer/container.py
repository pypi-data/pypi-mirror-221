#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Explorer                                                                            #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.10                                                                             #
# Filename   : /explorer/container.py                                                              #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/explorer                                           #
# ------------------------------------------------------------------------------------------------ #
# Created    : Monday March 27th 2023 07:02:56 pm                                                  #
# Modified   : Friday June 23rd 2023 02:28:09 am                                                   #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
"""Framework Dependency Container"""
import logging.config  # pragma: no cover

from dependency_injector import containers, providers

from explorer.adapter.identity import IDGenerator, FakeIDGenerator


# ------------------------------------------------------------------------------------------------ #
#                                        LOGGING                                                   #
# ------------------------------------------------------------------------------------------------ #
class LoggingContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    logging = providers.Resource(
        logging.config.dictConfig,
        config=config,
    )


# ------------------------------------------------------------------------------------------------ #
#                                          ADAPTER                                                 #
# ------------------------------------------------------------------------------------------------ #
class AdapterContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    idgen = providers.Singleton(IDGenerator, filepath=config.idgen.filepath, size=config.idgen.size)

    fake_idgen = providers.Singleton(FakeIDGenerator)


# ------------------------------------------------------------------------------------------------ #
#                                          FRAMEWORK                                               #
# ------------------------------------------------------------------------------------------------ #
class ExplorerContainer(containers.DeclarativeContainer):
    log_config = providers.Configuration(yaml_files=["config/logging.yml"])

    stats_config = providers.Configuration(yaml_files=["config/stats.yml"])

    adapter_config = providers.Configuration(yaml_files=["config/adapters.yml"])

    logs = providers.Container(LoggingContainer, config=log_config.logging)

    adapters = providers.Container(AdapterContainer, config=adapter_config)
