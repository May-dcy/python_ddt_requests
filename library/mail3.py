#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

class SendMail:
    def __init__(self, send_msg,
                 smtpserver="smtp.163.com", sender="dumay24@163.com",
                 psw="AIWLNDVBBJJCJXCF", receiver="dumay24@163.com",   #psw这个为授权码
                 port=25, attachment=None):
        # self.reportfile = reportfile
        self.send_msg = send_msg
        self.smtpserver = smtpserver
        self.sender = sender
        self.psw = psw
        self.receiver = receiver
        self.port = port
        self.attachment = attachment

    def send_mail(self):
        """发送最新的测试报告内容"""
        #打开测试报告，读取测试报告内容
        with open(self.send_msg, "rb") as f:
            mail_boday = f.read()
        #定义邮件
        msg = MIMEMultipart()
        msg['subject'] = Header(u"自动化测试报告", 'utf-8')
        msg['From'] = Header(self.sender, 'utf-8')
        msg['To'] = self.receiver

        #添加附件
        if self.attachment != None:
            file_name = self.attachment.split(os.path.sep)[-1]
            att = MIMEText(open(self.attachment, "rb").read(), "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att.add_header('Content-Disposition', 'attachment', filename = file_name)
            msg.attach(att)

        body = MIMEText(mail_boday, _subtype="html", _charset='utf-8')
        msg.attach(body)
        smtp = smtplib.SMTP()
        smtp.set_debuglevel(1)
        smtp.connect(self.smtpserver, self.port)
        #用户登录并发送邮件
        smtp.login(self.sender, self.psw)
        smtp.sendmail(self.sender, self.receiver, msg.as_string())
        smtp.quit()


