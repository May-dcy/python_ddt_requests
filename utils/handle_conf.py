from configparser import ConfigParser
from utils.handle_path import *

'''
 定义了一个名为Handle_conf的新类，它继承自ConfigParser类。
 这意味着Handle_conf类将具有ConfigParser类的所有功能和属性。
 当前这个类是用来处理conf.ini文件的工具类
'''
class Handle_Conf(ConfigParser):

    def __init__(self,filename):
        super(Handle_Conf,self).__init__()#继承父类的构造方法
        self.filename=filename#把传进来的形式参数赋值给到实例变量self.filename
        self.read(self.filename)#打开ini文件进行读取

    # 获取ini文件中的section下面对应的option的value值
    def get_value(self, section, option,):
        value=self.get(section,option)
        return value

path=os.path.join(conf_path,"conf_cms.ini")#读取的文件路径
conf=Handle_Conf(path)#创建对象读取ini
#print(conf.get_value('env','url'))  #调试下查看的 url
#print(conf.get_value('env','headers')) #调试下查看的 headers

