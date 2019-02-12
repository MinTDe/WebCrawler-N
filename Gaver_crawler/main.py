# version
# version - alpha -> 검색어 crawler 기능 추가
# version - beta -> 검색어 csv로 저장 기능 추가

# main.py
import requests
import pandas as pd
from bs4 import BeautifulSoup
from pandas import DataFrame

html = requests.get('https://www.naver.com').text
soup = BeautifulSoup(html, 'html.parser')

title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')

df_ranking = []
df_topic = []

for idx,title in enumerate(title_list, 1):
    df_ranking.append(idx)
    df_topic.append(title.text)

df_basic = {'Ranking':df_ranking, 'Topic':df_topic}
df = pd.DataFrame(df_basic)

df.to_csv("C:\Coding\WebCrawler\Gaver\Gaver_crawler\data\data.csv", index = False)
