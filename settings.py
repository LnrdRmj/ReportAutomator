import json
import os
import easygui
import time

class Settings:

    SETTINGS_FILE_NAME = 'settings.json'

    NUM_PRESTAZIONI = 'NUM_PRESTAZIONI'
    PREVIOUS_MONTH = 'PREVIOUS_MONTH'
    OUTPUT_FOLDER = 'OUTPUT_FOLDERS'

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
        outputFolder = self.askOutputFolder()

        settings = {
            Settings.NUM_PRESTAZIONI: numPrestazioni,
            Settings.OUTPUT_FOLDER: outputFolder
        }

        with open(Settings.SETTINGS_FILE_NAME, "a") as f:
            json.dump(settings, f, indent=4)

    def saveMonth(self, month):
        self.options[Settings.PREVIOUS_MONTH] = month
        self.saveOptions()

    def getMonth(self):
        return self.options.get(Settings.PREVIOUS_MONTH)

    def saveOptions(self):
        with open(Settings.SETTINGS_FILE_NAME, "w") as f:
            json.dump(self.options, f, indent=4)

    def askNumPrestazioni(self):
        numPrestazioni = input('Quante prestazioni hai fatto? [0] ')
        return 0 if numPrestazioni == '' else numPrestazioni

    def askOutputFolder(self):
        print('Scegli dove salvare le rendicontazioni (aspetta un secondo)')
        time.sleep(1)
        outputFolder = easygui.diropenbox()
        return outputFolder

    def setNumPrestazioni(self, numPrestazioni):
        self.options[Settings.NUM_PRESTAZIONI] = numPrestazioni
        self.saveOptions()

    def getNumPrestazioni(self):
        return int(self.options.get(Settings.NUM_PRESTAZIONI))

    def getAndUpdateNumPrestazioni(self):
        numPrestazioni = self.getNumPrestazioni()
        self.setNumPrestazioni(numPrestazioni + 1)
        return numPrestazioni

    def getOutputFoler(self):
        return self.options.get(Settings.OUTPUT_FOLDER)

    def saveOutpuFolder(self, outputFolder):
        self.options[Settings.OUTPUT_FOLDER] = outputFolder
        self.loadSettings()

if __name__ == "__main__":
    Settings()