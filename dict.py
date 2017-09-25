import smtplib
from email.mime.text import MIMEText

people = {}
while True:
    name = input("Enter Name: ")
    e_mail = input("Enter Email: ")
    if name == "":
        break
    people[name] = e_mail


def get_email(people_dict, name):
    print(people_dict.get(name, "Sorry that person is not on our mailing list!"))


def send_emails(people_dict):
    # my credentials
    username = "rodgers.ouma@meltwater.org"
    password = ""

    # connect to server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(username, password)
    server.ehlo()
    server.set_debuglevel(True)  # show communication with the server

    for name, address in people_dict.items():
        # create message
        message = "Dear {}. How is your day?".format(name)
        msg = MIMEText(message)
        msg['Subject'] = "Andrew's Python Class"
        msg['From'] = username
        msg['To'] = address
        server.sendmail(username, address, msg.as_string())
    server.quit()
