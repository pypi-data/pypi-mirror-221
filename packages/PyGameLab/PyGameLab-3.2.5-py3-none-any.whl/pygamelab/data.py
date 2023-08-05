import datetime

dependences = []

dependences.append("datetime")
dependences.append("difflib")
dependences.append("json")
dependences.append("random")
dependences.append("string")
dependences.append("sys")
dependences.append("unicodedata")

dependences.append("pygame")

initialized = False
version = "3.2.5"
interpreter = "Python 3.10.11"
dependences_printable = "\n  - ".join(dependences)


class Date:
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
