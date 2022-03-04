'''
課題6-2 任意のキーワードでAPIを検索した時の 商品名と価格の一覧を取得してみましょう
'''
from common import common_api
from kakaku_2 import *
from kakaku_3 import *
from kakaku_4 import *
import math


def test_common_api():
    search_word="鬼滅"
    url='https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
    params={
    "applicationId":1081905647609311133,
    "hits":30,
    "keyword":str(search_word),
    "page":1
    }
    resp=common_api(url,params)

    assert len(resp['Items'])>=1
    assert resp['Items'][0]['Item']['itemCode']

def test_get_api2():
    search_word="鬼滅"
    url='https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
    params={
    "applicationId":1081905647609311133,
    "hits":30,
    "keyword":str(search_word),
    "page":1
    }
    resp=common_api(url,params)
   
    count=0
    for i in resp['Items']:
        count+=1    
        Item=i["Item"]
        itemName=Item['itemName']
        itemPrice=Item['itemPrice']
    
    assert len(resp['Items'])>=1
    assert resp['Items'][0]['Item']['itemCode']

def test_get_api3():
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
    assert len(resp['Products'])>=1
    assert resp['Products'][0]['Product']['productName']
    assert resp['Products'][0]['Product']['maxPrice']
    assert resp['Products'][0]['Product']['minPrice']
    
    
def test_get_api4():
    df=pd.DataFrame()
    url='https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'

    params={
        'applicationId':1081905647609311133,
        'genreId':100283,
        "page":1,
        'period':'realtime',
    }
    resp=common_api(url,params)

    title=str(resp['title'])
    lastBuildDate=resp['lastBuildDate']
    print(f"ジャンル名:{title}")
    print(f"最終更新時間:{lastBuildDate}")
    print ("===================================")

    for i in resp['Items']:
        Item=i['Item']
        rank=Item['rank']
        itemName=Item['itemName']
        catchcopy=Item['catchcopy']
        itemPrice=Item['itemPrice']
        itemUrl=Item['itemUrl']
        print(f"順位:{rank}")
        print(f"商品名:{itemName}")
        print(f"価格:{itemPrice}")
        print(f"No:{itemUrl}")
        print ("-------------------")
        df=df.append({
            "順位":rank,
            "商品名":str(itemName[:30])+"...",
            "価格":itemPrice,
            "URL":itemUrl},
            ignore_index=True
        )
    df.to_csv("楽天ランキング一覧.csv",encoding="utf_8_sig",index=False)
    
    assert len(resp['Items'])>=1
    assert resp['Items'][0]['Item']['rank']
    assert resp['Items'][0]['Item']['itemName']
    assert resp['Items'][0]['Item']['itemUrl']