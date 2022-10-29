from .ReplacerInterface import ReplacerInterface

class ReplaceNumPrestazione(ReplacerInterface):
    
    STRING_TO_REPLACE = '{{num_prestazione}}'

    def __init__(self):
        super().__init__()

    def handle(self, paragraph):
        if (self.canHandleRequest(paragraph)):
            paragraph.text = paragraph.text.replace(ReplaceNumPrestazione.STRING_TO_REPLACE, 'num_prestazione')
        else:
            super().handle(paragraph)

    def canHandleRequest(self, paragraph):
        return (ReplaceNumPrestazione.STRING_TO_REPLACE in paragraph.text)