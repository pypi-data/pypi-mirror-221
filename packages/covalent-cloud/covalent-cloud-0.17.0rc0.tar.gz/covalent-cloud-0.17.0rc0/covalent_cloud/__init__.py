# Copyright 2023 Agnostiq Inc.


from importlib import metadata

from .cloud_executor.cloud_executor import CloudExecutor
from .dispatch_management import dispatch, get_result
from .service_account_interface.auth_config_manager import get_api_key, save_api_key
from .service_account_interface.client import get_client
from .shared.classes.settings import settings
from .swe_management.swe_manager import create_env

# TODO: Also edit this once QiskitExecutor file is moved
from .qiskit_executor import QiskitExecutor

__version__ = metadata.version("covalent_cloud")
