import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 


# app password has to be genrated through https://myaccount.google.com/apppasswords
sender_app_password = ''

html = Template(Path('index.html').read_text(encoding='utf-8'))
email = EmailMessage()
email['from'] = '' # enter sender's email address
email['to'] = '' # enter reciver's email address
email['subject'] = '' # enter the subject of the email
email.set_content(html.substitute({'variable_name': 'value'}), 'html') # wrtie the variables and it's values for the html file between the curly brackets

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender_email_ID', sender_app_password)
    smtp.send_message(email)
