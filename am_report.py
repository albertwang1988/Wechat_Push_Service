#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import csv
import datetime
import sys

import itchat

def send():
    for user in user_list:
        send_file_path = sys.path[0]+'/log/'+user[2]+'_'+user[3]+'.log'
        send_file = open(send_file_path,'r')
        send_content = send_file.read()

        if user[0] == '用户':
            dialog = itchat.search_friends(name = user[1])[0:]
            for m in dialog:
                itchat.send(send_content,m['UserName'])
                print(m['NickName'],'sent!')

        elif user[0] == '群':
            dialog = itchat.search_chatrooms(name = user[1])[0:]
            for n in dialog:
                itchat.send(send_content,n['UserName'])
                print(n['NickName'],'sent!')
        else:
            continue

        send_file.close()


pkl_path = sys.path[0]+'/itcha.pkl' # define the pkl file path, which stores login and contacts' information
log_time = datetime.datetime.now()

list_file = open(sys.path[0]+'/list/amsend.list','r')
user_list = csv.reader(list_file)

# BATTLE CONTROL ONLINE

itchat.auto_login(hotReload=True,enableCmdQR=2,statusStorageDir=pkl_path)

print(log_time)
send()

list_file.close()

# Module tested OK 10/19/2019