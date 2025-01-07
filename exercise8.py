from datetime import datetime

birthday_input = input("Enter your birthday (YYYY-MM-DD): ")

birthday = datetime.strptime(birthday_input, "%Y-%m-%d")

now = datetime.now()

if now.month > birthday.month or (now.month == birthday.month and now.day > birthday.day):
    birthday = birthday.replace(year=now.year + 1)
elif now.month == birthday.month and now.day == birthday.day:
    print("Today is your birthday!")
    exit()
else:
    birthday = birthday.replace(year=now.year)

time_remaining = birthday - now

days_remaining = time_remaining.days
hours_remaining = time_remaining.seconds // 3600
minutes_remaining = (time_remaining.seconds % 3600) // 60


print(f"Your birthday is in {days_remaining} days, {hours_remaining} hours, and {minutes_remaining} minutes!")