import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

# app password has to be generated through https://myaccount.google.com/apppasswords
sender_app_password = ''

try:
    # Read HTML template
    html = Template(Path('index.html').read_text(encoding='utf-8'))

    # Create EmailMessage instance
    email = EmailMessage()
    email['from'] = ''  # Enter sender's email address
    email['to'] = ''    # Enter receiver's email address
    email['subject'] = ''  # Enter the subject of the email
    email.set_content(html.substitute({'variable_name': 'value'}), 'html')

    # Connect to SMTP server and send the email
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('sender_email_ID', sender_app_password)
        smtp.send_message(email)

except FileNotFoundError as e:
    print(f"Error: HTML file 'index.html' not found. {e}")
except Exception as e:
    print(f"Error: An unexpected error occurred. {e}")
