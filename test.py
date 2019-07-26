# import os
# import getpathinfo  # 自己定义的内部类，该类返回项目的绝对路径
# # 调用读Excel的第三方库xlrd
# from xlrd import open_workbook
#
# # # 拿到该项目所在的绝对路径
# # path = getpathinfo.get_Path()
# #
# # class readExcel():
# #     def get_xls(self, xlsx_name, sheet_name):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
# #         cls = []
# #         # 获取用例文件路径
# #         xlsPath = os.path.join(path,'testCase',xlsx_name)
# #         file = open_workbook(xlsPath)  # 打开用例Excel
# #         sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
# #         # 获取这个sheet内容行数
# #         nrows = sheet.nrows
# #         for i in range(nrows):  # 根据行数做循环
# #             if sheet.row_values(i)[0] != u'case_name':  # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
# #                 cls.append(sheet.row_values(i))
# #         return cls
# #
# #
# #

import json
import requests
import urllib
data = {"phone":18701890657,
        "smsCode":"171204",
        "channel":"IPAD"
        }
print(type(data))
json1=json.dumps(data)
print(type(json1))
print(json1)
json2 = json.load(json1)
print(type(json2))
print(json2)
jsoN3= urllib.re
#
# #
# #
# # coding:utf-8
# import smtplib
# import sys
# from email.mime.text import MIMEText
# a='A@163.com','B@163.com'
# print(a)
# mailto_list=list(a)   #收件人邮箱列表
# mail_user="user@163.com"       #用户名
# mail_passwd="passwd"           #用户登录密码（第三方登录授权码）
# mail_host="smtp.163.com"      #邮箱服务器
# mail_postfix="163.com"        #邮箱后缀名
# #
# def send_mail(to_list,sub,content): #定义函数，参数为收件人，邮件主题，邮件内容
#     print(content)
#     me="<"+mail_user+">"
#
#     msg=MIMEText(content,'plain')
#     msg['Subject']=sub
#     msg['From']=me
#     msg['To']=';'.join(to_list)    #将收件人列表以“;” 形式隔开
#     print(msg)
#     try:
#          server = smtplib.SMTP_SSL()    #用的是SSL协议的邮箱smtp
#          server.connect(mail_host,465)  #smtp 的端口号465
#          print(server.login(mail_user,mail_passwd))
#          server.sendmail(me,to_list,msg.as_string()) #SMTP对象使用sendmail 方法发送邮件 #SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]
#          server.close()
#     except Exception as e:
#         print(str(e))
#     return False
# #
# # send_mail(mailto_list,"Long time no see",'happy new year,beautiful girl') #调用函数
#
#
# import urllib.parse
# #urlparse将url分为6个部分
# url ="https://i.cnblogs.com/EditPosts.aspx?opt=1"
# url_change = urllib.parse.urlparse(url) # 将url拆分为6个部分
# query = url_change.query #取出拆分后6个部分中的查询模块query
# lst_query = urllib.parse.parse_qsl(query)  #使用parse_qsl返回列表
# dict1 =dict(lst_query)  #将返回的列表转换为字典
# dict_query =urllib.parse.parse_qs(query)  #使用parse_qs返回字典
# print("使用parse_qsl返回列表  ：",lst_query)
# print("将返回的列表转换为字典 ：",dict1)
# print("使用parse_qs返回字典   : ",dict_query)
#
# # data = "test=test&test2=test2&test2=test3"
# # print(urllib.parse.parse_qsl(data)) #返回列表
# # print(urllib.parse.parse_qs(data))  #返回字典
# a=3910+3510+3410
# print(a)
#



# import unittest
# import paramunittest
#
# # 方案二
# @paramunittest.parametrized(
#     ('1', '2'),
#     # (4, 3),
#     ('2', '3'),
#     (('4',), {'b': '5'}),
#     ((), {'a': 5, 'b': 6}),
#     {'a': 5, 'b': 6},
# )
# class TestBar(unittest.TestCase):
#     def setParameters(self, a, b):
#         self.a = a
#         self.b = b
#
#     def testLess(self):
#         print("第一个参数", self.a)
#         self.assertLess(self.a, self.b)
#
#
# if __name__ == "__main__":
#     unittest.main()
