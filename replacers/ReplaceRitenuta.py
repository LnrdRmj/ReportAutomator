from calendar import month
from .ReplacerInterface import ReplacerInterface

class ReplaceRitenuta(ReplacerInterface):
    
    STRING_TO_REPLACE = '{{ritenuta}}'

    def __init__(self, ritenuta):
        super().__init__(ReplaceRitenuta.STRING_TO_REPLACE)
        self.ritenuta = ritenuta

    def handle(self, paragraph):
        if (self.canHandleRequest(paragraph)):
            paragraph.text = paragraph.text.replace(self.getStringToReplace(), self.formatPay())
        else:
            super().handle(paragraph)

    def formatPay(self):
        return "€{:.2f}".format(int(self.ritenuta))

    