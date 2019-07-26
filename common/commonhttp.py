import json
import requests
from common.commoncode import common_errorcode
# import geturlparams


class RunMain(object):
    def __init__(self):

        self.usr_header = {'User-Agent': 'iPadN/84 CFNetwork/711.2.23 Darwin/14.0.0',
                           'Content-type': 'application/json'
                           }

    def send_get(self, url, data, usr_header=None):
        if usr_header is None:
            usr_header = self.usr_header
        result = requests.get(url=url, data=data, headers=usr_header)
        get_res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return get_res

    def send_post(self, url, data, usr_header=None):  # 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        data = json.dumps(data)
        if usr_header is None:
            usr_header = self.usr_header
        result = requests.post(url=url, data=data, headers=usr_header)
        result = result.json()
        post_res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)  # 转换成字符串
        return post_res

    def run_main(self, method, url=None, data=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        method = method.replace(" ", "").replace("\r", "").replace("\n", "").lower()
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("目前支持get 和post,method值错误！！！")
        return result


if __name__ == "__main__":
    json_result = RunMain().run_main("post", "http://192.168.10.209:18087/ac-common/oauth/sms/stu",
                                     '{"phone":18701890657,"smsCode":"171204","channel":"IPAD"}')
    print(json_result)
    print(json.loads(json_result)["errorMessage"])
