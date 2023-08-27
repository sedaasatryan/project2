import smtplib
import socket
import os.path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'sedarmenia@gmail.com'
sender_password = '-----'
recipient_email = 'sedaasatryann@gmail.com'
subject = 'Project 2'
message = 'This is a test email sent from Python.'


# File to store the previous IP address
ip_file_path = 'previous_ip.txt'

# Function to retrieve the current public IP address
def get_current_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip

# Function to read the previous IP address from the file
def read_previous_ip(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()
    return None

# Function to write the current IP address to the file
def write_current_ip(file_path, ip):
    with open(file_path, 'w') as file:
        file.write(ip)

# Check for changes in IP address
current_ip = get_current_ip()
previous_ip = read_previous_ip(ip_file_path)

if current_ip != previous_ip:
    # Update and store the new IP address
    write_current_ip(ip_file_path, current_ip)

    # Create the email content
    message = f'The new IP address is: {current_ip}'



# Create the MIME object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Upgrade the connection to a secure one
server.login(sender_email, sender_password)

# Send the email
server.sendmail(sender_email, recipient_email, msg.as_string())

# Disconnect from the server
server.quit()

print("Email sent successfully!")
