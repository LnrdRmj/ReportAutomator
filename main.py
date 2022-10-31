import docx
import shutil

from replacers.ReplacerBuilder import ReplacerBuilder
from settings import loadSettings, NUM_PRESTAZIONI

pay = 0
month = 0
ritenuta = 0
theoreticalPay = 0

def getData():
    global pay
    global month
    global ritenuta
    global theoreticalPay
    pay = int(input("Quanto hai guadagnato? "))
    month = int(input("Che mese? (input da 1 a 12) "))
    # pay = 300
    # month = 10
    theoreticalPay = pay / (1 - 20 / 100) # pay is theoretical pay - 20% 
    ritenuta = theoreticalPay - pay

templateNotulaFileName = 'Notula template.docx'
# templateNotulaFileName = 'test.docx'
newNotulaFileName = 'demo.docx'

shutil.copy(templateNotulaFileName, newNotulaFileName)
notula = docx.Document(newNotulaFileName)

settings = loadSettings()
getData()

replacerChain = ReplacerBuilder().defaultChain(pay, month, settings[NUM_PRESTAZIONI], theoreticalPay, ritenuta)

for paragraph in notula.paragraphs:
    # print(paragraph.text)
    # print('-----')
    replacerChain.handle(paragraph)
    print(paragraph.text)
    print('-----')

notula.save(newNotulaFileName)
