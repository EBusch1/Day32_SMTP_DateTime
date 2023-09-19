# Day 31 SMTP DateTime

import smtplib



# gmail_connection = smtplib.SMTP("smtp.gmail.com")
with smtplib.SMTP("smtp.gmail.com") as gmail_connection:
    gmail_connection.starttls()
    gmail_connection.login(user=my_email, password=my_password)
    gmail_connection.sendmail(from_addr=my_email, to_addrs=their_email, msg="Subject: A greeting\n\n Howdy from the "
                                                                            "body!")
# gmail_connection.close() # This setup automatically closes.
