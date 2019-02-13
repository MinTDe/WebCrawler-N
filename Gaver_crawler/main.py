# version
# version - alpha -> 검색어 crawler 기능 추가
# version - beta -> 검색어 csv로 저장 기능 추가
# version - gamma -> 검색어가 다를시 인식 기능 추가

# main.py
import requests
import pandas as pd
from bs4 import BeautifulSoup
from pandas import DataFrame
from time import sleep

df_ranking = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ori_df_topic =[None] * 20
df_topic = [None] * 20

while(True):
    html = requests.get('https://www.naver.com').text
    soup = BeautifulSoup(html, 'html.parser')

    title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')

    print('line 24', ori_df_topic)

    for idx,title in enumerate(title_list, 0):
        df_topic[idx] = title.text

    if ori_df_topic != df_topic:
        ori_df_topic = df_topic

    print('line 32', ori_df_topic)

    df_basic = {'Ranking':df_ranking, 'Topic':ori_df_topic}
    df = pd.DataFrame(df_basic)
    print(df)
    sleep(3)
    #df.to_csv("D:\Coding\WebCrawler-N\Gaver_crawler\data\data.csv", index = False)
