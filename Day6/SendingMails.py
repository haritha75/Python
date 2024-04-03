
# smtplib is a Python library used for sending emails using the Simple Mail Transfer Protocol (SMTP). It is part of the standard library in Python, so you don't need to install any additional packages to use it.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

templete=Template(Path("Templet.html").read_text())

message = MIMEMultipart()
message["from"] = "Haritha"
message["to"] = "yerukonduharitha@gmail.com"
message["subject"]="Hi... this is test mail"
body = templete.substitute(name="john")
message.attach(MIMEText(body,"html"))
message.attach(MIMEImage(Path("apple.png").read_bytes()))



with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
  smtp.ehlo() # we are sending small request like hello  to indicating that
  smtp.starttls()
  smtp.login("yerukonduharitha@gmail.com","Haritha@23")
  smtp.send_message(message)
  print("Send...")

