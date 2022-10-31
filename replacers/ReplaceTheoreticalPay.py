from calendar import month
from .ReplacerInterface import ReplacerInterface

class ReplaceTheoreticalPay(ReplacerInterface):
    
    STRING_TO_REPLACE = '{{paga_notula}}'

    def __init__(self, theoreticalPay):
        super().__init__(ReplaceTheoreticalPay.STRING_TO_REPLACE)
        self.theoreticalPay = theoreticalPay

    def handle(self, paragraph):
        if (self.canHandleRequest(paragraph)):
            paragraph.text = paragraph.text.replace(self.getStringToReplace(), self.formatPay())
        else:
            super().handle(paragraph)

    def formatPay(self):
        return "€{:.2f}".format(int(self.theoreticalPay))