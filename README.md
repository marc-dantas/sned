# Sned Alpha
Sned (**SN**ake **ED**itor) is a minimalistic Python code editor written 100% in Python programming language.

> Sned was a very old project (originally named Snake Editor) I've already written al ongside @Kamasoo, but I lost the project files. So I decided to rewrite it.

The goal of Sned is to be an fan-made alternative to the built-in IDLE with high customization capabilities. If you are new in Python or want to contribute this is also a good project for you.

> Sned is also built to be an educational project. Not means to be used in production.

## Getting things running

> **NOTE**: You need an instance of the Python interpreter version 3.9 or higher and `pip` installed.

To use it, you need to install Sned via `pip`:
```console
$ python -m pip install git+https://github.com/marc-dantas/sned.git#egg=sned
```

Now you can use it:
```console
$ python -m sned
```

## Developer Milestones

- [X] Base project
- [ ] Improved layout
- [X] Dark mode (see customization section below for more information)
- [X] Line numbers
- [X] Python package


## Tutorial
### Usage
Sned has a very simple command line interface to add some simple functionality to the user.

```
usage: sned [-h] [-r RESOLUTION] [-s SETTINGS]

Sned CLI

options:
  -h, --help            show this help message and exit
  -r RESOLUTION, --resolution RESOLUTION
                        changes the window resolution.
  -s SETTINGS, --settings SETTINGS
                        changes the settings file path to be read.

Copyright (c) 2024 @marc-dantas. This software is licensed under MIT License.
```

### Configuration
Sned was always meant to be a very customizable Python editor. It works with configuration files. By default it will search for `settings.json` in the current directory.

You can specify the configuration file via command line in case you don't want to load `settings.json`. Here's a simple example.

```console
$ python -m sned # This will search for default `settings.json`
```

```console
$ python -m sned -s foo.json # This will search for `foo.json`
```

#### Configuration Format

The configuration format is very simple:

- `editor`: Text editor configuration
  - `font`: Name of the font used in the text editor
  - `font_size`: Size of the font used in the text editor
  - `tab_size`: Amount of spaces inserted when `[TAB]` is pressed.
  - `background`: Background of the application
  - `foreground`: Foreground (text color) of the application
- `syntax`: Syntax highlighting customization
  - `COMMENT`: Python comment color (e.g. `# ram spam eggs`)
  - `KEYWORD`: Python keyword color (e.g. `def`, `if`, `import`)
  - `BUILTIN`: Python built-in function or name color (e.g. `print`, `filter`, `any`)
  - `STRING`: String literal color (e.g. `"Hello World!"`)
  - `DEFINITION`: Definition literal color (function, class, etc.)

Here's an example configuration file:

```json
{
  "editor": {
    "font": "Consolas",
    "font_size": 20,
    "tab_size": 4,
    "foreground": "#000000",
    "background": "#FFFFFF"
  },
  "syntax": {
    "COMMENT": "#6A9955",
    "KEYWORD": "#0000FF",
    "BUILTIN": "#267F99",
    "STRING": "#B51515",
    "DEFINITION": "#795E26"
  }
}
```

### Customization
In this repository, there's a folder `templates` where you can find two different configuration files with specific color settings. To load them, just use the command line flag `-s` (or `--settings`) to use the themes.

> NOTE: Inside the editor you can customize the theme in the Settings window (shortcut: Ctrl+.)

- Light theme (`lighttheme.json`)
  ```console
  $ python -m sned -s templates/lighttheme.json
  ```
- Dark theme (`darktheme.json`)
  ```console
  $ python -m sned -s templates/darktheme.json
  ```

If you do not provide the configuration file, Sned will use the [`settings.json`](./settings.json) file.

---

> By @marc-dantas

> By @Kamasoo