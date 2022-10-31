from .ReplacerInterface import ReplacerInterface
from settings import getAndUpdateNumPrestazioni

class ReplaceNumPrestazione(ReplacerInterface):
    
    STRING_TO_REPLACE = '{{num_prestazione}}'

    def __init__(self, numPrestazioni):
        super().__init__()
        self.numPrestazioni = numPrestazioni

    def handle(self, paragraph):
        if (self.canHandleRequest(paragraph)):
            paragraph.text = paragraph.text.replace(ReplaceNumPrestazione.STRING_TO_REPLACE, str(getAndUpdateNumPrestazioni()))
        else:
            super().handle(paragraph)

    def canHandleRequest(self, paragraph):
        return (ReplaceNumPrestazione.STRING_TO_REPLACE in paragraph.text)