from abc import ABC, abstractmethod


""" Basisklasse abstracte Klasse für jeden Screen im Programm """
class Screen(ABC):
    def __init__(self, screenManager):
        self._screenManager = screenManager

    @property
    @abstractmethod
    def ROUTENAME(self):
        #Genutzt um Screen per ScreenManager aufzurufen
        pass

    @abstractmethod
    def initBuild(self):
        #Gestartet, um Screen zu zeichnen
        pass

    @abstractmethod
    def clear(self):
        #Löscht den Screen, wenn ein neuer Screen aufgerufen werden soll
        pass

    @property
    def _window(self):
        #Gibt das Tk Window zurück, dass für jeden Screen im Programm genutzt wird.
        return self._screenManager.window
