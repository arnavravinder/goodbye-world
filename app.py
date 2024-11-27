import datetime

end_date = datetime.datetime.now() + datetime.timedelta(days=25*365)

while datetime.datetime.now() < end_date:
    print("Goodbye, World!") 