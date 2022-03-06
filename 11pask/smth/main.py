import datetime
import smtplib
import random
with open("quotes.txt") as quotes_stream:
    quotes = quotes_stream.readlines()
    quotes_stream.close()
with open("confidential/email.txt") as stream:
    MY_EMAIL = stream.read()
    stream.close()

with open("confidential/password.txt") as stream:
    PASSWORD = stream.read()
    stream.close()
with open("confidential/address.txt") as stream:
    address = stream.read()
    stream.close()
if datetime.date.today().weekday() == 6:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=address,
            msg=f"Subject:This is subject\n\n{random.choice(quotes)}"
        )
