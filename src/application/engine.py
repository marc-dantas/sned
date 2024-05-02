import json
from . import debug
from idlelib.colorizer import ColorDelegator
from idlelib.percolator import Percolator
from tkinter import Text, filedialog, messagebox
from io import TextIOWrapper
from typing import Any


def message(value: str) -> None:
    messagebox.showinfo(title="Message", message=value)


def error(value: str) -> None:
    messagebox.showerror(title="Error", message=value)


def ask_unsaved() -> str:
    return messagebox.askquestion(title="File not saved",
                                  message="Are you sure you want to "
                                  "discard your unsaved changes in "
                                  "the current file?")


def save_file(path: str, contents: str):
    try:
        with open(path, "w") as f:
            f.write(contents)
        debug.log_info(f"file \"{path}\" saved successfully")
    except Exception as e:
        debug.log_fatal(f"unable to open file {path}a: {e}")
        exit(1)


def open_file(path: str, mode: str = None) -> TextIOWrapper:
    mode = mode if mode is not None else "r"
    f = None
    try:
        f = open(path, mode)
        debug.log_info(f"file \"{path}\" opened successfully")
    except Exception as e:
        debug.log_fatal(f"unable to open file: {e}")
        exit(1)
    return f


FILETYPES = (("Python module", "*.py"), ("All", "*"))


def editor_ask_save_file():
    path = filedialog.asksaveasfilename(title="Save", filetypes=FILETYPES)
    return path


def editor_ask_file() -> str:
    path = filedialog.askopenfilename(title="Open", filetypes=FILETYPES)
    return path


def check_settings(settings: dict) -> None:
    syntax_fields = {"COMMENT", "KEYWORD",
                     "BUILTIN", "STRING",
                     "DEFINITION"}
    editor_fields = {"font", "tab_size", "font_size", "background", "foreground"}
    # using set because of the independent order
    assert set(settings.keys()) == {"editor", "syntax"}, "invalid fields"
    assert set(settings["editor"]) == editor_fields, "invalid fields for editor"
    assert set(settings["syntax"]) == syntax_fields, "invalid fields for syntax"


def load_settings(file: str) -> Any:
    settings = {}
    try:
        settings = json.load(open_file(file))
    except Exception as e:
        debug.log_fatal(f"invalid configuration JSON format: {e}")
        exit(1)

    try:
        check_settings(settings)
    except AssertionError as e:
        debug.log_fatal(f"invalid configuration format: {e}")
        exit(1)

    debug.log_info(f"settings file loaded successfully")
    return settings


def highlight(text: Text, settings) -> None:
    d = ColorDelegator()

    def field(foreground: str) -> dict:
        return {
            "background": settings["editor"]["background"],
            "foreground": foreground
        }
    
    d.tagdefs['COMMENT'] = field(settings["syntax"]["COMMENT"])
    d.tagdefs['KEYWORD'] = field(settings["syntax"]["KEYWORD"])
    d.tagdefs['BUILTIN'] = field(settings["syntax"]["BUILTIN"])
    d.tagdefs['STRING'] = field(settings["syntax"]["STRING"])
    d.tagdefs['DEFINITION'] = field(settings["syntax"]["DEFINITION"])
    p = Percolator(text)
    p.insertfilter(d)
