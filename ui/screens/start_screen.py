from tkinter import Label, Button, font

from ui.screen import Screen


class StartScreen(Screen):
    ROUTENAME = "/"

    def clickButton(self):
        self._screenManager.navigate("/chess")

    def initBuild(self):
        LabelGame = Label(text="Ein Schach",
                          fg="#265B78")
        LabelGame["font"] = font.Font(family='Arial', size=70, weight='bold')
        LabelGame.place(anchor="center", relx=0.5, rely=0.2)

        ButtonPlay = Button(text="Spielen",
                            command=self.clickButton,
                            bg="#265B78",
                            activebackground="#265B78",
                            fg="#ffffff",
                            activeforeground="#ffffff",
                            borderwidth=0)
        ButtonPlay["font"] = font.Font(family='Arial', size=20, weight='bold')
        ButtonPlay.place(anchor="center", relx=0.5,
                         rely=0.5, width=210, height=80)

    def clear(self):
        print("lol")
