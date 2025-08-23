##Automatic Birthday wish Email sender

#smtp:- ye library ek external sourse hai jo email bhejne ke liye use karege.
import smtplib ##simple mail Transfer Protocol

#To create properly formatted email message with subject,body,etc
#ye dynamicaly send ho paye iss liye

from email.mime.text import MIMEText
from datetime import datetime
import time



sender="rajendrasinghdodiya158@gmail.com"
##Sender Gmail address (must be the same used to generate app password)

password="ziah nows qyxg zcck"
##16-character app password generated from your Google account

receiver=input("Enter Your Email Address: ")
##Takes the reciever's email as input from user

name=input("Enter Your Name: ")
dob_input =input("Enter Your Date of Birth(dd-mm): ")#21-08
#Takes the reciever name to personalize the birthday message

send_hour = 12
send_minute =3
print("Waiting for the correct time to send wishes..")


while True:
    now =datetime.now()
    today =now.strftime("%d-%m")

    if dob_input == today and now.hour == send_hour and now.minute == send_minute:
        msg = MIMEText(f"🎂🎂 Happy Birthday! {name} and have a good day 😀😃 ")
        msg['Subject'] = "Happy Birthday!"
        msg['From'] = sender  # email header
        msg['To'] = receiver
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(sender, password)
            server.send_message(msg)
            server.quit()
            print("Email sent successfully")

        except Exception as e:

            print("Something went wrong")
        break

    time.sleep(30)





