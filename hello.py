#encoding=utf-8
import pyminizip
import os

compression_level = 5 # 1-9

def getPassword(filename):
    with open('password.txt','r') as foo:
        for line in foo.readlines():
            if filename in line:
                arr = line.split(':')
                # print(arr[1][:-1])
                return arr[1][:-1]

# 如果此循环在迭代第一次时break出，则其效果和上面的相同
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if ".docx" in name:
            namebefore = name[:-5]
            password = getPassword(namebefore)
            # print(name + ":" + password)
            pyminizip.compress(name, "./", namebefore + ".zip", password, compression_level)




