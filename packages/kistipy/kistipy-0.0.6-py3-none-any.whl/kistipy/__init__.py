import logging
import sys

from kistipy.sdk.type.common import *

logger = logging.getLogger("kistipy")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)
