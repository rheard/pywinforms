import clr

from clr import System

from . import utils


def __getattr__(name):
    _original_class = getattr(System.Windows.Forms, name, None)

    if _original_class is None:
        _original_class = getattr(System.ComponentModel, name)

    elif not clr.GetClrType(_original_class).IsSubclassOf(System.ComponentModel.Component):
        raise AttributeError(name)

    return utils.get_wrapper_class(_original_class)
