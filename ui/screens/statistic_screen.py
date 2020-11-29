from tkinter import Label, Button, font, Frame

from ui.screen import Screen


class StatisticScreen(Screen):
    ROUTENAME = "/stats"

    def clickButton(self):
        self._screenManager.navigate("/stats")

    def initBuild(self):
        self.frame = Frame(width=1000, height=800)
        self.frame.place(x=0, y=0)

        self.LabelEnd = Label(master=self.frame, text="Letzte Spiele", fg="#417D9E")
        self.LabelEnd["font"] = font.Font(family='Arial', size=50, weight='bold')
        self.LabelEnd.place(anchor="center", relx=0.5, rely=0.1)
        
        
        lastGameFrame = Frame(master=self.frame, bg="#417D9E", width=840, height=150)
        lastGameFrame.place(anchor="center", relx=0.5, rely=0.3)
        
        LabelStats = Label(master=lastGameFrame, text="1 v 1 - 15 min - 39 Runden", fg="#ffffff", bg="#417D9E")
        LabelStats["font"] = font.Font(family='Arial', size=20)
        LabelStats.place(anchor="center", relx=0.5, rely=0.2)
        
        LabelWin = Label(master=lastGameFrame, text="Schwarz hat gewonnen", fg="#ffffff", bg="#417D9E")
        LabelWin["font"] = font.Font(family='Arial', size=40)
        LabelWin.place(anchor="center", relx=0.5, rely=0.6)
        
        lastGameFrame = Frame(master=self.frame,bg="#417D9E", width=840, height=150)
        lastGameFrame.place(anchor="center", relx=0.5, rely=0.55)
        
        LabelStats = Label(master=lastGameFrame, text="1 v 1 - 5 min - 10 Runden", fg="#ffffff", bg="#417D9E")
        LabelStats["font"] = font.Font(family='Arial', size=20)
        LabelStats.place(anchor="center", relx=0.5, rely=0.2)
        
        LabelWin = Label(master=lastGameFrame, text="Weiß - hat gewonnen", fg="#ffffff", bg="#417D9E")
        LabelWin["font"] = font.Font(family='Arial', size=40)
        LabelWin.place(anchor="center", relx=0.5, rely=0.6)
        
        lastGameFrame = Frame(master=self.frame, bg="#417D9E", width=840, height=150)
        lastGameFrame.place(anchor="center", relx=0.5, rely=0.8)
        
        LabelStats = Label(master=lastGameFrame, text="1 v 1 - 10 min - 21 Runden", fg="#ffffff", bg="#417D9E")
        LabelStats["font"] = font.Font(family='Arial', size=20)
        LabelStats.place(anchor="center", relx=0.5, rely=0.2)
        
        LabelWin = Label(master=lastGameFrame, text="Schwarz hat gewonnen", fg="#ffffff", bg="#417D9E")
        LabelWin["font"] = font.Font(family='Arial', size=40)
        LabelWin.place(anchor="center", relx=0.5, rely=0.6)

    def clear(self):
        self.frame.destroy()
