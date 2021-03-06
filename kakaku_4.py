

import requests
import sys
from encodings import utf_8, utf_8_sig
from time import sleep
import pandas as pd
from common import common_api

args=sys.argv
shopName=args[0]

def get_api4():
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
            # 初めの30文字だけを出力させる
            "商品名":str(itemName[:30])+"...",
            "価格":itemPrice,
            "URL":itemUrl},
            ignore_index=True
        )
        
    df.to_csv("楽天ランキング一覧.csv",encoding="utf_8_sig",index=False)
    
get_api4()
