from datetime import datetime, date, time


t = time(22, 30, 0)
form_dt = t.strftime("%I: %M: %S %p")
print(form_dt)