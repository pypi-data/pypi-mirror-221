#! /usr/bin/env python
# Copyright 2020 Uwe Schmitt <uwe.schmitt@id.ethz.ch>

import sys


try:
    import emzed_gui

    has_emzed_gui = True
except ImportError:
    has_emzed_gui = False

    def __dir__():
        return []


if has_emzed_gui:
    from emzed.remote_package import RemoteModule

    emzed_gui = RemoteModule(sys.executable, "emzed_gui")  # noqa: F811
    __dir__ = emzed_gui.__dir__  # noqa: F811


def __getattr__(name):
    if not has_emzed_gui:
        raise AttributeError("please install emzed_gui package first.")

    return getattr(emzed_gui, name)
