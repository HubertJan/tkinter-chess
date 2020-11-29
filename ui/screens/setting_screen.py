from tkinter import Label, Button, font, Frame

from ui.screen import Screen


class SettingScreen(Screen):
    ROUTENAME = "/setting"

    def backButton(self):
        self._screenManager.navigate("/")

    def clickButton(self):
        self._screenManager.navigate("/chess", self.time)

    def clickTimeSelect(self, index):
        if self.time == None:
            self.ButtonStart.config(state="normal")

        self.time = self.INDEX_TIME_LIST[index]

        for buttonIndex in range(len(self.timeButtons)):
            if buttonIndex == index:
                self.timeButtons[buttonIndex].config(bg="#265B78", fg="#FFF",)
            else:
                self.timeButtons[buttonIndex].config(bg="#FFF", fg="#265B78",)

    def initBuild(self):
        self.time = None
        self.INDEX_TIME_LIST = [2, 600, 3600]
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


        img = self._screenManager.imageHandler.images["Back"]

        self.buttonBack = Button(
            command= self.backButton,
            master=self.frame, image= img,  borderwidth=0)
        self.buttonBack.place(anchor="center", relx=0.1,
                              rely=0.1, width=85, height=85)

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

        self.timeButtons = []
        self.timeButtons.append(Button(master=self.frame, text="1 min",
                                       bg="#fff",
                                       command=lambda: self.clickTimeSelect(0),
                                       activebackground="#fff",
                                       fg="#265B78",
                                       activeforeground="#265B78",
                                       borderwidth=0))

        self.timeButtons[0]["font"] = font.Font(
            family='Arial', size=40, weight='bold')
        self.timeButtons[0].place(anchor="center", relx=0.2,
                                  rely=0.62, width=190, height=110)

        self.timeButtons.append(Button(master=self.frame, text="10 min",
                                       bg="#fff",
                                       command=lambda: self.clickTimeSelect(1),
                                       activebackground="#fff",
                                       fg="#265B78",
                                       activeforeground="#265B78",
                                       borderwidth=0))

        self.timeButtons[1]["font"] = font.Font(
            family='Arial', size=40, weight='bold')
        self.timeButtons[1].place(anchor="center", relx=0.5,
                                  rely=0.62, width=190, height=110)

        self.timeButtons.append(Button(master=self.frame, text="60 min",
                                       command=lambda: self.clickTimeSelect(2),
                                       bg="#fff",
                                       activebackground="#fff",
                                       fg="#265B78",
                                       activeforeground="#265B78",
                                       borderwidth=0))

        self.timeButtons[2]["font"] = font.Font(
            family='Arial', size=40, weight='bold')
        self.timeButtons[2].place(anchor="center", relx=0.8,
                                  rely=0.62, width=190, height=110)

        self.ButtonStart = Button(master=self.frame, text="Starten",
                                  command=self.clickButton,
                                  bg="#265B78",
                                  activebackground="#265B78",
                                  fg="#ffffff",
                                  activeforeground="#ffffff",
                                  state="disabled",
                                  borderwidth=0)
        self.ButtonStart["font"] = font.Font(
            family='Arial', size=20, weight='bold')
        self.ButtonStart.place(anchor="center", relx=0.5,
                               rely=0.9, width=210, height=80)

    def clear(self):
        self.frame.destroy()
