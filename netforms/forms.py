from clr import System, GetClrType

from .utils import __WRAPPER_CLASSES, get_wrapper_class


class Form(get_wrapper_class(System.Windows.Forms.Form)):
    def __init__(self, *args, controls=None, **kwargs):
        super(Form, self).__init__(*args, **kwargs)

        for control in controls or []:
            self.controls.add(control)

        self.initialize_components()

    def initialize_components(self):
        self.initialize_component()

    def initialize_component(self):
        self.InitializeComponent()

    def InitializeComponent(self):
        pass


__WRAPPER_CLASSES[System.Windows.Forms.Form] = Form

# These types are found in controls.py and components.py
__BLACKLIST_TYPES = [System.Windows.Forms.Control, System.ComponentModel.Component]


def __getattr__(name):
    _original_class = getattr(System.Windows.Forms, name)
    clr_type = GetClrType(_original_class)

    if any(clr_type.IsSubclassOf(blacklist_type) for blacklist_type in __BLACKLIST_TYPES):
        raise AttributeError(name)

    return get_wrapper_class(_original_class)


class TabControl(get_wrapper_class(System.Windows.Forms.TabControl)):
    list_arguments = ["Controls", ]


class TabPage(get_wrapper_class(System.Windows.Forms.TabPage)):
    list_arguments = ["Controls", ]
