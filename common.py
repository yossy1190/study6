
'''

各課題で共通しているapiを叩く作業は、ここに集約

'''

import requests

def common_api(url,params):    
    r=requests.get(url=url,params=params)
    resp=r.json()
    return resp
