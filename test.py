from calendar import month
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

date = datetime.today() + relativedelta(months=12, day=1) - relativedelta(days=1)

print(date.strftime('%d/%m/%Y'))
