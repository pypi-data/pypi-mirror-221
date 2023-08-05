import os
from requests.exceptions import (
    InvalidSchema,
)
import requests
from urllib.parse import urlparse
from urllib.parse import urlencode

class HttpQuerier:
    def __init__(self, host="localhost", isSSL=False):
        self.host = host
        self.isSSL = isSSL

    def getQueryUrl(self, mydsUrl):
        parsed_url = urlparse(mydsUrl)
        scheme = parsed_url.scheme  # 获取协议
        if scheme != "myds":
            raise InvalidSchema(f"Requires 'myds' protocol for {mydsUrl!r}")
        prot = "http"
        if self.isSSL:
            prot += "s"
        port = parsed_url.port
        if port is None:
            port = 5149
        hostname = parsed_url.hostname  # 获取域名和端口
        params = {"dbName": hostname};
        urlStr = f'{prot}://{self.host}:{port}/query?' + urlencode(params)
        args = parsed_url.query  # 获取查询字符串
        if args != "":
            urlStr += "&" + args
        return urlStr

    def query(self, mydsUrl):
        urlStr = self.getQueryUrl(mydsUrl);
        res = requests.get(urlStr).text
        if res.startswith("[error]"):
            raise ConnectionError(res)
        parsed_url = urlparse(mydsUrl)
        path = parsed_url.path
        if path != "":
            if res.startswith("/"):
                res = res[0:-1]
            while len(path) >= 3 and path[0:3] == "/..":
                res = os.path.dirname(res)
                path = path[3:]
            res += path
        return res

def simpleQuery(dsName):
    return HttpQuerier().query(f'myds://{dsName}')