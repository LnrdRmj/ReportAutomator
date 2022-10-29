from .ReplaceNumPrestazione import ReplaceNumPrestazione
from .ReplacePay import ReplacePay

class ReplacerBuilder:

    def __init__(self):
        self.replacers = []

    def build(self):

        for i, replacer in enumerate(self.replacers[:-1]):
            self.replacers[i].setNext(self.replacers[i + 1])

        return self.replacers[0]

    def addReplaceNumPrestazione(self):
        self.replacers.append(ReplaceNumPrestazione())
        return self
    
    def addReplacePay(self):
        self.replacers.append(ReplacePay())
        return self

    def defaultChain(self):
        return self.addReplaceNumPrestazione().addReplacePay().build()
            