import smtplib


sender_email = "felixkitonga2001@gmail.com"
rec_email =  "felixmutua6847@gmail.com"
password = "wilw czbi ijww yicq"
message = "hey fella this mail was sent using python"
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
print("login success")
server.sendmail(sender_email,rec_email,message)
print("Email sent to rec_email")