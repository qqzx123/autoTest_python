import requests

class request:
    header={
        "content-type":"application/json",
        "Authorization":"你的token地址"
    }
    otherHeader={
        "content-type":"application/json",
        "Authorization":"另外一个人的token地址"
    }
    def do_get(self,url,isMyToken):
        if isMyToken=="true":
            get = requests.get(url=url,headers=self.header)
        else:
            get = requests.get(url=url,headers=self.otherHeader)
        result = get.text
        return result

    def do_post(self,url,para,isMyToken):
        if isMyToken=="true":
            post = requests.post(url,para,headers=self.header)
        else:
            post = requests.post(url,para,headers=self.otherHeader)
        result = post.text
        return result

# jiekou=request()
# response =jiekou.do_get("http://www.baidu.com")
# print(response)
