from calendar import month
from .ReplacerInterface import ReplacerInterface

from datetime import datetime
from dateutil.relativedelta import relativedelta

class ReplaceInizioData(ReplacerInterface):
    
    STRING_TO_REPLACE = '{{data_inizio}}'

    def __init__(self, month):
        super().__init__(ReplaceInizioData.STRING_TO_REPLACE)
        self.month = month

    def startMonthDate(self):
        result = self.getFirstDayOfMonth().strftime('%d/%m/%Y')
        return result

    def getFirstDayOfMonth(self):
        return datetime.today() + relativedelta(month=self.month, day=1)

    def handle(self, paragraph):
        if (self.canHandleRequest(paragraph)):
            paragraph.text = paragraph.text.replace(self.getStringToReplace(), self.startMonthDate())
        else:
            super().handle(paragraph)

    