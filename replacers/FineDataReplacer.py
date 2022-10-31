from .ReplacerInterface import ReplacerInterface
from settings import getAndUpdateNumPrestazioni

class ReplaceNumPrestazione(ReplacerInterface):
    
    STRING_TO_REPLACE = '{{data_inizio}}'

    def __init__(self, mese):
        super().__init__(ReplaceNumPrestazione.STRING_TO_REPLACE)
        self.mese = mese

    def handle(self, paragraph):
        if (self.canHandleRequest(paragraph)):
            paragraph.text = paragraph.text.replace(self.getStringToReplace(), str(getAndUpdateNumPrestazioni()))
        else:
            super().handle(paragraph)

    def canHandleRequest(self, paragraph):
        return (self.getStringToReplace() in paragraph.text)