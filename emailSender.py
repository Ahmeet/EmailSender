# @happyoakwood
from email.message import EmailMessage
import ssl
import smtplib
# go to https://myaccount.google.com/u/1/apppasswords and create app password.

email_sender = "sender@gmail.com"  # this will be sender e-mail address.
email_password = "password"  # this will be app password.

email_reciever = "reciever@gmail.com"  # this will be reciever e-mail address.
# You can create mail via temp-mail.org

subject = "Test E-Mail"  # subject.
body = "This email sent via python script."  # body.

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciever
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_reciever, em.as_string())
