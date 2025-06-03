'''
 Default Argument Function
 Define a function send_email(subject, message, sender="admin@example.com") that simulates sending an email. 
 The function should print the sender's email address, subject, and message.
'''

def send_email(subject , message , sender="admin@example.com"):
    print(subject , message , sender )
subject="Request for leave"
message="Dear sir , Please grant me leave from 4 June to 8 June 2025 "
sender=""
send_email(subject , message , sender)