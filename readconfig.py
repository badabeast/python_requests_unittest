import os
import configparser
from getpathinfo import get_path

path = get_path()
config_path = os.path.join(path, 'config', 'config.ini')  # 获取config文件夹下的config.ini文件

config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法 初始化实例
config.read(config_path, encoding='utf-8')  # 读取config文件


class ReadConfig(object):
    # 从config.ini中读取需要的数据
    def __init__(self):
        self.server = config.get('APP', 'ServerModel')
        self.email_on_off = config.get

    def get_http(self, name=None):  # 0测试服，1预发布，2正式服，
        if self.server == '0':
            self.url = config.get('TestHttp', name)
        elif self.server == '1':
            self.url = config.get('preHttp', name)
        elif self.server == '2':
            self.url = config.get('ReleaseHttp', 'baseurl')
        else:
            print("服务器选择错误，0测试服，1预发布，2正式服，目前选择", self.server)
        return self.url

    def get_mysql(self, name):  # 写好，留以后备用。但是因为我们没有对数据库的操作，所以这个可以屏蔽掉
        sqlvalue = config.get('Local_Database', name)
        return sqlvalue

    def get_email(self, name):
        emailvalue = config.get('EMAIL', name)
        return emailvalue


if __name__ == '__main__':
    print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))
    print('目前连接的数据库为：', ReadConfig().get_mysql('host'))
    test = ReadConfig().get_email('host')
    print('邮件的收件人有：', test)
