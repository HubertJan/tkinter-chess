from abc import ABC, abstractmethod

class Screen(ABC):
  def __init__(self, screenManager):
    self._screenManager = screenManager
  
  @property
  @abstractmethod
  def ROUTENAME(self):
    pass
  
  @abstractmethod
  def initBuild(self):
    pass
  
  @abstractmethod
  def clear(self):
    pass
  
  @property
  def _window(self):
    return self._screenManager.window
  