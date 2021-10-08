import smtplib
from email.mime.text import MIMEText

body = 'This is a test email. How are you?'

msg = MIMEText(body)
msg['From'] = "praneetha.nakirikanti@gmail.com"
msg['To'] = "npraneeta98@gmail.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com',587)
# Enable secured connection
server.starttls()

server.login("praneetha.nakirikanti@gmail.com","mastan786")
server.send_message(msg)
print("Mail sent")
server.quit()
