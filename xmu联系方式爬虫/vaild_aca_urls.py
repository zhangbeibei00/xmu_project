import pandas as pd
import requests
import re

data=pd.read_csv('academy_urls.csv')
vaild_orgs=[]
vaild_urls=[]
for row in data.itertuples():
    url=getattr(row,'urls')
    org=getattr(row,'orgs')
    if not("xmu.edu.cn"in url):
        continue
    try:
        r=requests.get(url)
    except:
        print("unvaild")
        continue
    code=r.status_code
    if code!=200:
        print("unvaild")
        continue
    print("vaild")
    print(url,org)
    vaild_orgs.append(org)
    vaild_urls.append(url)

print(vaild_orgs)
print(vaild_urls)
dataframe=pd.DataFrame({'vaild_orgs':vaild_orgs,'vaild_urls':vaild_urls})
dataframe.to_csv("vaild_academy_urls.csv",index=False,sep=',')
