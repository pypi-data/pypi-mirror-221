import datetime

today = datetime.date.today()
now = datetime.datetime.now()
time = now.time()

second = now.second
minute = now.minute
hour = now.hour
year = today.year

class day:
   number = datetime.date.today().day
   name = datetime.date.today().strftime("%A")

class month:
   number = datetime.date.today().month
   name = datetime.date.today().strftime("%B")