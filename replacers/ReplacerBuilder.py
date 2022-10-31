from .ReplaceNumPrestazione import ReplaceNumPrestazione
from .ReplacePay import ReplacePay
from .ReplaceFineData import ReplaceFineData
from .ReplaceInizioData import ReplaceInizioData
from .ReplaceDataOdierna import ReplaceDataOdierna
from .ReplaceRitenuta import ReplaceRitenuta
from .ReplaceTheoreticalPay import ReplaceTheoreticalPay, ReplacerInterface

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

    def addDataOdierna(self):
        self.replacers.append(ReplaceDataOdierna())
        return self

    def addRitenuta(self, ritenuta):
        self.replacers.append(ReplaceRitenuta(ritenuta))
        return self

    def addTheoreticalPay(self, theoreticalPay):
        self.replacers.append(ReplaceTheoreticalPay(theoreticalPay))
        return self

    def defaultChain(self, pay, month, numPrestazioni, theoreticalPay, ritenuta):
        return self\
            .addReplaceNumPrestazione(numPrestazioni)\
            .addReplacePay(pay)\
            .addFineData(month)\
            .addInizioData(month)\
            .addDataOdierna()\
            .addTheoreticalPay(theoreticalPay)\
            .addRitenuta(ritenuta)\
            .build()
            