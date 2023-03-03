import datetime

date_str = []

date1 = datetime.date(2020, 5, 14)
date2 = datetime.date(2023, 2, 27)
one_day = datetime.timedelta(days = 1)

while(date1 <= date2):
    date_str.append(date1.strftime('%Y-%m-%d') + '.csv')
    date1 += one_day

print(date_str)
