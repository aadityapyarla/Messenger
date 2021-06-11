import pywhatkit
import datetime
now = datetime.datetime.now()
hour = int(now.strftime("%H"))
time_min = int(now.strftime("%M"))
time_sec = int(now.strftime("%S"))
if time_min == 59 and time_sec == 59:
    hour += 1
number = 7738643500
message = "Mummy go to sleep!"
pywhatkit.sendwhatmsg(f"+91{number}", message, hour, time_min + 2)

