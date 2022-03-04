
'''
任意の商品の最安値と最高値を取得してみましょう
'''

from webbrowser import get
import requests
import sys
from encodings import utf_8
from time import sleep
import math
from common import common_api


args=sys.argv
shopName=args[0]

def get_api3():
    search_word="iPhone"
    url='https://app.rakuten.co.jp/services/api/Product/Search/20170426'
    params={
        "applicationId":1081905647609311133,
        "hits":30,
        "keyword":str(search_word),
        "page":1,
        "sort":"-satisfied"
    }

    resp=common_api(url,params=params)
    total=int(resp['count'])
    max_page=math.ceil(total/30)
# マックスのページ数を取得。小数点未満の端数切り上げ
    print(f"商品数:{total}")
    print(f"ページ数:{max_page}")
    print ("===================================")
    print("満足度順で表示します。")


    counter=0
    for i in resp['Products']:
        counter+=1    
        product=i['Product']
        name=product['productName']
        maxprice=product['maxPrice']
        minprice=product['minPrice']

        print(f"満足度No:{counter}")
        print(f"商品名:{name}")
        print(f"最高価格:{maxprice}")
        print(f"最低価格:{minprice}")
        print ("===================================")

get_api3()
    