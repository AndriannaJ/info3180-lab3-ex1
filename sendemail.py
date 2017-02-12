import smtplib

from_name = 'Andrianna Jack'
from_addr = 'andriannaaj@gmail.com'
to_name = 'YOU'
to_addr = 'andriannaaj@gmail.com'


subject = 'INFO 3180 - Lab3'
msg = 'Lab3- exercise1'
message = """From: {} <{}>
To: {} <{}> 
Subject: {}
{}
"""
message_to_send = message.format(from_name, from_addr, to_name,
 to_addr, subject, msg)
 
# Credentials (if needed)

username = ''
password = ''

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls() 
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 