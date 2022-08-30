# import csv
# with open(r"D:\project\python\test\get_info\get_info\math_info.csv", "rt") as csvfile:
#         reader = csv.reader(csvfile)
#         column = [row[0] for row in reader]
#         print(column)

import re

# text1 = 'helpmath@xmu.edu.cn'
# text2 = '白鹭嘉奖申请+姓名”，发送到mathtw@xmu.edu.cn，文件和邮件件标注“白鹭嘉奖申请+姓名”。四、评奖程序1.学院下发评奖通知，学生在规'
# mol = r'([\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+)'
#
# f = re.finditer(mol, text2)
# for i in f:
#     print(i.group(1))
#     if len(i.group(1)) < len(text2):
#         print('false')
#     else:
#         print('True')
#     break


# ans = ('1', '2', '3', '4', '5')
# if ans[0]!='1':
#     print('ll')
# else:
#     print("oo")

# import csv
# with open(r"D:\project\python\test\get_info\get_info\math_info.csv", "rt") as csvfile:
#         reader1 = csv.reader(csvfile)
#         reader2=csv.reader(csvfile)
#         col = [row[0] for row in reader1]
#

import pandas as pd
import numpy as np
import pickle
# # data_col = ['url', 'yuan']
# # data1 = pd.read_csv(r'D:\project\python\test\get_info\get_info\math_info.csv', usecols=[0, 1],names=data_col)
# # print(data1['url'])
# # data_array = np.array(data1['url'])
# # data_list =data_array.tolist()
# # # print(data_list)
# # print(data1['yuan'][0])
# data_col = ['yuan', 'url']
# data1 = pd.read_csv(r'D:\project\python\test\vaild_academy_urls.csv', usecols=[0, 1], names=data_col)
# print(data1['url'])
# url_array = np.array(data1['url'])
# url_list = url_array.tolist()[1:]
# yuan_array=np.array(data1['yuan'])
# yuan_list=yuan_array.tolist()[1:]
# start_urls = url_list
# print(start_urls)
# print(yuan_list)
# yuan_pat = r'\/\/[a-zA-Z0-9]+'
# key_list = [re.findall(yuan_pat, url)[0][2:] for url in start_urls]
# print(key_list)
# dict1 = dict(zip(key_list,yuan_list))
# # print(dict1)
#
# f_save = open('dict_file.pkl', 'wb')
# pickle.dump(dict1, f_save)
# f_save.close()
#
# f_read = open(r'D:\project\python\test\get_info\get_info\spiders\dict_file.pkl', 'rb')
# name_dict1 = pickle.load(f_read)
# print(name_dict1)
# f_read.close()

with open(r'D:\project\python\test\get_info\get_info\spiders\dict_file.pkl','rb')as f:
    data=pickle.load(f)
print(data)

# web_str='https://chem.xmu.edu.cn/info/1079/8518.htm'
# print(web_str.count('/'))
# print(web_str[-1])

