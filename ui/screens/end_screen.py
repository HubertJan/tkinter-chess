from tkinter import Label, Button, font, Frame

from ui.screen import Screen


class EndScreen(Screen):
    ROUTENAME = "/end"

    def __init__(self, screenManager, text):
        super().__init__(screenManager)
        self.text = text

    def clickButton(self):
        self._screenManager.navigate("/")

    def initBuild(self):
        self.frame = Frame(width=1000, height=800)
        self.frame.place(x=0, y=0)

        self.LabelEnd = Label(master=self.frame, text=self.text, fg="#417D9E")
        self.LabelEnd["font"] = font.Font(family='Arial', size=50, weight='bold')
        self.LabelEnd.place(anchor="center", relx=0.5, rely=0.1)
        
        self.ButtonPlay = Button(
                            master=self.frame,
                            text="Zum Menü",
                            command=self.clickButton,
                            bg="#265B78",
                            activebackground="#265B78",
                            fg="#ffffff",
                            activeforeground="#ffffff",
                            borderwidth=0)
        self.ButtonPlay["font"] = font.Font(family='Arial', size=20, weight='bold')
        self.ButtonPlay.place(anchor="center", relx=0.5,
                         rely=0.5, width=210, height=80)

    def clear(self):
        self.frame.destroy()
