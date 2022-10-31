from .ReplaceNumPrestazione import ReplaceNumPrestazione
from .ReplacePay import ReplacePay
from .ReplaceFineData import ReplaceFineData
from .ReplaceInizioData import ReplaceInizioData

class ReplacerBuilder:

    def __init__(self):
        self.replacers = []

    def build(self):

        for i, replacer in enumerate(self.replacers[:-1]):
            self.replacers[i].setNext(self.replacers[i + 1])

        return self.replacers[0]

    def addReplaceNumPrestazione(self, numPrestazioni):
        self.replacers.append(ReplaceNumPrestazione(numPrestazioni))
        return self
    
    def addReplacePay(self, pay):
        self.replacers.append(ReplacePay(pay))
        return self

    def addFineData(self, month):
        self.replacers.append(ReplaceFineData(month))
        return self
    
    def addInizioData(self, month):
        self.replacers.append(ReplaceInizioData(month))
        return self

    def defaultChain(self, pay, month, numPrestazioni):
        return self\
            .addReplaceNumPrestazione(numPrestazioni)\
            .addReplacePay(pay)\
            .addFineData(month)\
            .addInizioData(month)\
            .build()
            