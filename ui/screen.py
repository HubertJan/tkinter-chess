from abc import ABC, abstractmethod


""" Basisklasse abstracte Klasse für jeden Screen im Programm """
class Screen(ABC):
    def __init__(self, screenManager):
        """Every Screen has access to the ScreenManager that it got called by so that it can use the ScreenManager.navigate() to change Screen.
        """
        self._screenManager = screenManager

    @property
    @abstractmethod
    def ROUTENAME(self):
        """Use to call the Screen in ScreenManager through navigate
        """
        pass

    @abstractmethod
    def initBuild(self):
        """Use to build the Screen if you navigate to the Screen
        """
        pass

    @abstractmethod
    def clear(self):
        """Use to clear the Screen if you navigate to a different Screen
        """
        pass
    
    
    @property
    def _window(self):
        """Can be used as a shortcut to access window property of ScreenManager in _screenManager
        return self._screenManager.window
