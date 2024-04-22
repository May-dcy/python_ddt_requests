# 封装一个登录的公共方法
from utils.handle_conf import conf
from utils.handle_requests import Send_requests
class Cms_login():
    def login(self):
        request = Send_requests()
        url = conf.get_value('env','url')+"/manage/loginJump.do"
        data = {
            "userAccount":"admin",
            "loginPwd":"123456"}
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        response = request.send(method='post',url=url,data=data,headers=headers)
        return request