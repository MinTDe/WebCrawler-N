import pandas as pd

col = [1,2,3]
time_range = [1,2,3]
time_pd = pd.DataFrame(0., columns=col, index=time_range)
filename = 'b'
time_pd.to_csv(filename + ".csv", mode='w')
time_pd.to_csv("D:\Coding\WebCrawler-N\Gaver_crawler\data\ " + filename + ".csv", index = False)
