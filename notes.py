# Day 31 SMTP DateTime

# import smtplib
#
# my_email = ""
# my_password = ""
# their_email = ""
#
#
# # gmail_connection = smtplib.SMTP("smtp.gmail.com")
# with smtplib.SMTP("smtp.gmail.com") as gmail_connection:
#     gmail_connection.starttls()
#     gmail_connection.login(user=my_email, password=my_password)
#     gmail_connection.sendmail(from_addr=my_email, to_addrs=their_email, msg="Subject: A greeting\n\n Howdy from the "
#                                                                             "body!")
# # gmail_connection.close() # This setup automatically closes.

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()

print(now)
print(year)
print(month)
print(weekday)

date_of_birth = dt.datetime(year=1999, month=6, day=2)
print(date_of_birth)