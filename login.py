#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Module to login and keep login status of wechat
# GUI or CLI needed to show the QRCode.

import sys

import itchat


def login():
    print ('登陆成功，请保持后台运行')
    # messages showed when login succesfully

def logout():
    print ('退出登录，再次调用可能需要重新登录')
    # messages showed when quit

def interrupted():
    print('异常退出，请检查并重新登录')
    # messages showed when unintended exit occurs

pkl_path = sys.path[0]+'/itcha.pkl' # define the pkl file path, which stores login and contacts' information

# BATTLE CONTROL ONLINE


itchat.auto_login(hotReload=True,enableCmdQR=2,loginCallback=login,exitCallback=logout,statusStorageDir=pkl_path)
# hotReload makes you automatically login without authentication after a short time of logout
# enableCmdQR means show QRCode on CLI interface, numbers followed defined the size of QRCode
# loginCallback and exitCallback defines method when login and logout
# statusStorageDir defined pkl file path

itchat.run()


# Module tested OK 10/20/2019
