import smtplib
from smtplib import SMTP

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("dashbikash135@gmail.com","bk1317dash")
EmailMy = "dashbikash135@gmail.com"
EmailTo = []

with open("Myemail.txt") as f :
    for email in f.readlines():
        EmailTo.append(email)

Message = ''' This is just to inform you all that we can rock you'''

for email in EmailTo:
    server.sendmail(EmailMy,email,Message)
    