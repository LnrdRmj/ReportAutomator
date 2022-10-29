from .ReplacerInterface import ReplacerInterface

class ReplacePay(ReplacerInterface):
    
    STRING_TO_REPLACE = '{{paga}}'

    def __init__(self):
        super().__init__()

    def handle(self, paragraph):
        if (self.canHandleRequest(paragraph)):
            paragraph.text = paragraph.text.replace(ReplacePay.STRING_TO_REPLACE, 'paga')
        else:
            super().handle(paragraph)

    def canHandleRequest(self, paragraph):
        return (ReplacePay.STRING_TO_REPLACE in paragraph.text)