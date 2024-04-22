'''
此模块是用来封装发送接口请求的工具类
'''

import  requests

'''封装了一个发送接口请求的工具类'''
class Send_requests(object):
    '''用来保持会话'''
    def __init__(self):#
        # 始化方法，创建一个 requests Session 对象，用来保持 HTTP 会话，这样可以在同一个会话中发送多个请求
        self.session=requests.Session()

    def send(self,method,url,data=None,json=None,params=None,headers=None):
        method=method.lower()#把接口的请求方法改为小写
        if method=="get":
            response=self.session.get(url=url,params=params)
        elif method=="post":
            response=self.session.post(url=url,data=data,headers=headers)
        elif method=="post_json":
            response=self.session.post(url=url,json=json,headers=headers)
        elif method=="delete":
            response=self.session.delete(url=url,data=data)
        return response

































































