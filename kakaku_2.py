'''
課題6-2 任意のキーワードでAPIを検索した時の 商品名と価格の一覧を取得してみましょう
'''
from typing import ItemsView
from urllib import response
from pytest import Item
import requests
import sys
from encodings import utf_8
from time import sleep
import math
import pandas as pd
from common import common_api

args=sys.argv
shopName=args[0]

def get_api2():
    search_word="鬼滅"
    url='https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
    params={
    "applicationId":1081905647609311133,
    "hits":30,
    "keyword":str(search_word),
    "page":1
    }
    resp=common_api(url,params)
    
    '''
    最大件数を受け取り、ページ数を表示させる
    '''
    
    total=int(resp['count'])
    max_page=math.ceil(total/30)
    print(f"商品数:{total}")
    print(f"ページ数:{max_page}")
    print ("===================================")
    
    count=0
    for i in resp['Items']:
        count+=1    
        Item=i["Item"]
        itemName=Item['itemName']
        itemPrice=Item['itemPrice']
        print(count)
        print(f"商品名:{itemName}")
        print(f"価格:{itemPrice}")
        print ("-----------")

get_api2()
