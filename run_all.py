import os
import common.HTMLTestRunner as HTMLTestRunner
import getpathinfo
import unittest
import readconfig
from common.configemail import SendEmail
from datetime import datetime
from logging_method import LoggingMethod
# from apscheduler.schedulers.blocking import BlockingScheduler
# import pythoncom

# import common.Log

send_mail = SendEmail()
path = getpathinfo.get_path()
report_path = os.path.join(path, 'result')
on_off = readconfig.ReadConfig().get_email('on_off')
logger = LoggingMethod(__name__).getlogger()


class AllTest:  # 定义一个类AllTest
    def __init__(self):  # 初始化一些参数和数据
        global resultName
        now = datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
        resultName = str(report_path+'\\'+now+'_report.html')
        # resultName = str(os.path.join(report_path,"report.html"))
        self.caseListFile = os.path.join(path, "caselist.txt")  # 配置执行哪些测试文件的配置文件路径
        self.caseFile = os.path.join(path, "testCase")  # 真正的测试断言文件路径
        self.caseList = []
        logger.info("resultNmae", resultName)
        logger.info("caseListFile", self.caseListFile)
        logger.info("caseList", self.caseList)

    def set_case_list(self):
        """
        读取caselist.txt文件中的用例名称，并添加到caselist元素组
        :return:
        """
        fb = open(self.caseListFile, 'r', encoding='utf-8')
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):  # 如果data非空且不以#开头
                self.caseList.append(data.replace("\n", ""))  # 读取每行数据会将换行转换为\n，去掉每行数据中的\n
        fb.close()
        return self.caseList

    def set_case_suite(self):
        """
        :return:
        """
        self.set_case_list()  # 通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:  # 从caselist元素组中循环取出case
            case_name = case.split("/")[-1]  # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            logger.info(case_name + ".py")  # 打印出取出来的名称
            # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)  # 将discover存入suite_module元素组
        if len(suite_module) > 0:  # 判断suite_module元素组是否存在元素
            for suite in suite_module:  # 如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:  # 从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
        else:
            logger.info('目前suit_module无数据')
            return None
        return test_suite  # 返回测试集

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()  # 调用set_case_suite获取test_suite
            print('try')
            if suit is not None:  # 判断test_suite是否为空
                print('if-suit')
                rf = open(resultName, 'wb')  # 打开result/20181108/report.html测试报告文件，如果不存在就创建
                # rf = open('F:/python+request+unittest/result/report.html', 'wb')
                # 调用HTMLTestRunner
                runner = HTMLTestRunner.HTMLTestRunner(stream=rf, title='Test Report', description='Test Description')
                runner.run(suit)
                rf.close()
            else:
                print("Have no case to test.")
                logger.info("Have no case to test")
        except Exception as ex:
            print("运行出错", __name__, str(ex))
            logger.error("运行出错", __name__, str(ex))

            # log.info(str(ex))

        finally:
            print("*********TEST END*********")
            logger.info("*********TEST END*********")

        # 判断邮件发送的开关
        if on_off == 'on':
            send_mail.aliyun()
        else:
            print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")


# scheduler = BlockingScheduler()
# scheduler.add_job(AllTest().run, 'cron', day_of_week='1-5', hour=14, minute=59)
# scheduler.start()


if __name__ == '__main__':
    AllTest().run()
    # AllTest()
