#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Module to get weather forecast

import csv
import datetime
import json
import sys

import requests


def get_forecast():

    global forecast_date,cond_txt_d,cond_txt_n,hum,pop,tmp_max,tmp_min,wind_dir,wind_sc
    
    # define urls and file path
    forecast_url = 'https://free-api.heweather.com/s6/weather?location='+row[0]+'&key=YOUR KEY HERE'
    forecast_feedback = requests.get(forecast_url)
    forecast_json = json.loads(forecast_feedback.text)

    #prepare data to wrie in the log files
    forecast_date = forecast_json['HeWeather6'][0]['daily_forecast'][1]['date']
    cond_txt_d = forecast_json['HeWeather6'][0]['daily_forecast'][1]['cond_txt_d']
    cond_txt_n = forecast_json['HeWeather6'][0]['daily_forecast'][1]['cond_txt_n']
    hum = forecast_json['HeWeather6'][0]['daily_forecast'][1]['hum']
    pop = forecast_json['HeWeather6'][0]['daily_forecast'][1]['pop']
    tmp_max = forecast_json['HeWeather6'][0]['daily_forecast'][1]['tmp_max']
    tmp_min = forecast_json['HeWeather6'][0]['daily_forecast'][1]['tmp_min']
    wind_dir = forecast_json['HeWeather6'][0]['daily_forecast'][1]['wind_dir']
    wind_sc = forecast_json['HeWeather6'][0]['daily_forecast'][1]['wind_sc']


def car_plate():
    # find the restricted number of cars and write in the file
    global car_plate_num
    car_date = datetime.datetime.now()
    car_week = str((car_date.weekday()+1)%7)
    car_num_file = open(sys.path[0]+'/list/car.list','r')
    car_num = csv.reader(car_num_file)
    for num_row in car_num:
        if num_row[0] == car_week and row[0] == '北京':
            writein_file.writelines(['\n明日限行尾号：',num_row[1]])
        else:
            continue

def write_in():

    global writein_file
    writein_file = open(filename,'w')
    writein_file.writelines(["明日（",forecast_date,"）",row[0],"天气预报\n\n"])
    writein_file.writelines(["明天白天：",cond_txt_d,"，最高气温",tmp_max,"℃；晚间：",cond_txt_n,"，最低气温",tmp_min,"℃\n"])
    writein_file.writelines(['风向：',wind_dir,'，风力',wind_sc,'级，相对湿度',hum,'%，降水概率',pop,'%\n\n'])
    car_plate()
    writein_file.close()



file_path = sys.path[0] # get path to read list files
location_file = open(file_path+'/list/location.list','r') # open list to read location information
location_data = csv.reader(location_file) # read csv into dictionary for futher procedure

for row in location_data:
    filename = file_path+'/log/forecast_'+row[1]+'.log'
    get_forecast()
    write_in()

location_file.close()

# Module tested OK 10/19/2019
