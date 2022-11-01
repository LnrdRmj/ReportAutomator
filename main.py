from asyncio.windows_events import NULL
import docx
import shutil
import subprocess
import pathlib
from datetime import datetime
from dateutil.relativedelta import relativedelta

from replacers.ReplacerBuilder import ReplacerBuilder
from settings import loadSettings, NUM_PRESTAZIONI
import settings

pay = 0
month = 0
ritenuta = 0
theoreticalPay = 0

options = loadSettings()

def askMonth():

    global options

    month = options[settings.PREVIOUS_MONTH]
    if (month != NULL):
        monthPrediction = (month + 1) % 12
        answer = input(f"Il mese della rendicontazione è {monthPrediction}? [Y/month] ")

        if (answer == '' or answer == 'Y'):
            return monthPrediction
        else:
            return int(answer)

    return int(input("Che mese? (input da 1 a 12) "))


def getData():
    global pay
    global month
    global ritenuta
    global theoreticalPay
    pay = int(input("Quanto hai guadagnato? "))
    month = askMonth()
    # pay = 300
    # month = 10
    theoreticalPay = pay / (1 - 20 / 100) # pay is theoretical pay - 20% 
    ritenuta = theoreticalPay - pay

templateNotulaFileName = 'template/Notula template.docx'

getData()

# templateNotulaFileName = 'template/test.docx'
newNotulaFileName = (datetime.today() + relativedelta(month=month)).strftime('%B %Y')
newNotulaFilePath = f'output\{newNotulaFileName}.docx'
shutil.copy(templateNotulaFileName, newNotulaFilePath)
notula = docx.Document(newNotulaFilePath)

replacerChain = ReplacerBuilder().defaultChain(pay, month, options[NUM_PRESTAZIONI], theoreticalPay, ritenuta)

for paragraph in notula.paragraphs:
    # print(paragraph.text)
    # print('-----')
    replacerChain.handle(paragraph)
    # print(paragraph.text)
    # print('-----')

notula.save(newNotulaFilePath)

# print(str(pathlib.Path().resolve()) + "\\" + newNotulaFileName)
newNotulaFilePath = '\\' + newNotulaFilePath
subprocess.Popen(fr'explorer /select,"{str(pathlib.Path().resolve()) + "" + newNotulaFilePath}"')