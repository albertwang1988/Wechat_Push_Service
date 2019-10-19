#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Module to get weather report from HeWeather

import csv
import datetime
import json
import sys

import requests

def get_weather():

    global weather_date,sr_time,ss_time,cond_txt_d,cond_txt_n,tmp_max,tmp_min,wind_dir,wind_sc,hum,pop
    # define urls and file path
    weather_url = 'https://free-api.heweather.com/s6/weather?location='+row[0]+'&key=YOUR KEY HERE'
    weather_feedback = requests.get(weather_url)
    weather_json = json.loads(weather_feedback.text)

    #prepare data to wrie in the log files
    weather_date = weather_json['HeWeather6'][0]['daily_forecast'][0]['date']
    sr_time = weather_json['HeWeather6'][0]['daily_forecast'][0]['sr']
    ss_time = weather_json['HeWeather6'][0]['daily_forecast'][0]['ss']
    cond_txt_d = weather_json['HeWeather6'][0]['daily_forecast'][0]['cond_txt_d']
    cond_txt_n = weather_json['HeWeather6'][0]['daily_forecast'][0]['cond_txt_n']
    tmp_max = weather_json['HeWeather6'][0]['daily_forecast'][0]['tmp_max']
    tmp_min = weather_json['HeWeather6'][0]['daily_forecast'][0]['tmp_min']
    wind_dir = weather_json['HeWeather6'][0]['daily_forecast'][0]['wind_dir']
    wind_sc = weather_json['HeWeather6'][0]['daily_forecast'][0]['wind_sc']
    hum = weather_json['HeWeather6'][0]['daily_forecast'][0]['hum']
    pop = weather_json['HeWeather6'][0]['daily_forecast'][0]['pop']

def car_plate():
    # find the restricted number of cars and write in the file
    global car_plate_num
    car_date = datetime.datetime.now()
    car_week = str(car_date.weekday())
    car_num_file = open(sys.path[0]+'/list/car.list','r')
    car_num = csv.reader(car_num_file)
    for num_row in car_num:
        if num_row[0] == car_week and row[0] == '北京':
            writein_file.writelines(['\n今日限行尾号：',num_row[1]])
        else:
            continue


def write_in():

    global writein_file
    writein_file = open(filename,'w')
    writein_file.writelines([weather_date,row[0],'天气\n\n'])
    writein_file.writelines(['日出时间：',sr_time,'，\n日落时间：',ss_time,'\n'])
    writein_file.writelines(['今天白天：',cond_txt_d,'，最高气温',tmp_max,'℃；晚间：',cond_txt_n,'，最低气温',tmp_min,'℃\n'])
    writein_file.writelines(['风向：',wind_dir,'，风力',wind_sc,'级，相对湿度',hum,'%，降水概率',pop,'%\n\n'])
    car_plate()
    writein_file.close()

# BATTLE CONTROL ONLINE

file_path = sys.path[0] # get path to read list files
location_file = open(file_path+'/list/location.list','r') # open list to read location information
location_data = csv.reader(location_file) # read csv into dictionary for futher procedure


for row in location_data:
    filename = file_path+'/log/weather_'+row[1]+'.log'
    get_weather()
    write_in()

location_file.close()

# Module tested OK 10/19/2019
