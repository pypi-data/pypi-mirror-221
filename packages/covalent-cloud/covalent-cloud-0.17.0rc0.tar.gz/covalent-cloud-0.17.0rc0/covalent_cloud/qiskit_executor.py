# Copyright 2023 Agnostiq Inc.

# TODO: Move this file to an appropriate location once qelectron stuff is merged

from typing import Optional
from pydantic import BaseModel


class Options(BaseModel):
    """
    Options for the QiskitExecutor
    """

    optimization_level: int = 3
    resilience_level: int = 3


class QiskitExecutor(BaseModel):
    """
    QiskitExecutor represents the configuration to use when executing the QElectron
    on the Qiskit backend.
    """

    backend: str
    shots: Optional[int] = 1024
    single_job: bool = False
    max_execution_time: int = None
    options: Options = None
