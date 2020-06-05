# Date and Time
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate() # gets current date
print(now)
print(now.toString(Qt.ISODate)) # prints yyyy-mm-dd
print(now.toString(Qt.DefaultLocaleLongDate)) # prints local date format.

datetime = QDateTime.currentDateTime()
print(datetime.toString()) # prints date and time

time = QTime.currentTime()
print(time.toString(Qt.DefaultLocaleLongDate))

# =====================================================================
# UTC
print("#==========================================\nUTC\n#==========================================")
now = QDateTime.currentDateTime()
print("local datetime: ", now.toString(Qt.ISODate))
print("Universal datetime: ", now.toUTC().toString(Qt.ISODate))
print("Offset form UTC: {0} seconds".format(now.offsetFromUtc())) # offsetFromUtc gives the difference between UTC and local time in seconds.

# =====================================================================
# Number of days
print("#==========================================\nNumber of days\n#==========================================")
d = QDate(1945,5,7)
print(f"days in month: {d.daysInMonth()}")
print(f"days in year: {d.daysInYear()}")

# =====================================================================
# Difference in days
print("#==========================================\nDifference in days\n#==========================================")
xmas1 = QDate(2020,12,24)
xmas2 = QDate(2019,12,24)
now = QDate.currentDate()

print(f"Xmas to now: {xmas2.daysTo(now)}")
print(f"now to Xmas: {now.daysTo(xmas1)}")

# =====================================================================
# Datetime arithmetic
print("#==========================================\nDatetime arithmetic\n#==========================================")
now = QDateTime.currentDateTime()

print(f"Today: {now.toString(Qt.ISODate)}")
print(f"Adding 12 days: {now.addDays(12).toString(Qt.ISODate)}")
print(f"Substracting 22 days: {now.addDays(-22).toString(Qt.ISODate)}")

print(f"Adding 50 seconds: {now.addSecs(50).toString(Qt.ISODate)}")
print(f"Adding 3 months: {now.addMonths(3).toString(Qt.ISODate)}")
print(f"Adding 12 years: {now.addYears(12).toString(Qt.ISODate)}")

# =====================================================================
# Daylight Saving Time
print("#==========================================\nDST\n#==========================================")
print(f"Time Zone: {now.timeZoneAbbreviation()}")

if now.isDaylightTime():
    print("Daylight Saving Time")
else: print("No Daylight Saving Time")

# =====================================================================
# Unix Epoch
print("#==========================================\nUNIX Epoch\n#==========================================")
unix_time = now.toSecsSinceEpoch() 
print(f"Segundos desde el unix epoch:{unix_time}")

d = QDateTime.fromSecsSinceEpoch(unix_time)
print(f"Unix time en isodate: {d.toString(Qt.ISODate)}")