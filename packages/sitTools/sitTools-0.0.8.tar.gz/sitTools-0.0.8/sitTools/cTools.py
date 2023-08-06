# coding: utf-8
import requests, os, sys, tarfile, yaml, math, time
import numpy as np
import pandas as pd
import smtplib
import configparser as cfg
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def r_get(url, header, param, times=3, sec=5):
    '''
    r_get(url, header, param, times, sec)

    HTTP GET request function.
    You can define fail retry times and wait sec. by yourself.
    可自訂 HTTP GET 請求異常重試次數與等待秒數的函式

    Argument:
    參數說明

    url = GET request URL, string type.
          請求網址, 字串類型

    header = GET request header, dictionary type.
              請求 header 欄位, 字典類型

    param = GET request data, dictionary type.
             請求資料, 在 request 時會附加在網址, 字典類型

    times = Fail retry times, default retry 3 times, int type.
            請求連線異常重試次數, 預設值為重試 3 次, 整數類型

    sec = Retry wait second, default wait 5 sec., int type.
          重試間隔等待秒數, 預設 5 秒, 整數類型

    '''
    for t in range(times):
        try:
            return requests.get(url, headers=header, params=param)
        except Exception as err:
            stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'{stamp} Connect to {url} err, retry after {sec} sec...')
            time.sleep(sec)
    return None

