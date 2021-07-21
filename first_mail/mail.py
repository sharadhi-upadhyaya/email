import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = '465')
s.auth()
s.login('rosha0894@gmail.com','rosha@123')

msg = MIMEMultipart()
msg['From'] = 'rosha0894@gmail.com'
msg['To']= 'rosha0894@gmail.com'
msg['Subject'] = 'ning tale sari illa'

message = "Get lost"

msg.attach(MIMEText(message,'plain'))

s.send_message(msg)

# del msg

# def create_message(sender, to, subject, message_text):
#     message = MIMEText(message_text)
#     message['to']=to
#     message['from']=sender
#     message['subject']=subject
#     print(message)
#     # return {'raw': base64.urlsafe_b64encode(message.as_string())}
#     return message.as_string()

# create_message('rosha0894@gmail.com','rosha0894@gmail.com','ning tale sari illa','Bye')