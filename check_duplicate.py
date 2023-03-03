import os 
import datetime

csv_dir = 'D:\COVID-19\csse_covid_19_data\csse_covid_19_daily_reports_us'

csv_files = os.listdir(csv_dir)

#Create unique name of day to compare
def gen_date():
    date_str = []

    date1 = datetime.date(2020, 5, 14)
    date2 = datetime.date(2023, 2, 27)
    one_day = datetime.timedelta(days = 1)

    while(date1 <= date2):
        date_str.append(date1.strftime('%Y-%m-%d') + '.csv')
        date1 += one_day
    return date_str

unique_name = gen_date()

if len(unique_name) == len(csv_files):
    print('No Duplicate')
else:
    duplicate = []
    for name in unique_name:
        if csv_files.count(name + '.csv') > 1:
            duplicate.append(name)
            print(f'Duplicate day found {name}')

f = open("log.txt",'a')
for i,name in enumerate(csv_files):
    if i <= 1019:
        f.write(name + '    ' + unique_name[i] + '\n')

