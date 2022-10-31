import docx
import shutil

from replacers.ReplacerBuilder import ReplacerBuilder
from settings import loadSettings, NUM_PRESTAZIONI

pay = 0
month = 0

def getData():
    global pay
    global month
    # pay = input("Quanto hai guadagnato? ")
    # month = input("Che mese? (input da 1 a 12) ")
    pay = 300
    month = 10

# templateNotulaFileName = 'Notula template.docx'
templateNotulaFileName = 'test.docx'
newNotulaFileName = 'demo.docx'

shutil.copy(templateNotulaFileName, newNotulaFileName)
notula = docx.Document(newNotulaFileName)

settings = loadSettings()
getData()

replacerChain = ReplacerBuilder().defaultChain(pay, month, settings[NUM_PRESTAZIONI])

for paragraph in notula.paragraphs:
    # print(paragraph.text)
    # print('-----')
    replacerChain.handle(paragraph)
    print(paragraph.text)
    print('-----')

notula.save(newNotulaFileName)
