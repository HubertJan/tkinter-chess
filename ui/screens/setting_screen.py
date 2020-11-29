from tkinter import Label, Button, font, Frame

from ui.screen import Screen


class SettingScreen(Screen):
    ROUTENAME = "/setting"

    def clickButton(self):
        self._screenManager.navigate("/chess", self.time)

    def initBuild(self):
        self.time = 60
        self.frame = Frame(width=1000, height=800)
        self.frame.place(x=0, y=0)
        LabelCreate = Label(master=self.frame,
                            text="Spiel erstellen", fg="#417D9E")
        LabelCreate["font"] = font.Font(family='Arial', size=50, weight='bold')
        LabelCreate.place(anchor="center", relx=0.5, rely=0.1)

        LabelPlayer = Label(master=self.frame,
                            text="Spieleranzahl", fg="#000000")
        LabelPlayer["font"] = font.Font(family='Arial', size=30)
        LabelPlayer.place(anchor="center", relx=0.5, rely=0.2)

        ButtonPlayer1 = Button(master=self.frame, text="1",
                               bg="#fff",
                               activebackground="#fff",
                               fg="#265B78",
                               activeforeground="#265B78",
                               borderwidth=0)

        ButtonPlayer1["font"] = font.Font(
            family='Arial', size=50, weight='bold')
        ButtonPlayer1.place(anchor="center", relx=0.39,
                            rely=0.32, width=110, height=110)

        ButtonPlayer2 = Button(master=self.frame, text="2",
                               bg="#fff",
                               activebackground="#fff",
                               fg="#265B78",
                               activeforeground="#265B78",
                               borderwidth=0)

        ButtonPlayer2["font"] = font.Font(
            family='Arial', size=50, weight='bold')
        ButtonPlayer2.place(anchor="center", relx=0.61,
                            rely=0.32, width=110, height=110)

        LabelTime = Label(master=self.frame, text="Zeitlimit", fg="#000000")
        LabelTime["font"] = font.Font(family='Arial', size=30)
        LabelTime.place(anchor="center", relx=0.5, rely=0.5)

        ButtonMin5 = Button(master=self.frame, text="5 min",
                            bg="#fff",
                            activebackground="#fff",
                            fg="#265B78",
                            activeforeground="#265B78",
                            borderwidth=0)

        ButtonMin5["font"] = font.Font(family='Arial', size=40, weight='bold')
        ButtonMin5.place(anchor="center", relx=0.2,
                         rely=0.62, width=190, height=110)

        ButtonMin15 = Button(master=self.frame, text="15 min",
                             bg="#fff",
                             activebackground="#fff",
                             fg="#265B78",
                             activeforeground="#265B78",
                             borderwidth=0)

        ButtonMin15["font"] = font.Font(family='Arial', size=40, weight='bold')
        ButtonMin15.place(anchor="center", relx=0.5,
                          rely=0.62, width=190, height=110)

        ButtonMinAndere = Button(master=self.frame, text="... min",
                                 bg="#fff",
                                 activebackground="#fff",
                                 fg="#265B78",
                                 activeforeground="#265B78",
                                 borderwidth=0)

        ButtonMinAndere["font"] = font.Font(
            family='Arial', size=40, weight='bold')
        ButtonMinAndere.place(anchor="center", relx=0.8,
                              rely=0.62, width=190, height=110)

        ButtonStart = Button(master=self.frame, text="Starten",
                             command=self.clickButton,
                             bg="#265B78",
                             activebackground="#265B78",
                             fg="#ffffff",
                             activeforeground="#ffffff",
                             borderwidth=0)
        ButtonStart["font"] = font.Font(family='Arial', size=20, weight='bold')
        ButtonStart.place(anchor="center", relx=0.5,
                          rely=0.9, width=210, height=80)

    def clear(self):
        self.frame.destroy()
