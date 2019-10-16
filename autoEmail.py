import smtplib, ssl, datetime
from getpass import getpass

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = input("Enter your email address: ")
password = getpass()
receiver_email = input("To: ")
subject = input("Subject: ")
content = input("Message: ")
message = """\
Subject: """ + subject + """

""" + content

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    print("Logged in")
    server.sendmail(sender_email, receiver_email, message)
    print("Email sent!") 
    print(datetime.datetime.now())