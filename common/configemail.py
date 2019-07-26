import smtplib
import os
import sys
from email.mime.text import MIMEText
from readconfig import ReadConfig
import datetime
import getpathinfo

# 读取配置文件

read_conf = ReadConfig()
# 从配置文件中读取，smtp服务器、端口、发件人、密码、收件人、抄送人
smtp = read_conf.get_email("host")
port = read_conf.get_email("port")
user = read_conf.get_email("user")
pwd = read_conf.get_email("pwd")
addressee = read_conf.get_email("addressee")
# addressee=list(addressee.split(";"))


chaosong = read_conf.get_email("chaosong")
# 从配置文件中读取，邮件主题
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
subject = "hello,这是" + now + read_conf.get_email("subject")
print(subject)
mail_path = os.path.join(getpathinfo.get_path(), 'result', 'report.html')  # 获取测试报告路径

content = "<h1>测试报告来咯！</h1>"


class SendEmail(object):
    def aliyun(self):
        # 构造邮件
        msg = MIMEText(content, "html", "gbk")  # msg邮件对象
        msg['Subject'] = subject
        msg['From'] = user
        msg['to'] = addressee
        msg['Accept-Language'] = 'zh-CN'
        msg['Accept-Charset'] = 'ISO-8859-1,utf-8'

        # 发送邮件
        try:
            ss = smtplib.SMTP_SSL(smtp, port)
            ss.login(user, pwd)
            ss.sendmail(user, addressee, msg.as_string())  # 发送
            print("发送成功！")
        except Exception as e:
            print("发送失败！详情：", e)


if __name__ == "__main__":
    print(subject)
    SendEmail().aliyun()
