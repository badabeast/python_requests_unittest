from readconfig import ReadConfig
from readexcel import ReadExcel

readconfig = ReadConfig()
path = ReadExcel().get_xlsx('interface_usecases.xlsx', 'login')[0][3]
# print(path)


class GetUrlParams():  # 定义一个方法，将从配置文件中读取的进行拼接
    def get_url(self):
        config_url = readconfig.get_http("baseurl")
        if config_url != 'https://api.aircourses.com':
            new_url = readconfig.get_http('baseurl') + ":" + readconfig.get_http('port') + path+"?"
        else:
            new_url = config_url+"?"
        # logger.info('new_url'+new_url)
        return new_url


if __name__ == '__main__':  # 验证拼接后的正确性
    print(__file__)
    print(GetUrlParams().get_url())
