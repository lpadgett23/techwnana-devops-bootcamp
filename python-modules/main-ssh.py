import paramiko

ssh = paramiko.SSHClient()
ssh.connect(hostname='', username='root', port=22)