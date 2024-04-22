#coding=utf-8

import unittest
from ddt import ddt,data
from utils.handle_excel import Handle_Excel
from utils.handle_path import *
import os
from utils.handle_conf import conf
from utils.handle_requests import Send_requests
from utils.handle_login import Cms_login
'''
ddt模块
打开dos窗口：输入 pip install ddt  进行下载
ddt模块：是用来做数据驱动的
ddt装饰器：用来装饰类
data装饰器：用来装饰方法的
装饰器的原理：就是闭包，闭包就是函数里面定义一个函数，外面的函数称为外函数，里面的函数称为内函数
外函数中返回内函数的函数名，也就是返回内函数的地址，内函数里面写装饰器的逻辑
'''
case_file = os.path.join(data_path,'data.xlsx')

@ddt
class Test_Login(unittest.TestCase):
    excel = Handle_Excel(case_file,'updateLoginPwd')
    cases = excel.read_data()  #一个列表当中是5个字典，每个字典都是一个用例
    # print(cases)
    request = Send_requests()  #创建了一个发送接口请求的对象
    @classmethod
    def setUpClass(cls) -> None:
        cls.request = Cms_login().login()  #调用登录接口
    @data(*cases)
    def test_02_updateLoginPwd(self,case):
        '''封装登录接口''' #数据要从Excel表格里面拿
        # 1.准备接口的入参
        url = conf.get_value('env','url')+case['url']
        # eval()  函数是用来执行一个字符串表达式，并返回表达式的值
        headers = eval(conf.get_value('env','headers'))
        method = case['method']
        data = eval(case['data'])
        excepted = eval(case['excepted'])
        case_id = case['case_id']
        case_id = case_id+1  #记录当前跑了几条用例

        # 2.发送接口请求
        response = self.request.send(method=method,url=url,data=data,headers=headers)
        result = response.json()
        # print(result)
        # 3.对接口的响应内容进行断言
        try:  #try尝试去执行代码
            self.assertEqual(excepted['msg'],result['msg'])  #断言期望结果和实际结果是否一直
            self.assertEqual(excepted['code'],result['code'])
        except Exception as e: #捕捉异常
            self.excel.write_excel(case_id,8,'未通过')
            print(e)
        else:
            self.excel.write_excel(case_id,8,'通过')
if __name__ == '__main__':
    unittest.main()