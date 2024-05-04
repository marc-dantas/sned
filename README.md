# Snake Editor Alpha

Snake Editor is a minimalistic Python code editor written 100% in Python programming language.

> Snake Editor was a very old project I've already written alongside @Kamasoo, but I lost the project files. So I decided to rewrite it.

The goal of Snake Editor is to be an fan-made alternative to the built-in IDLE with high customization capabilities. If you are new in Python or want to contribute this is also a good project for you.

> Snake Editor is also built to be an educational project. Not means to be used in production.

## Getting things running
For now, Snake Editor is in its early stages of development and there's no way to use it as an proper Python package. So you need to run it manually by the source code.

To be able to use Snake Editor, you need an instance of the Python interpreter version 3.9 or higher and `pip` installed.

- 1st step: Clone the source code from the repository.
    ```console
    $ git clone https://github.com/marc-dantas/snake_editor/
    ```
- 2nd step: Get into the repository's folder.
    ```console
    $ cd snake_editor
    ```
> **Note**: Snake Editor doesn't use any third-party Python packages or libraries. You just need a full installation of Python's standard library to be able to run Snake Editor. 
- 3rd step: Run the main script.
    ```console
    $ python src/main.py
    ```

These steps should make you through the process and make you run Snake Editor properly.

## Developer Milestones

- [X] Base project
- [ ] Improved layout
- [X] Dark mode (see customization section below for more information)
- [X] Line numbers
- [ ] Python package


## Tutorial
### Usage
Snake Editor has a very simple command line interface to add some simple functionality to the user.

```
usage: snake editor [-h] [-r RESOLUTION] [-s SETTINGS]

Snake Editor CLI

options:
  -h, --help            show this help message and exit
  -r RESOLUTION, --resolution RESOLUTION
                        changes the window resolution.
  -s SETTINGS, --settings SETTINGS
                        changes the settings file path to be read.

Copyright 2023 @marc-dantas @Kamasoo. This software is under MIT License
```

### Configuration
Snake Editor was always meant to be a very customizable Python editor. It works with configuration files. By default it will search for `settings.json` in the current directory.

You can specify the configuration file via command line in case you don't want to load `settings.json`. Here's a simple example.

```console
$ python src/main.py # This will search for default `settings.json`
```

```console
$ python src/main.py -s foo.json # This will search for `foo.json`
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
  $ python src/main.py -s templates/lighttheme.json
  ```
- Dark theme (`darktheme.json`)
  ```console
  $ python src/main.py -s templates/darktheme.json
  ```

If you do not provide the configuration file, Snake Editor will use the [`settings.json`](./settings.json) file.


---



> By @marc-dantas

> By @Kamasoo