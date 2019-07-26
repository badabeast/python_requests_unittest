"""
当A调用B时
os.getcwd  返回的是最外层的路径：A文件所在的路径
os.path.dirname(__file__)返回的是.py文件的目录
os.path.abspath(__file__)返回的是.py文件的绝对路径（完整路径）

os.path.realpath()先处理路径中的符号链接，再返回绝对路径
linux 中重定向文件显示  b -> a
用os.path.realpath()  显示b
os.path.abspath(__file__)  返回a
"""
import os


def get_path():
    path = os.path.dirname(os.path.abspath(__file__))
    return path


if __name__ == '__main__':  # 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', get_path())
