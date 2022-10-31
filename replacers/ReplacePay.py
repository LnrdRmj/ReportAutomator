from .ReplacerInterface import ReplacerInterface

class ReplacePay(ReplacerInterface):
    
    STRING_TO_REPLACE = '{{paga}}'

    def __init__(self, pay):
        super().__init__(ReplacePay.STRING_TO_REPLACE)
        self.pay = pay

    def handle(self, paragraph):
        if (self.canHandleRequest(paragraph)):
            paragraph.text = paragraph.text.replace(self.getStringToReplace(), self.formatPay())
        else:
            super().handle(paragraph)

    def canHandleRequest(self, paragraph):
        return (self.getStringToReplace() in paragraph.text)

    def formatPay(self):
        return "€{:.2f}".format(int(self.pay))