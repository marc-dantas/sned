from sys import stderr


def log_info(value: str) -> None:
    print(f"snake editor: info: {value}", file=stderr)


def log_fatal(value: str) -> None:
    print(f"snake editor: fatal: {value}", file=stderr)


def log_warning(value: str) -> None:
    print(f"snake editor: warning: {value}", file=stderr)
