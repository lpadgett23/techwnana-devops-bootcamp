import requests
import smtplib
from dotenv import load_dotenv
import os
import paramiko
import linode_api4
import time
import schedule

# she did this without dotenv load and only os.environ.get()..... why am I used to doing it with dotenv, is it because DE usually has lots of vars to import? do they call the sys a different # of times at runtime?
# ohhh, she set them inside of pycharm. I prefer it all in the code, nothing manual
load_dotenv()
EMAIL_ADDRESS=os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD=os.getenv("EMAIL_PASSWORD_RAW")
HOSTNAME=os.getenv("HOSTNAME")
KEY_FILENAME=os.getenv("PRIVATE_SSH_KEY_FILENAME")
key_path=os.path.expanduser(KEY_FILENAME)
LINODE_TOKEN=os.getenv("LINODE_TOKEN")
LINODE_RESOURCE_ID=os.getenv("LINODE_SERVER_ID")


def restart_server_and_container_linode():
    # restart linode server
    print('Rebooting the server')
    linode_client = linode_api4.LinodeClient(LINODE_TOKEN)
    nginx_server = linode_client.load(linode_api4.Instance, LINODE_RESOURCE_ID)
    nginx_server.reboot()

    # restart the application after enough time post-reboot - will base it on a state check
    while True:
        nginx_server = linode_client.load(linode_api4.Instance, LINODE_RESOURCE_ID)
        if nginx_server.status == 'running':
            time.sleep(60)  #seconds
            restart_container_on_server()
            break


def send_notification(body_msg):
    print('Sending notification email .. ')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:                       # this is the provider's smtp + their port
        smtp.starttls()                                                     # encrypt the comm from python to our email server
        smtp.ehlo()                                                         # identify our python app with the mail server on this encrypted conn
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        msg=f"Subject: SITE DOWN\n {body_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)                    # sender, receiver, msg

def restart_container_on_server():
    print('Restarting the application .. ')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(HOSTNAME, username='root', key_filename=key_path)
    stdin, stdout, stderr = ssh.exec_command('docker start 9416280eea63')
    print(stdout.readlines())
    ssh.close()
    print('Application restarted.')


def monitor_application():
    try:
        res = requests.get('http://172-105-154-156.ip.linodeusercontent.com:8080') # this is the reverse dns + the port that is open

        if res.status_code == 200:
            print('Application is up & running successfully!')
        else:
            print('Application Down. Fix it!')
            msg=f"Application returned{res.status_code}. Fix the issue tout de suite! Restart the application"
            send_notification(msg)

            # restart the application
            # re: mechanism: it's common to connect via ssh in python scripts
            restart_container_on_server()

    except Exception as e:
        print(f'Connection error happened: {e}')
        msg="Application not accessible at all."
        send_notification(msg)
        restart_server_and_container_linode()
    


schedule.every(5).seconds.do(monitor_application)

while True:
    schedule.run_pending()