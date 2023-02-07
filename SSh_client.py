

import paramiko
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect('45.79.72.239',username= 'autonomiq', password='g3sr3CrHs7M$7rb',port=22)
sftp_client=ssh.open_sftp()
#sftp_client.get('/home/autonomiq/outfile1.txt','outfile1.txt')

sftp_client.put('./out.txt','/home/autonomiq/out.txt')

sftp_client.close()
ssh.close()


