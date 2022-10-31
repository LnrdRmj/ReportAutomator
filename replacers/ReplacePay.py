from .ReplacerInterface import ReplacerInterface

class ReplacePay(ReplacerInterface):
    
    STRING_TO_REPLACE = '{{paga}}'

    def __init__(self, pay):
        super().__init__()
        self.pay = pay

    def handle(self, paragraph):
        if (self.canHandleRequest(paragraph)):
            paragraph.text = paragraph.text.replace(ReplacePay.STRING_TO_REPLACE, self.formatPay())
        else:
            super().handle(paragraph)

    def canHandleRequest(self, paragraph):
        return (ReplacePay.STRING_TO_REPLACE in paragraph.text)

    def formatPay(self):
        return "€{:.2f}".format(int(self.pay))