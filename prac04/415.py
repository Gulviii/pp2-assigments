import sys
from datetime import datetime, timedelta, timezone
import math

def parse_date(line):
    date_part, tz_part = line.strip().split()
    year, month, day = map(int, date_part.split('-'))
    sign = 1 if tz_part[3] == '+' else -1
    hours = int(tz_part[4:6])
    minutes = int(tz_part[7:9])
    offset = timezone(sign * timedelta(hours=hours, minutes=minutes))
    return year, month, day, offset

b_line = sys.stdin.readline()
c_line = sys.stdin.readline()

b_year, b_month, b_day, b_tz = parse_date(b_line)
c_year, c_month, c_day, c_tz = parse_date(c_line)

current = datetime(c_year, c_month, c_day, tzinfo=c_tz)

def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def get_birthday(year):
    if b_month == 2 and b_day == 29 and not is_leap(year):
        return datetime(year, 2, 28, tzinfo=b_tz)
    return datetime(year, b_month, b_day, tzinfo=b_tz)

birthday = get_birthday(c_year)
if birthday.astimezone(timezone.utc) < current.astimezone(timezone.utc):
    birthday = get_birthday(c_year + 1)

delta = birthday.astimezone(timezone.utc) - current.astimezone(timezone.utc)
seconds = delta.total_seconds()

if seconds == 0:
    print(0)
else:
    days = math.ceil(seconds / 86400)
    print(days)
