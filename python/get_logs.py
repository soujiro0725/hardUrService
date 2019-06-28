#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import paramiko
from scp import SCPClient

TARGET_HOST = '172.16.1.91' # Metasploitable2-2
USER = 'msfadmin'
PASSWORD = 'msfadmin'
LOG_DIR = os.environ['HOME'] + '/Projects/docker-elk-filebeat/logs'


def main():

    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(TARGET_HOST, username=USER, password=PASSWORD)
        with SCPClient(ssh.get_transport()) as scp:
            scp.get('/var/log/apache2/access.log')
        
    # stdin, stdout, stderr = client.exec_command('ls -l /var/log')
    # for line in stdout:
    #     print(line)


if __name__ == '__main__':
    main()


