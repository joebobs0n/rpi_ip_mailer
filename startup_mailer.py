import subprocess
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import time
import http.client as httplib

throwaway_email = 'your_email@gmail.com'
email_password = 'your password'


def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False


while not have_internet():
    pass

gmail_user = throwaway_email  # throwaway email
gmail_password = email_password  # throwaway email password
to = [throwaway_email]  # target email (same as throwaway)
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)  # Server to use.

arg = 'hostname'  # Linux command to retrieve device's name
# Runs 'arg' in a hidden terminal.
p = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
data = p.communicate()  # Get data from 'p terminal'.
# Parse out device name
name_lines = data[0].splitlines()
name_line = name_lines[0].split()
name = name_line[0]
device = '%s' % (name.decode())

arg = 'hostname -I'  # Linux command to retrieve ip addresses
# Runs 'arg' in a hidden terminal.
p = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
data = p.communicate()  # Get data from 'p terminal'.
# Parse out ip address of device
ip_lines = data[0].splitlines()
split_line = ip_lines[0].split()
ipaddr = split_line[0]
my_ip = '%s' % (ipaddr.decode())

# start communication with server with TLS encryption
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)  # log into server

# Creates the text, subject, 'from', and 'to' of the message.
for recipient in to:
    msg = MIMEText(my_ip)
    msg['Subject'] = 'IP Addr - %s (%s)' % (device, datetime.now().strftime('%d %b %Y at %H:%M:%S'))
    msg['From'] = gmail_user
    msg['To'] = recipient

    # Sends the message
    smtpserver.sendmail(gmail_user, [recipient], msg.as_string())

# Closes the smtp server.
smtpserver.quit()
