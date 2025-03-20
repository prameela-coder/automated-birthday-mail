# Email Automation Script
import pandas as pd
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load employee email addresses from Excel
df = pd.read_excel('employeedetails.xlsx')
emails = df['email'].tolist()

# Email configuration
sender_email = "prameelakala340@gmail.com"
sender_password = "jathin0504$"
subject = "Automated Email Notification"
body = "hello This is an automated message sent to all employees."

# Set up the server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_password)

# Send email to each employee
for email in emails:
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'birthday'))
    
    server.send_message(msg)

# Close the server
server.quit()
