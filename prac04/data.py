from datetime import datetime, timedelta
now = datetime.now()
five_days_ago = now - timedelta(days=5)
print("Current date:", now.date())
print("Five days ago:", five_days_ago.date())

# Кеше, бүгін, ертеңді шығару
from datetime import datetime, timedelta
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#datetime‑тен микросекундтарды алып тастау
from datetime import datetime
now = datetime.now()
without_microseconds = now.replace(microsecond=0)
print("With microseconds:", now)
print("Without microseconds:", without_microseconds)

#Екі күннің айырмасын секундпен есептеу
from datetime import datetime
date1 = datetime(2026, 2, 19, 14, 30, 0)
date2 = datetime(2026, 2, 18, 12, 0, 0)
diff_seconds = abs((date1 - date2).total_seconds())
print("Difference in seconds:", diff_seconds)