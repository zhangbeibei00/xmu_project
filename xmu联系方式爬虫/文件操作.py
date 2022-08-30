import csv

# f=open('academy_urls.csv','r',encoding='utf-8')
# cf=csv.reader(f)
# list1=list(cf)
# print(cf)
# # print(list1)
# list2=sorted(list1,key=lambda s:s[1],reverse=True)
# print(list2)

# f=open('new_csv.csv','w',encoding='utf-8',newline='')
# mess1=['hello','new','world']
# mess2=['i','am','waiting','for','you']
# fw=csv.writer(f)
# fw.writerow(mess1)
# fw.writerow(mess2)
# fw.writerows([mess1,mess2])
# f.close()
# print('csv:write over')

import pandas as pd
df=pd.read_csv('new_csv.csv',encoding='utf-8')
print(df)
print(len(df))
print(df['new'])
mess1=['he','is','my','boyfriend','o']

