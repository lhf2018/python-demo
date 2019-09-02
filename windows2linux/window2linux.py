# -*- coding: utf-8 -*-
import paramiko
import datetime
import os


hostname='***.***.***.***'
user='root'
pwd='*****'

def rexists(sftp, path):
    """os.path.exists for paramiko's SCP object
    """
    try:
        sftp.stat(path)
    except IOError as e:
        if 'No such file' in str(e):
            return False
        raise
    else:
        return True

def window_to_linux_file(local,remote):
    try:
        """sftp文件client"""
        t = paramiko.Transport((hostname, 22))
        t.connect(username=user,password=pwd)
        sftp=paramiko.SFTPClient.from_transport(t)
        """ssh client"""
        ssh = paramiko.SSHClient()
        # 这行代码的作用是允许连接不在know_hosts文件中的主机。
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, 22, user, pwd)

        # 拆分本地地址，拼接远端
        filename=os.path.split(local)
        remote+=filename[1]

        # 检查远端linux是否存在该文件
        if ~rexists(sftp,remote):
            ssh.exec_command('touch '+remote)

        print('upload file start %s ' % datetime.datetime.now())
        sftp.put(local,remote)
        t.close()
    except Exception:
        print("传送文件失败")
        return
    print('upload file end %s ' % datetime.datetime.now())

if __name__=='__main__':
    local='C:\\Users\\11469\\Desktop\\pwd.txt'
    remote='/testmove/'
    window_to_linux_file(local,remote)