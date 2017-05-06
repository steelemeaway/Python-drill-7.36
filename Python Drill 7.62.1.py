
import datetime
from datetime import datetime, timedelta, time

portlandTime = datetime.now()
portlandHour = int(portlandTime.strftime("%H"))
nycTime = portlandTime + timedelta(hours=3)
nycHour = int(nycTime.strftime("%H"))
londonTime = portlandTime + timedelta(hours=8)
londonHour = int(londonTime.strftime("%H"))

closingTime = 21
openingTime = 9

if nycHour >= closingTime or nycHour < openingTime:
    print "NYC location is closed"
else:
    print "NYC location is open"

if londonHour >= closingTime or londonHour < openingTime:
    print "London location is closed"
else:
    print "London location is open"

