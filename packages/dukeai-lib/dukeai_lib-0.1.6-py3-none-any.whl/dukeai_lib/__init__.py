"""

dukeai_lib

Common functions used across the DUKE.ai project environments.

"""
from .tools import tools
from .tools.tools import gen_random_sha

from .utilities import utilities
from .utilities.utilities import DecimalEncoder

from .application import application
from .application.application import check_access, api_response

__version__ = "0.1.6"
__author__ = "Blake Donahoo"



