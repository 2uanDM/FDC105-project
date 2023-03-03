import os
import datetime 

csv_dir = 'D:\COVID-19\csse_covid_19_data\csse_covid_19_daily_reports'

csv_files = os.listdir(csv_dir)

for csv_file in csv_files:
    date_str = csv_file.split('.')[0]
    date = datetime.datetime.strptime(date_str, '%m-%d-%Y')
    new_name = date.strftime('%Y-%m-%d') + '.csv'
    os.rename(os.path.join(csv_dir, csv_file), os.path.join(csv_dir, new_name))