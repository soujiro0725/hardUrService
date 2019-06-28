#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import paramiko
import shutil
from scp import SCPClient


TARGET_HOST = '172.16.1.91' # Metasploitable2-2
USER = 'msfadmin'
PASSWORD = 'msfadmin'
LOG_DIR = os.environ['HOME'] + '/Projects/docker-elk-filebeat/logs/'

FILE_NAME = 'error.log'

FILE_LIST = [
             'apache2/access.log',
             'apache2/error.log',
             'auth.log',
             'boot',
             'btmp',
             'daemon.log',
             'debug',
             # 'dist-upgrade', #scp.SCPException: scp: /var/log/dist-upgrade: not a regular file
             'dmesg',
             'dpkg.log',
             # 'fsck',
             'kern.log',
             # 'installer',
             'lastlog',
             'lpr.log',
             'mail.err',
             'mail.info',
             'mail.log',
             'mail.warn',
             'messages',
             # 'samba',
             'syslog',
             'udev',
             'user.log',
             # 'vsftpd.log', # permission denied
             'wtmp'
             ]



def main():

    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(TARGET_HOST, username=USER, password=PASSWORD)
        with SCPClient(ssh.get_transport()) as scp:
            for f in FILE_LIST:
                scp.get('/var/log/' + f)
                if f.find('/') != -1: # if logs are in subdirectories
                    f = f.split('/')[1]
                shutil.move(f, LOG_DIR + f)
        
    # stdin, stdout, stderr = client.exec_command('ls -l /var/log')
    # for line in stdout:
    #     print(line)


if __name__ == '__main__':
    main()


