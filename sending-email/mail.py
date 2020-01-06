import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Aditya Singh'
email['to'] = '<to email address>'
email['subject'] = 'Any Subject'

email.set_content(html.substitute({'name': 'sender'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('<your email address>', '<your password>')
  smtp.send_message(email)

print('Email Sent!')