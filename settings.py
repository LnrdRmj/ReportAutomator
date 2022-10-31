import json
import os

SETTINGS_FILE_NAME = 'settings.json'
NUM_PRESTAZIONI = 'NUM_PRESTAZIONI'

def askNumPrestazioni():
    numPrestazioni = input('Quante prestazioni hai fatto? [0] ')
    return 0 if numPrestazioni == '' else numPrestazioni

def getAndUpdateNumPrestazioni():
    settings = loadSettings()
    numPrestazioni = settings[NUM_PRESTAZIONI]
    settings[NUM_PRESTAZIONI] = settings[NUM_PRESTAZIONI] + 1
    with open(SETTINGS_FILE_NAME, "w") as f:
        json.dump(settings, f, indent=4)
    return numPrestazioni

def createSettingsFile():
    print('Nessuna configurazione trovata')
    print('Ne creo uno nuovo')
    numPrestazioni = askNumPrestazioni()

    settings = {
        NUM_PRESTAZIONI: numPrestazioni
    }

    with open(SETTINGS_FILE_NAME, "a") as f:
        json.dump(settings, f, indent=4)

def loadSettings():

    if (not os.path.isfile(SETTINGS_FILE_NAME)):
        createSettingsFile()

    with open(SETTINGS_FILE_NAME, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    loadSettings()