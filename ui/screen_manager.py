from tkinter import Tk

from ui.screens.chess_screen import ChessScreen
from ui.screens.start_screen import StartScreen
from ui.screens.end_screen import EndScreen
from ui.screens.statistic_screen import StatisticScreen
from ui.screens.setting_screen import SettingScreen
from ui.images import ImageHandler

class ScreenManager:
    def __init__(self):
        self.window = Tk()
        self.window.resizable(width=False, height=False)
        self.window.geometry("1000x800")

        self._screens = {StartScreen.ROUTENAME: StartScreen(self),
                         ChessScreen.ROUTENAME: ChessScreen(self),
                         SettingScreen.ROUTENAME: SettingScreen(self),
                         EndScreen.ROUTENAME: EndScreen(self, "Schwarz hat gewonnen"),
                         StatisticScreen.ROUTENAME: StatisticScreen(self)}
        self._currentScreenRouteName = None
        self.imageHandler = ImageHandler()

    def start(self):
        self.navigate("/end")
        self.window.mainloop()

    def navigate(self, screenRouteName, arg=None):
        if(self._currentScreenRouteName != None):
            self._screens[self._currentScreenRouteName].clear()
        if arg == None:
            self._screens[screenRouteName].initBuild()
        else:
            self._screens[screenRouteName].initBuild(arg)
        self._currentScreenRouteName = screenRouteName
