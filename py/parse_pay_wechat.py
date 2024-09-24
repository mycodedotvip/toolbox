import csv
import os
import sys

def main(args):
    
# 打开 CSV 文件
with open('example.csv', mode='r', encoding='utf-8') as file:
    # 使用 csv.reader 读取文件
    csv_reader = csv.reader(file)
    
    # 遍历每一行
    for row in csv_reader:
        print(row)  # 打印每一行内容

