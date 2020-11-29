import pandas as pd
from pathlib import Path


class Database:
    def __init__(self, databaseFileName):
        self._data = None
        dirpath = Path(__file__).cwd().as_posix()
        self.dbFileURL = dirpath + databaseFileName
        self._readFile()

    def addRecord(self, typeOfGame, time, rounds, winner):
        new_row = {'typeOfGame': str(typeOfGame),
                   'time': str(time),
                   'rounds': str(rounds),
                   'winner': str(winner),
                   }
        self._data = self._data.append(new_row, ignore_index=True)
        self._saveFile()

    @property
    def records(self):
        records = []
        for record in self._data.values:
            recordMap = {'typeOfGame':  record[0],
                         'time':  record[1],
                         'rounds':  record[2],
                         'winner':  record[3],
                         }
            records.append(recordMap)
        return records

    def _saveFile(self):
        try:
            self._data.to_csv(self.dbFileURL, encoding='utf-8', index=False)
        except:
            print("database.py: Error writing to the db file: " + self.dbFileURL)

    def _readFile(self):
        try:
            self._data: pd.DataFrame = pd.read_csv(self.dbFileURL)
        except:
            print("database.py: Error reading the db file: " + self.dbFileURL)
