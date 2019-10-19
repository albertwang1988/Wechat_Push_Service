#! /usr/bin/env python3
# =-*- coding:utf-8 -*-

import sys
import time

import itchat

day = int((time.strftime("%d")))
pkl_path = sys.path[0]+'/itcha.pkl' # define the pkl file path, which stores login and contacts' information

if day <= 7:
    itchat.auto_login(hotReload=True,statusStorageDir=pkl_path)
    chatroom = itchat.search_chatrooms(name='HELLDIVERS')
    for m in chatroom:
        itchat.send('今天会免更新啦！快去PS+会员下载！',m['UserName'])

# Module tested OK 10/19/2019