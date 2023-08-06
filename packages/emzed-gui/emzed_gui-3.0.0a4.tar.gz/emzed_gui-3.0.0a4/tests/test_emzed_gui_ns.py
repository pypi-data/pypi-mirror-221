#!/usr/bin/env python

def test_emzed_tui_ns(regtest):
    from emzed.remote_package import RemoteModule
    import emzed.gui
    assert isinstance(emzed.gui.emzed_gui, RemoteModule)
    dd = sorted(d for d in dir(emzed.gui) if not d.startswith("_"))
    print(dd, file=regtest)
