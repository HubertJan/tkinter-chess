from tkinter import Label, Button, font, Frame

from ui.screen import Screen
from database import Database


class StatisticScreen(Screen):
    ROUTENAME = "/stats"

    def clickButton(self):
        self._screenManager.navigate("/stats")

    def backButton(self):
        self._screenManager.navigate("/")

    def createGameStatsFrame(self, time, gameRound, gameType, winner):
        lastGameFrame = Frame(
         master=self.frame, bg="#417D9E", width=840, height=150)

        timeText = round(int(time) / 60)
        gameRoundText = gameRound
        if gameType == 0:
            gameTypeText = "Spieler gegen Spieler"
        else:
            gameTypeText = "Spieler gegen Bot"

        LabelStats = Label(
            master=lastGameFrame, text=f'{gameTypeText} - {timeText} min - {gameRoundText} Runden', fg="#ffffff", bg="#417D9E")
        LabelStats["font"] = font.Font(family='Arial', size=20)
        LabelStats.place(anchor="center", relx=0.5, rely=0.2)

        if winner == "Unentschieden":
            winnerText = "Unentschieden"
        else:
            winnerText = winner + " hat gewonnen"

        LabelWin = Label(master=lastGameFrame,
                         text=winnerText, fg="#ffffff", bg="#417D9E")
        LabelWin["font"] = font.Font(family='Arial', size=40)
        LabelWin.place(anchor="center", relx=0.5, rely=0.6)

        return lastGameFrame

    def initBuild(self):
        self.database = Database("/records.csv")

        records = self.database.records

        self.frame = Frame(width=1000, height=800)
        self.frame.place(x=0, y=0)

        self.LabelEnd = Label(
            master=self.frame, text="Letzte Spiele", fg="#417D9E")
        self.LabelEnd["font"] = font.Font(
            family='Arial', size=50, weight='bold')
        self.LabelEnd.place(anchor="center", relx=0.5, rely=0.1)

        img = self._screenManager.imageHandler.images["Back"]
        self.buttonBack = Button(
            command=self.backButton,
            master=self.frame, image=img,  borderwidth=0)
        self.buttonBack.place(anchor="center", relx=0.1,
                              rely=0.1, width=85, height=85)

        if len(records) - 1 >= 0:
            record = records[len(records) - 1]
            lastGameFrame = self.createGameStatsFrame(record["time"], record["rounds"], record["typeOfGame"], record["winner"])
            lastGameFrame.place(anchor="center", relx=0.5, rely=0.35)

        if len(records) - 2 >= 0:
            record = records[len(records) - 2]
            lastGameFrame = self.createGameStatsFrame(record["time"], record["rounds"], record["typeOfGame"], record["winner"])
            lastGameFrame.place(anchor="center", relx=0.5, rely=0.55)
        if len(records) - 3 >= 0:
            record = records[len(records) - 3]
            lastGameFrame = self.createGameStatsFrame(record["time"], record["rounds"], record["typeOfGame"], record["winner"])
            lastGameFrame.place(anchor="center", relx=0.5, rely=0.75)
    def clear(self):
        self.frame.destroy()
