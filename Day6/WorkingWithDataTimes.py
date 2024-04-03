from datetime import datetime
import time

dt1 = datetime(2024,1,1)
dt2 = datetime.now() #current date time
dt =  datetime.strptime("2024/01/01","%Y/%m/%d") # converting date string to date time


# both lines achieve similar results by providing the current date and time. However, datetime.now() is more concise and straightforward, 
# while datetime.fromtimestamp(time.time()) allows for more flexibility  if you need to work with timestamps directly.
dt = datetime.fromtimestamp(time.time())
print(dt)
print(datetime.now())

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))
print(dt2>dt1)
# datetime object represents in time
from datetime import timedelta #it represents duration

dur = dt2-dt1
print(dur)
print("days",dur.days)
print("days",dur.seconds)
print("days",dur.total_seconds())

dt1 = dt1+timedelta(days=1,seconds=12000)
print(dt1)