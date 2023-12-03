import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


host = "smtp.gmail.com"
port = 587

sender_email = "felixkitonga2001@gmail.com"
rec_email = "felixmutua6847@gmail.com"
password ="wilw czbi ijww yicq"

message = MIMEMultipart("alternative")
message['subject'] = "mail sent using python"
message['from'] = sender_email
message['to'] = rec_email
message['cc'] = sender_email
message['bcc'] = sender_email

html = ""
with open("mail.html",'r') as file:
    html= file.read()

html_part = MIMEText(html, 'html')
message.attach(html_part)

smtp = smtplib.SMTP(host, port)

status_code, response = smtp.ehlo()
print(f"[*] echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(sender_email, password)
print(f"[*] logging in: {status_code} {response}")

smtp.sendmail(sender_email, rec_email, message.as_string)
smtp.quit()

