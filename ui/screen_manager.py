from tkinter import Tk

from ui.screens.chess_screen import ChessScreen
from ui.screens.start_screen import StartScreen


class ScreenManager:
    def __init__(self):
        self.window = Tk()
        self.window.resizable(width=False, height=False)
        self.window.geometry("1000x800")

        self._screens = {StartScreen.ROUTENAME: StartScreen(self),
                         ChessScreen.ROUTENAME: ChessScreen(self), }
        self._currentScreenRouteName = None

    def start(self):
        self.navigate("/")
        self.window.mainloop()

    def navigate(self, screenRouteName):
        self._currentScreenRouteName = screenRouteName
        if(self._currentScreenRouteName != None):
            self._screens[self._currentScreenRouteName].clear()
        self._screens[screenRouteName].initBuild()
        self._currentScreenRouteName = screenRouteName
