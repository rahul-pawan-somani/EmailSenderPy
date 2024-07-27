# Newsletter Ninja
This Python script allows you to send customized emails that can be formatted with the help of HTML. It can be particularly useful for sending newsletters, notifications, or any other kind of formatted email to your recipients. The script uses a Gmail account to send emails, but you can configure it to work with other email providers as well.

## Prerequisites
- Python 3.x
- smtplib library
- email library
- string library
- pathlib library

## Usage
1. Install the required Python libraries
2. Generate an app password for Gmail if you haven't already. You can create one [here](https://myaccount.google.com/apppasswords).
3. Edit the Python script (`send_email.py`) to provide the following information:
- Sender's email address.
- Receiver's email address.
- Email subject.
- HTML content.
- Sender's app password
4. Run the script using the command:
  python send_email.py
