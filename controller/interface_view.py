from abc import ABC, abstractmethod


class IView(ABC):
    @abstractmethod
    def update(self):
        # Regt die UI zum Updaten ihres Inhaltes auf
        return
