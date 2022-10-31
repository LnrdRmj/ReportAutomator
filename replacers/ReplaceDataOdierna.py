from calendar import month
from .ReplacerInterface import ReplacerInterface

from datetime import datetime
from dateutil.relativedelta import relativedelta

class ReplaceDataOdierna(ReplacerInterface):
    
    STRING_TO_REPLACE = '{{data_odierna}}'

    def __init__(self):
        super().__init__(ReplaceDataOdierna.STRING_TO_REPLACE)
        self.month = month

    def startMonthDate(self):
        result = self.getFirstDayOfMonth().strftime('%d/%m/%Y')
        return result

    def getFirstDayOfMonth(self):
        return datetime.today()

    def handle(self, paragraph):
        if (self.canHandleRequest(paragraph)):
            paragraph.text = paragraph.text.replace(self.getStringToReplace(), self.startMonthDate())
        else:
            super().handle(paragraph)

    