from . import debug, engine, views
from argparse import ArgumentParser

DEFAULT_SETTINGS_FILE = "settings.json"
DEFAULT_RESOLUTION = "600x600"


def parse_argv():
    p = ArgumentParser("sned",
                       description="Sned CLI",
                       epilog="Copyright (c) 2024 @marc-dantas. "
                       "This software is licensed under MIT License.")
    p.add_argument("-r", "--resolution",
                   help="changes the window resolution.",
                   default=DEFAULT_RESOLUTION)
    p.add_argument(
        "-s", "--settings",
        help="changes the settings file path to be read.",
        default=DEFAULT_SETTINGS_FILE
    )
    return p.parse_args()


def main() -> None:
    args = parse_argv()
    settings = engine.load_settings(args.settings)
    res = args.resolution.split('x')
    if (len(res) <= 1) or any(not x.isdigit() for x in res):
        debug.log_warning(f"invalid resolution specifier (using default {DEFAULT_RESOLUTION}).")
        res = DEFAULT_RESOLUTION.split('x')
    editor = views.Editor(tuple(res), settings, args.settings)
    debug.log_info("event trigger: window (Editor)")
    editor.draw()


if __name__ == "__main__":
    main()
