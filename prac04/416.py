import datetime

def parse(line):
    date_part, tz_part = line.split(" UTC")
    dt = datetime.datetime.strptime(date_part, "%Y-%m-%d %H:%M:%S")
    sign = 1 if tz_part[0] == '+' else -1
    h, m = map(int, tz_part[1:].split(":"))
    offset = datetime.timedelta(hours=h, minutes=m) * sign
    return dt - offset
start = parse(input().strip())
end = parse(input().strip())

duration = int((end - start).total_seconds())
print(duration)