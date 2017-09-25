import smtplib
import email.utils
from email.mime.text import MIMEText

people = {}
while True:
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    if name == "":
        break
    people[name] = email


def get_email(people_dict, name):
    print(dict[name])


def send_emails(people_dict):
    for name, address in people_dict.items()

    # Create the message
    msg = MIMEText("Hello {}".format(name))
    msg['To'] = email.utils.formataddr((name, address))
    msg['From'] = email.utils.formataddr(("Anon User", 'cenafa@d1yun.com'))
    msg['Subject'] = "Andrew's Python Class"

    server = smtplib.SMTP('localhost', 1025)
    server.set_debuglevel(True)  # show communication with the server
    try:
        server.sendmail('cenafa@d1yun.com',
                        [address],
                        msg.as_string())
    finally:
        server.quit()
