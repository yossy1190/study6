
import requests

def common_api(url,params):    
    r=requests.get(url=url,params=params)
    resp=r.json()
    return resp