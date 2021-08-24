import smtplib
import datetime as dt
import random

MY_EMAIL = "elvin_send@gmail.com"
MY_PASSWORD = "abcd1234()"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    # connection = smtplib.SMTP("smtp.gmail.com")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

# import smtplib
#
# # Reference: https://docs.python.org/3/library/smtplib.html
#
# my_email = "elvin_send@gmail.com"
# password = "abc123()"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  # layer of security
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="elvin_receive@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
# # connection.close()    # instead of having this, use the with open
#


# # import datetime
# import datetime as dt
#
# now = dt.datetime.now()  # current date and time
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year= 1995, month=12, day=15, hour=4)
# print(date_of_birth)
