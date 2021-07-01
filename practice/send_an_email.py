import smtplib

sender = "4025jbh@gmail.com"
receiver = "4025jbh@korea.ac.kr"
password = "password123" #changed
subject = "Python email test"
body = "이메일 작성"

# header
message = f"""From: me{sender}
To: me{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")