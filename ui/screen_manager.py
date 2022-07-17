from tkinter import PhotoImage, Tk

from ui.screens.chess_screen import ChessScreen
from ui.screens.start_screen import StartScreen
from ui.screens.end_screen import EndScreen
from ui.screens.statistic_screen import StatisticScreen
from ui.screens.setting_screen import SettingScreen
from ui.screens.manual_screen import ManualScreen
from ui.images import ImageHandler

class ScreenManager:
    def __init__(self):
        self.window = Tk()
        self.window.resizable(width=False, height=False)
        iconImage = PhotoImage(file = 'IMG/icon.png')
        self.window.iconphoto(False, iconImage)
        self.window.title("aChess")
        self.window.geometry("1000x800")

        # Jeder Scren wird mit ROUTENAME verknüpft
        self._screens = {StartScreen.ROUTENAME: StartScreen(self),
                         ChessScreen.ROUTENAME: ChessScreen(self),
                         SettingScreen.ROUTENAME: SettingScreen(self),
                         EndScreen.ROUTENAME: EndScreen(self),
                         ManualScreen.ROUTENAME: ManualScreen(self),
                         StatisticScreen.ROUTENAME: StatisticScreen(self)}
        self._currentScreenRouteName = None
        self.imageHandler = ImageHandler()

    def start(self):
        self.navigate("/") # Startmenü wird als erstes geöffnet
        self.window.mainloop()

    def navigate(self, screenRouteName, arg=None):
        # wechsel den Screen
        # kann Argumente an die Screen weitergeben
        if(self._currentScreenRouteName != None):
            self._screens[self._currentScreenRouteName].clear()
        if arg == None:
            self._screens[screenRouteName].initBuild()
        else:
            self._screens[screenRouteName].initBuild(arg)
        self._currentScreenRouteName = screenRouteName
