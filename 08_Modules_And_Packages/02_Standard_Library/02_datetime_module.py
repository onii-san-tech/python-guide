"""
The datetime Module

Work with dates and times.
"""

from datetime import datetime, date, timedelta

# Current date and time
now = datetime.now()
print(now)
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)

# Formatting dates
print(now.strftime("%Y-%m-%d"))          # 2024-01-15
print(now.strftime("%d %B, %Y"))         # 15 January, 2024
print(now.strftime("%I:%M %p"))          # 02:30 PM

# Parsing a date string
birthday = datetime.strptime("1990-06-15", "%Y-%m-%d")
print(birthday)

# Date arithmetic
today = date.today()
in_30_days = today + timedelta(days=30)
print(f"30 days from now: {in_30_days}")

# Age calculator
birth_date = date(1990, 1, 1)
age = (today - birth_date).days // 365
print(f"Age: {age} years")
