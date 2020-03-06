import datetime
import pytz

# naive (without timezone) and aware dates
d1 = datetime.date(2020,3,13)
print(d1)
d2 = datetime.date.today()
print(d2)
print(d2.year)
print(d2.weekday()) # 0-6
print(d2.isoweekday()) # 1-7

# time deltas
td1 = datetime.timedelta(days=7)
print(d2+td1) # returns date
print(d2-td1) # returns date
print(d1-d2) # returns time delta: 8 days, 0:00:00

# time
t1 = datetime.time(9, 30, 45, 100000)
print(t1)
print(t1.hour)

# datetime
dt1 = datetime.datetime(2020,3,13,8,0,0,0)
print(dt1)
print(dt1+td1)

td2 = datetime.timedelta(hours=7)
print(dt1+td2)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utc_now = datetime.datetime.utcnow()

print(dt_today) # timezone is none
print(dt_now) # allows for timezone, default is none
print(dt_utc_now) # includes timezone

# timezones
tz_dt1 = datetime.datetime(2020,3,13,9,0,0,0, tzinfo=pytz.UTC)
print(tz_dt1)
tz_dt_now = datetime.datetime.now(tz=pytz.UTC)
print(tz_dt_now)

dt_stockholm = tz_dt_now.astimezone(pytz.timezone('Europe/Stockholm'))
print(dt_stockholm)

for timezone in pytz.all_timezones:
    print(timezone)

# convert from naive to aware
naive_datetime = datetime.datetime.now()
new_timezone = pytz.timezone('Europe/Vienna')
naive_datetime = new_timezone.localize(naive_datetime)
print(naive_datetime)

# format date
print(naive_datetime.isoformat())
print(naive_datetime.strftime('%B %d, %Y'))

# convert from string to date
date_string = 'March 13, 2020'
date_from_string = datetime.datetime.strptime(date_string, '%B %d, %Y')
print(date_from_string)