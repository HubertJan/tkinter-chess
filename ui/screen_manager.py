from tkinter import Tk

from ui.screens.main_screen import MainScreen
from ui.screens.start_screen import StartScreen

class ScreenManager:
  def __init__(self):
    self.window = Tk()
    self.window.resizable(width=False, height=False)
    self.window.geometry("1000x800")

    self._screens = {StartScreen.ROUTENAME: StartScreen(self),}
    self._currentScreenRouteName = None

  def navigate(self,screenRouteName):
    self._currentScreenRouteName = screenRouteName
    if(self._currentScreenRouteName != None):
      self._screens[self._currentScreenRouteName].clear()
    self._screens[screenRouteName].initBuild()
    self._currentScreenRouteName = screenRouteName
  
    