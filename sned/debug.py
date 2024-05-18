from sys import stderr


def log_info(value: str) -> None:
    print(f"sned: info: {value}", file=stderr)


def log_fatal(value: str) -> None:
    print(f"sned: fatal: {value}", file=stderr)


def log_warning(value: str) -> None:
    print(f"sned: warning: {value}", file=stderr)
