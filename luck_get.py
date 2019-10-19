#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import csv
import json
import sys

import requests

def get_luck():

    global datetime,name,allcount,color,health,love,money,number,qfriend,summary,work
    luck_feedback = requests.get(luck_url)
    luck_json = json.loads(luck_feedback.text)
    name = luck_json['name']
    datetime = luck_json['datetime']
    allcount = luck_json['all']
    color = luck_json['color']
    health = luck_json['health']
    love = luck_json ['love']
    money = luck_json['money']
    work = luck_json ['work']
    number = str(luck_json ['number'])
    qfriend = luck_json['QFriend']
    summary = luck_json['summary']

def write_in():
    
    writein_file = open (filename,"w")
    writein_file.writelines([name,datetime,"运势\n\n"])
    writein_file.writelines(["今日综合指数：",allcount,"；幸运色：",color,"；健康指数：",health,"；爱情指数：",love,"；财运指数：",money,"；工作指数：",work,"\n"])
    writein_file.writelines(["今日幸运数字：",number,"；速配星座：",qfriend,"\n\n"])
    writein_file.writelines([summary,"\n"])
    writein_file.close()

# BATTLE CONTROL ONLIN

url_list = ['水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座']
filename_list = ['luck_shuiping','luck_shuangyu','luck_baiyang','luck_jinniu','luck_shuangzi','luck_juxie','luck_shizi','luck_chunv','luck_tiancheng','luck_tianxie','luck_sheshou','luck_mojie']

for i in range(12):
    luck_url = "http://web.juhe.cn:8080/constellation/getAll?consName=" + url_list[i] + "&type=today&key=YOUR KEY HERE"
    get_luck()
    filename = sys.path[0] + '/log/' + filename_list[i] + ".log"
    write_in()

# Module tested OK 10/19/2019
