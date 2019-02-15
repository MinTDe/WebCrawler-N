# main.py

import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from pandas import DataFrame
from time import sleep
from datetime import datetime
from pathlib import Path

path = str(Path('./data/'))

df_ranking = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ori_df_topic =[None] * 20
df_topic = [None] * 20
str1 = 'ori_df_topic'

#for i in range(1000):

#현재 컴퓨터 시각 측정
time = datetime.now()
print('------------------------------------------------------------------------------------------------------------------')
print(time)
TIME = str(time.year)+str(time.month)+str(time.day)+'_'+str(time.hour)+'.'+str(time.minute)+'.'+str(time.second)
TIME_PATH = str(time.year)+str(time.month)+str(time.day)
print(type(TIME_PATH))
