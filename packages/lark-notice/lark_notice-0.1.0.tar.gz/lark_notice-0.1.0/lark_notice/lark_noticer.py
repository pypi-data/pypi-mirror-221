import requests
from pprint import pprint
class LarkNoticer:
    def __init__(self) -> None:
        pass

    def hello():
        print("hello")

    def req_get(url="http://www.baidu.com", params={}):
        rsp = requests.get(url, params=params)
        pprint(rsp)