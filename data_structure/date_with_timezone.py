from datetime import datetime
from pytz import timezone

d = datetime(2021, 8, 2, 9, 30, 0)
print(d)

central = timezone("US/Central")
loc_d = central.localize(d)

print(loc_d)

bang_d = loc_d.astimezone(timezone("Asia/Kolkata"))
print(bang_d)
