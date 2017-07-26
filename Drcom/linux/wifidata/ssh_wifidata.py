# -*- coding:utf-8 -*-
# /etc/config/wireless > wifi重启生效\
# wifi_5g  name=[14] key=[15]
# wifi_2g  name=[30] key=[31]
import paramiko
import ftplib
import os
import time
import socket
import random
import hashlib

print '######################\nSSH , FTP  Loading...'
socket.setdefaulttimeout(3)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ftp = ftplib.FTP()

def input_key():
    global number
    number = '%s'%random.randint(100000, 999999)
    key_number = number+'Benjamin'+number[5]+number[4]
    return key_number

def keytoken(key_number):
    m2 = hashlib.md5()
    m2.update(key_number)
    key =  m2.hexdigest()
    return key

def connect():
    try:
        ssh.connect(hostname='192.168.1.1', port=22, username='root', password='Anonymous',allow_agent=False,look_for_keys=False)
        ftp.connect('192.168.1.1',21)
        ftp.login('root','Anonymous')
        ftp.cwd("/etc/config")
        print '######################\nSSH , FTP Load Sucess!\n######################'
        return True
    except:
        print '######################\nSSH , FTP Load Failed!\n######################'
        time.sleep(60)
        return False

def domain():
    f = file('wireless', 'w+')
    wifi_2g_name = raw_input('Please input wifi_2g_name: ')
    wifi_2g_pw = raw_input('Please input wifi_2g_pw: ')
    print '-------------------------------------------'
    time.sleep(0.3)
    wifi_5g_name = raw_input('Please input wifi_5g_name: ')
    wifi_5g_pw = raw_input('Please input wifi_5g_pw: ')

    data = '''
config wifi-device 'rai0'
    option type 'mt7612'
    option hwmode '11a'
    option channel 'auto'
    option txpower '100'
    option htmode 'VHT80'
    option country 'CN'

config wifi-iface
    option device 'rai0'
    option network 'lan'
    option mode 'ap'
    option encryption 'psk2'
    option ssid '%s'
    option key '%s'

config wifi-device 'ra0'
    option type 'rt2860v2'
    option hwmode '11g'
    option channel 'auto'
    option txpower '100'
    option htmode 'HT40'
    option country 'CN'

config wifi-iface
    option device 'ra0'
    option network 'lan'
    option mode 'ap'
    option encryption 'psk2'
    option ssid '%s'
    option key '%s'

'''%(wifi_5g_name,wifi_5g_pw,wifi_2g_name,wifi_2g_pw)

    f.write(data)
    f.close()

    stdin, stdout, stderr = ssh.exec_command('rm -f /etc/config/wireless')
    time.sleep(1)

    localfile = 'wireless'
    f = open(localfile, 'rb')
    ftp.storbinary('STOR %s' % os.path.basename(localfile), f)

    time.sleep(1)
    stdin, stdout, stderr = ssh.exec_command('wifi')

    ssh.close()
    ftp.close()
    print '\n######################\nThe End,Now Check your router!\n######################'
    time.sleep(60)

key = keytoken(input_key())
error = 0
if connect():
    while error<=2:
        input_key = raw_input('CipherText:%s, Please input Key: '%number)
        if  input_key == key:
            print '\nLogin sucess!\n'
            domain()
            break
        else:
            error += 1
            print 'Key error %s'%error
            if error == 3:
                print '\nThe end,Error more than 3 times!'
                time.sleep(60)
            continue
else:
    pass