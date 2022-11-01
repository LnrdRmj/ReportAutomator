import json
import os

class Settings:

    SETTINGS_FILE_NAME = 'settings.json'
    NUM_PRESTAZIONI = 'NUM_PRESTAZIONI'
    PREVIOUS_MONTH = 'PREVIOUS_MONTH'

    def __init__(self):
        self.options = self.loadSettings()
    
    def loadSettings(self):

        if (not os.path.isfile(Settings.SETTINGS_FILE_NAME)):
            self.createSettingsFile()

        with open(Settings.SETTINGS_FILE_NAME, "r") as f:
            return json.load(f)

    def createSettingsFile(self):
        print('Nessuna configurazione trovata')
        print('Ne creo uno nuovo')
        numPrestazioni = self.askNumPrestazioni()

        settings = {
            Settings.NUM_PRESTAZIONI: numPrestazioni
        }

        with open(Settings.SETTINGS_FILE_NAME, "a") as f:
            json.dump(settings, f, indent=4)

    def saveMonth(self, month):
        self.options[Settings.PREVIOUS_MONTH] = month
        self.saveOptions()

    def saveOptions(self):
        with open(Settings.SETTINGS_FILE_NAME, "w") as f:
            json.dump(self.options, f, indent=4)

    def askNumPrestazioni(self):
        numPrestazioni = input('Quante prestazioni hai fatto? [0] ')
        return 0 if numPrestazioni == '' else numPrestazioni

    def getAndUpdateNumPrestazioni(self):
        settings = self.loadSettings()
        numPrestazioni = settings[Settings.NUM_PRESTAZIONI]
        settings[Settings.NUM_PRESTAZIONI] = settings[Settings.NUM_PRESTAZIONI] + 1
        with open(Settings.SETTINGS_FILE_NAME, "w") as f:
            json.dump(settings, f, indent=4)
        return numPrestazioni

if __name__ == "__main__":
    Settings()