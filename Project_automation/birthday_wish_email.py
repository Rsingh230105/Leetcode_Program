##Automatic Birthday wish Email sender

#smtp:- ye library ek external sourse hai jo email bhejne ke liye use karege.
import smtplib ##simple mail Transfer Protocol

#To create properly formatted email message with subject,body,etc
#ye dynamicaly send ho paye iss liye

from email.mime.text import MIMEText

sender="rajendrasinghdodiya158@gmail.com"
##Sender Gmail address (must be the same used to generate app password)

password="ziah nows qyxg zcck"
##16-character app password generated from your Google account

receiver=input("Enter Your Email Address: ")
##Takes the reciever's email as input from user

name=input("Enter Your Name: ")
#Takes the reciever name to personalize the birthday message

msg = MIMEText(f"🎂🎂 Happy Birthday! {name} and have a good day 😀😃 ")
##Cretes the body content of the email with emojis and name

msg['Subject'] = "Happy Birthday!"
msg['From'] = sender  #email header
msg['To'] = receiver

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
#Connects securely to Gmail's SMTP server using SSL and port 465

#Logs in to the Gmail server using the senders email and app password
server.login(sender,password)

server.send_message(msg)
#message send

server.quit()

print("Email sent successfully")



