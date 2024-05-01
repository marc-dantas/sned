from application import debug, engine, views
from argparse import ArgumentParser

DEFAULT_SETTINGS_FILE = "settings.json"
DEFAULT_RESOLUTION = "600x600"


def parse_argv():
    p = ArgumentParser("snake editor",
                       description="Snake Editor CLI",
                       epilog="Copyright 2023 @marc-dantas @Kamasoo. "
                       "This software is under MIT License")
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
    editor = views.Editor(args.resolution, settings, args.settings)
    debug.log_info("event trigger: window (Editor)")
    editor.draw()


if __name__ == "__main__":
    main()

