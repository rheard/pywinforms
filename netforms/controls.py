import logging

import clr

from clr import System

from . import utils

logger = logging.getLogger(__name__)


def __getattr__(name):
    _original_class = getattr(System.Windows.Forms, name)

    if not clr.GetClrType(_original_class).IsSubclassOf(System.Windows.Forms.Control):
        raise AttributeError(name)

    return utils.get_wrapper_class(_original_class)
