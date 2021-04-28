from datetime import date

today = date.today()
birthday = date(today.year, 2, 2)

print(birthday)

if birthday > today:
    diff = birthday - today
    print(f'Pozostało {diff.days} do Twoich urodzin')
else:
    diff = today - birthday
    print(f'Twoje urodziny były {diff.days} dni temu')
    nextbirthday = date(today.year + 1, 2, 2)
    print(f'Następne urodziny masz {nextbirthday} ')
    print(f'Będzie to {nextbirthday.strftime("%A")}')
