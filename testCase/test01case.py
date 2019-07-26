import json
import unittest
from common.commonhttp import RunMain
import paramunittest
import geturlparams
import urllib.parse
from logging_method import LoggingMethod
import readexcel
from common.commoncode import common_errorcode
logger = LoggingMethod(__name__).getlogger()
url = geturlparams.GetUrlParams().get_url()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = (readexcel.ReadExcel().get_xlsx("interface_usecases.xlsx", "login"))


@paramunittest.parametrized(*login_xls)  # 登录接口
class UserLogin(unittest.TestCase):
    def setParameters(self, case_module, case_name, note, path, method, query, status):
        """
        与xlsx的列名一致
        set params
        :param case_module
        :param case_name
        :param note
        :param path
        :param method
        :param query
        :param status
        :return:
        """
        self.case_module = str(case_module)
        self.case_name = str(case_name)
        self.note = str(note)
        self.path = str(path)
        self.method = str(method)
        # self.query = str(query)
        self.query = query
        self.status = str(status)

    def description(self):
        """
        test report description
        :return:
        """
        print(self.case_name+"正在测试登录模块")
        logger.info(self.case_name+"正在测试登录模块")

    def setUp(self):
        """
        :return:
        """
        full_url = url + self.query
        self.data_list = dict(urllib.parse.parse_qsl(
            urllib.parse.urlsplit(full_url).query))  # 将一个完整的URL中的name=&pwd=转换为{"name":"xxx","pwd":"bbb"}
        self.info = RunMain().run_main(self.method, url, self.data_list)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        print(self.case_name + "准备开始测试")
        logger.info(self.case_name + "准备开始测试")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        """
        check test result
        :return:
        """
        # url1 = url
        # new_url = url1 + self.query
        # data_list = dict(urllib.parse.parse_qsl(
        #     urllib.parse.urlsplit(new_url).query))  # 将一个完整的URL中的name=&pwd=转换为{"name":"xxx","pwd":"bbb"}
        # info = RunMain().run_main(self.method, url, data_list)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        # print(self.case_name, "的json响应结果" + "\n", info)
        if self.info is not None and self.info != "":
            ss = json.loads(self.info)  # 将响应转换为字典格式
            common_errorcode(ss)
            if self.case_name == "login_success":  # 如果case_name是login_success，说明合法，返回的code应该为200
                if (ss["success"]) is True and ss["errorCode"] == 0:
                    self.assertIsNotNone(ss["data"]["accessToken"])
                    self.assertEqual(ss["data"]["type"], 3)
                    self.assertEqual(ss["data"]["phone"], self.data_list["phone"])
                    self.assertIsNotNone(ss["data"]["id"])

        # except Exception as erq:
        #     print(self.case_name, erq)
        # else:
        #     print("目前执行的测试用例：", self.case_name)
        #     print("断言失败")
        # finally:
        #     logger.info("testcase01 结束")
        else:
            logger.error("响应结果为空")


if __name__ == "_main":

    unittest.main()
