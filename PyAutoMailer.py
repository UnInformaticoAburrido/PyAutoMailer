from email import encoders
from email.mime.base import MIMEBase
import smtplib
import json
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
receivers = []
with open('config.json', 'r') as file:
    config = json.load(file)
smtp_server = config['smtp_server']
smtp_port = config['smtp_port']
user = config['user']
password = config['password']
attachment_path = config['attachment_path']
attachment_name = config['attachment_name']
message_path= config['message_path']
receiver_path= config['receiver_path']
C_Subject= config['C_Subject']
FileAtachement=config['FileAtachement']
with open(receiver_path, "r") as archivo:
    for linea in archivo:
        receivers.append(linea)
with open(message_path, "r", encoding="utf-8") as archivo:
    messageG = archivo.read()
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(user, password)
for receiver in receivers:
    message = MIMEMultipart()
    message['From'] = user
    message['To'] = receiver
    message['Subject'] = C_Subject
    message.attach(MIMEText(messageG, 'plain'))
    if(FileAtachement):
        with open(attachment_path, 'rb') as attached_file:
            adjunto_MIME = MIMEBase('application', 'octet-stream')
            adjunto_MIME.set_payload(attached_file.read())
            encoders.encode_base64(adjunto_MIME)
            adjunto_MIME.add_header('Content-Disposition', f"attachment; filename= {attachment_name}")
            message.attach(adjunto_MIME)
    server.send_message(message)
    print("Sent to > "+receiver)
server.quit()
print("Execution finished press enter to continue")
input()