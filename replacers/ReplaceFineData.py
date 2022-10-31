from calendar import month
from .ReplacerInterface import ReplacerInterface

from datetime import datetime
from dateutil.relativedelta import relativedelta

class ReplaceFineData(ReplacerInterface):
    
    STRING_TO_REPLACE = '{{data_fine}}'

    def __init__(self, month):
        super().__init__(ReplaceFineData.STRING_TO_REPLACE)
        self.month = month

    def startMonthDate(self):
        result = self.getLastDayOfMonth().strftime('%d/%m/%Y')
        return result

    def getLastDayOfMonth(self):
        today = datetime.today() + relativedelta(month=self.month)
        firstDayOfNextMonth = today + relativedelta(months=1, day=1)
        lastDayOfMonth =  firstDayOfNextMonth - relativedelta(days=1)
        return lastDayOfMonth

    def handle(self, paragraph):
        if (self.canHandleRequest(paragraph)):
            paragraph.text = paragraph.text.replace(self.getStringToReplace(), self.startMonthDate())
        else:
            super().handle(paragraph)

    