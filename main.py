import datetime as dt
import random
import smtplib

MY_EMAIL = "myemail@gmail.com"
MY_PASSWORD = "mypassword"

now = dt.datetime.now()
weekday = now.weekday()
# 0 = first day of a week (Monday)
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        to_addrs="emailadress@gmail.com",
        from_addr=MY_EMAIL,
        msg=f"Subject:Monday Motivation\n\n{quote}"
    )
