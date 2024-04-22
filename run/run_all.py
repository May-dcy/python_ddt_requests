'''
此模块是用来生成测试报告，并且发送报告到邮箱`
'''
import time
import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner
from utils.handle_path import *
from library.mail3 import SendMail

#定义生成报告的路径和文件
new = time.strftime('%Y-%m-%d-%H-%M-%S')
filename = report_path+'\\' + str(new)+"_api_report.html"
def auto_run():
    discover = unittest.defaultTestLoader.discover(
        start_dir=testcase_path,
        pattern='test_*.py')

    f = open(filename,'wb')
    runner = HTMLTestRunner(
        stream=f,
        title='cms平台接口自动化测试报告',
        description="用例执行情况如下",
        tester="dcs"
    )
    runner.run(discover)
    f.close()
def sendMail():
    sm = SendMail(send_msg=filename,attachment=filename)
    sm.send_mail()
if __name__ == '__main__':
    auto_run()
    sendMail()