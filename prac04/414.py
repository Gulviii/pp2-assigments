import sys
import datetime

def parse_line(line):
    date_str, tz_str = line.strip().split()
    year, month, day = map(int, date_str.split('-'))
    local_midnight = datetime.datetime(year, month, day, 0, 0, 0)
    sign = 1 if tz_str[3] == '+' else -1
    hh, mm = map(int, tz_str[4:].split(':'))
    offset = datetime.timedelta(hours=hh, minutes=mm) * sign
    utc_time = local_midnight - offset
    return utc_time

def main():
    line1 = sys.stdin.readline()
    line2 = sys.stdin.readline()
    t1 = parse_line(line1)
    t2 = parse_line(line2)
    diff_seconds = abs((t1 - t2).total_seconds())
    days = int(diff_seconds // (24*3600))
    print(days)

if __name__ == "__main__":
    main()
