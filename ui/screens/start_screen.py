from tkinter import Label, Button, font

from ui.screen import Screen


class StartScreen(Screen):
    ROUTENAME = "/"

    def clickPlay(self):
        self._screenManager.navigate("/setting")

    def clickStats(self):
        self._screenManager.navigate("/stats")

    def clickManual(self):
        self._screenManager.navigate("/manual")

    def initBuild(self):
        self.LabelGame = Label(text="aChess",
                               fg="#265B78")
        self.LabelGame["font"] = font.Font(
            family='Arial', size=70, weight='bold')
        self.LabelGame.place(anchor="center", relx=0.5, rely=0.2)

        self.ButtonPlay = Button(text="Spielen",
                                 command=self.clickPlay,
                                 bg="#265B78",
                                 activebackground="#265B78",
                                 fg="#ffffff",
                                 activeforeground="#ffffff",
                                 borderwidth=0)
        self.ButtonPlay["font"] = font.Font(
            family='Arial', size=20, weight='bold')
        self.ButtonPlay.place(anchor="center", relx=0.5,
                              rely=0.4, width=210, height=80)

        self.buttonStats = Button(text="Letzte Spiele",
                                  command=self.clickStats,
                                  bg="#265B78",
                                  activebackground="#265B78",
                                  fg="#ffffff",
                                  activeforeground="#ffffff",
                                  borderwidth=0)
        self.buttonStats["font"] = font.Font(
            family='Arial', size=20, weight='bold')
        self.buttonStats.place(anchor="center", relx=0.5,
                               rely=0.6, width=210, height=80)

        self.buttonManual = Button(text="Anleitung",
                                   command=self.clickManual,
                                   bg="#265B78",
                                   activebackground="#265B78",
                                   fg="#ffffff",
                                   activeforeground="#ffffff",
                                   borderwidth=0)
        self.buttonManual["font"] = font.Font(
            family='Arial', size=20, weight='bold')
        self.buttonManual.place(anchor="center", relx=0.5,
                                rely=0.8, width=210, height=80)

    def clear(self):
        self.LabelGame.destroy()
        self.ButtonPlay.destroy()
