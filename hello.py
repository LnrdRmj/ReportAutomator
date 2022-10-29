import docx
import shutil

from replacers.ReplacePay import ReplacePay
from replacers.ReplacerBuilder import ReplacerBuilder

# templateNotulaFileName = 'Notula template.docx'
templateNotulaFileName = 'test.docx'
newNotulaFileName = 'demo.docx'

shutil.copy(templateNotulaFileName, newNotulaFileName)
notula = docx.Document(newNotulaFileName)

replacerChain = ReplacerBuilder().defaultChain()

for paragraph in notula.paragraphs:
    replacerChain.handle(paragraph)

notula.save(newNotulaFileName)
