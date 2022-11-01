from .ReplacerInterface import ReplacerInterface
from settings import Settings

class ReplaceNumPrestazione(ReplacerInterface):
    
    STRING_TO_REPLACE = '{{num_prestazione}}'

    def __init__(self, numPrestazioni):
        super().__init__(ReplaceNumPrestazione.STRING_TO_REPLACE)
        self.numPrestazioni = numPrestazioni

    def handle(self, paragraph):
        if (self.canHandleRequest(paragraph)):
            paragraph.text = paragraph.text.replace(self.getStringToReplace(), str(Settings().getAndUpdateNumPrestazioni))
        else:
            super().handle(paragraph)