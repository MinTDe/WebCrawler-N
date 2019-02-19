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

try:
    while True:
    #for i in range(1000):

        #현재 컴퓨터 시각 측정
        time = datetime.now()
        print('------------------------------------------------------------------------------------------------------------------')
        print(time)
        TIME = str(time.year)+str(time.month)+str(time.day)+'_'+str(time.hour)+'.'+str(time.minute)+'.'+str(time.second)
        # 디렉토리 지정
        TIME_PATH = str(time.year)+ '/' + str(time.month)+ '/' +str(time.day)

        #www.naver.com의 html을 parsing
        html = requests.get('https://www.naver.com').text
        soup = BeautifulSoup(html, 'html.parser')
        title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')

        #네이버 급상승 검색어를 list에 삽입
        for idx,title in enumerate(title_list, 0):
            df_topic[idx] = title.text

        # 급상승 검색어 순위가 바뀌면 작동
        if ori_df_topic != df_topic:
            print('Change ranking')
            ori_df_topic = df_topic[:]
            df_basic = {'Ranking':df_ranking, 'Topic':df_topic}
            df = pd.DataFrame(df_basic)

            #해당 디렉토리가 존재하지 않을 때 디렉토리 생성
            if not(os.path.isdir(path + '/' + TIME_PATH + '/')):
                print(False)
                os.makedirs(os.path.join(path + '/' + TIME_PATH + '/'))

            #csv확장자로 파일 저장
            df.to_csv(path + '/' + TIME_PATH + '/' + TIME + ".csv", index = False)
            print(df)

        # 테스트 확인용
        else :
            print('pass')

        #추후에 변화되면 상승시 빨간색 하강시 파란색으로 출력 예정
        print('sec - ori : ', ori_df_topic)
        print('sec - df : ', df_topic)
        print(ori_df_topic == df_topic)
        #for j in range(20):
        #print('Ranking : %2s - df_topic : %-30s %-10s : %30s' %(df_ranking[j],df_topic[j],'-ori_df_topic',ori_df_topic[j]))
        sleep(5)
#Ctrl + C를 누르면 프로그램 중지
except KeyboardInterrupt:
    pass
