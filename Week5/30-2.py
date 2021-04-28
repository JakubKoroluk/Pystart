from datetime import datetime, timedelta


start_date = '05.05.2020'
end_date = '10.05.2020'
salary_per_hour = '100'

fstart_date = datetime.strptime(start_date, '%d.%m.%Y')
fend_date = datetime.strptime(end_date, '%d.%m.%Y')

diff = fend_date - fstart_date
working_days = diff.days

# for day in range(fstart_date, fend_date):
#     print(datetime.strftime(day, '%A, %d,%m,%Y'))

while fstart_date != (fend_date + timedelta(days=1)):
    if fstart_date.strftime('%A') in ['Saturday', 'Sunday']:
        working_days += 1

    print(datetime.strftime(fstart_date, '%A, %d,%m,%Y'))
    diff = timedelta(days=1)
    fstart_date += diff

print(f' Zarobiłeś {int(working_days) * int(salary_per_hour)} dolanów')