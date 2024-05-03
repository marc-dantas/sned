from . import engine, debug
import webbrowser
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from os.path import exists, split


class Editor(Tk):

    def __init__(self, res: tuple, settings, sf: str) -> None:
        super().__init__()
        self.geometry(f"{res[0]}x{res[1]}")
        self.minsize(res[0], res[1])
        self.file = ""
        self._settings = settings
        self.sf = sf
        self.unsaved = False
        self.title(f"Snake Editor - new*")
        self.protocol("WM_DELETE_WINDOW", self._on_window_close)

    def _on_window_close(self) -> None:
        x = "no"
        if self.unsaved:
            x = engine.ask_unsaved()
        if x == "yes" or not self.unsaved:
            self.destroy()

    def _on_change(self, index: str, target: Label) -> None:
        self.title(f"Snake Editor - {self.file if self.file else 'new'}*")
        self.unsaved = True
        line, col = index.split('.')
        target['text'] = f"{self.file if self.file else 'new'}:{line}:{col}"
    
    def _on_tab(self, target: Text) -> str:
        target.insert(INSERT, (" "*self._settings["editor"]["tab_size"]))
        return "break"
    
    def _increase_font(self, target: Text) -> str:
        fontsize = int(target['font'].split()[1])
        target.config(font=(self._settings["editor"]["font"], fontsize + 1))
        return "break"
    
    def _decrease_font(self, target: Text) -> str:
        fontsize = int(target['font'].split()[1])
        if fontsize == 0:
            return "break"
        target.config(font=(self._settings["editor"]["font"], fontsize - 1))
        return "break"
    
    def save(self, contents: str) -> None:
        debug.log_info("event trigger: save")
        self.unsaved = False
        if not self.file:
            path = engine.editor_ask_save_file()
            if not path:
                engine.error("No such file or directory")
                return
            self.file = split(path)[1] # tail
            engine.save_file(path, contents)
        else:
            engine.save_file(self.file, contents)
        self.title(f"Snake Editor - {self.file if self.file else 'new'}")

    def open(self, target: Text) -> None:
        print(target.index(INSERT))
        debug.log_info("event trigger: open")
        if self.unsaved and engine.ask_unsaved() == "no":
            return
        path = engine.editor_ask_file()
        if not path:
            return
        if not exists(path):
            engine.error("No such file or directory")
            return
        f = engine.open_file(path)
        target.delete("1.0", END)
        target.insert("1.0", f.read())
        self.file = split(path)[1] # tail
        self.title(f"Snake Editor - {self.file if self.file else 'new'}")

    def credits(self) -> None:
        window = Credits(self, (800, 300), self._settings)
        debug.log_info("event trigger: window (Credits)")
        window.draw()

    def settings(self) -> None:
        window = Settings(
            self, (600, 600), self._settings if self._settings is not None else {}, self.sf)
        debug.log_info("event trigger: window (Settings)")
        window.draw()

    def draw(self) -> None:
        menu = Menu()
        file = Menu(menu, tearoff=False)
        file.add_command(
            label="Open file",
            accelerator="Ctrl+O",
            command=lambda: self.open(text)
        )
        self.bind("<Control-o>", lambda _: self.open(text))
        file.add_command(
            label="Save file",
            accelerator="Ctrl+S",
            command=lambda: self.save(text.get("1.0", END))
        )
        self.bind("<Control-s>", lambda _: self.save(text.get("1.0", END)))
        file.add_separator()
        file.add_command(
            label="Exit",
            accelerator="Ctrl+Q",
            command=self._on_window_close,
        )
        self.bind("<Control-q>", lambda _: self._on_window_close())
        menu.add_cascade(menu=file, label="File")
        options = Menu(menu, tearoff=False)
        options.add_command(
            label="Settings",
            accelerator="Ctrl+.",
            command=self.settings
        )
        self.bind("<Control-period>", lambda _: self.settings())
        options.add_separator()
        options.add_command(
            label="Credits",
            command=self.credits
        )
        menu.add_cascade(menu=options, label="Options")
        self.config(menu=menu)

        text = ScrolledText(self, wrap=NONE, font=(self._settings["editor"]["font"],
                                                   self._settings["editor"]["font_size"]),
                            background=self._settings["editor"]["background"],
                            foreground=self._settings["editor"]["foreground"])
        engine.highlight(text, self._settings)
        text.bind("<KeyRelease>", lambda _: self._on_change(text.index(INSERT), status))
        text.bind("<Button 1>", lambda _: self._on_change(text.index(INSERT), status))
        text.bind("<Control-equal>", lambda _: self._increase_font(text))
        text.bind("<Control-minus>", lambda _: self._decrease_font(text))
        text.bind("<Tab>", lambda _: self._on_tab(text))
        text.place(relx=0, rely=0, relheight=.95, relwidth=1)

        status = Label(self, font=(self._settings["editor"]["font"], 14), text=f"{self.file if self.file else 'new'}")
        status.place(relx=0, rely=1, relheight=.05, anchor=SW)

        self.mainloop()


class Credits(Toplevel):

    def __init__(self, root: Tk, res: tuple, settings) -> None:
        super().__init__(root)
        self._settings = settings
        self.title("Credits")
        self.geometry(f"{res[0]}x{res[1]}")
        self.minsize(res[0], res[1])
        self.resizable(False, False)

    def open_repository(self) -> None:
        debug.log_info("event trigger: open_repository")
        webbrowser.open("https://github.com/marc-dantas/snake-editor/")

    def open_marcdantas(self):
        debug.log_info("event trigger: open_marcdantas")
        webbrowser.open("https://github.com/marc-dantas/")

    def open_kamaasoo(self):
        debug.log_info("event trigger: open_kamaasoo")
        webbrowser.open("https://github.com/Kamaasoo/")

    def draw(self) -> None:
        copy = Label(
            self, text="Copyright © 2024 Snake Editor - All Rights Reserved", font=("", 20))
        copy.place(relx=.5, rely=.1, anchor="center")
        author = Label(
            self, text="Developed and Designed by @marc-dantas and @Kamaasoo", font=("", 14))
        author.place(relx=.5, rely=.2, anchor="center")
        license = Label(
            self, text="This piece of software is fully open-source and licensed under the MIT License.", font=("", 12))
        license.place(relx=.5, rely=.3, anchor="center")

        marcdantas = Button(self, text="@marc-dantas",
                            font=("", 14), command=self.open_marcdantas)
        marcdantas.place(relx=.4, rely=.45, anchor="center")
        kmsz = Button(self, text="@Kamaasoo",
                      font=("", 14), command=self.open_kamaasoo)
        kmsz.place(relx=.6, rely=.45, anchor="center")

        contrib = Button(self, text="Snake Editor on Github",
                         font=("", 14), command=self.open_repository)
        contrib.place(relx=.5, rely=.9, anchor="center")

        self.mainloop()


class Settings(Toplevel):

    def __init__(self, root: Tk, res: tuple, settings, file: str) -> None:
        super().__init__(root)
        self._settings = settings
        self.file = file
        self.title("Settings")
        self.geometry(f"{res[0]}x{res[1]}")
        self.minsize(res[0], res[1])

    def apply(self, new_settings: str) -> None:
        self.destroy()
        engine.save_file(self.file, new_settings)
        debug.log_info("configuration file saved")
        engine.message(
            "To see the configuration changes, please restart Snake Editor")

    def draw(self) -> None:
        text = ScrolledText(self, font=(
            self._settings["editor"]["font"], self._settings["editor"]["font_size"]))
        text.insert(END, engine.json.dumps(self._settings, indent=2))

        text.place(relx=0, rely=0, relwidth=1, relheight=.9)

        apply = Button(self, text="Apply",
                       command=lambda: self.apply(text.get("1.0", END)))
        apply.place(relx=.0, rely=.9, relheight=.1, relwidth=1)
        self.mainloop()
