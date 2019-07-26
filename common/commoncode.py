# -*- coding:utf-8 -*-
# :carriere
import json

def common_errorcode(result):
    """
    断言通用code
    只接受 dict类型的响应结果
    """
    print(result)
    print(type(result))
    if result["errorCode"] == 0:
        assert result["success"] is True
        return result["success"]
    elif result["errorCode"] == 103:
        assert result["success"] is False
        assert result["errorMessage"] == "用户名或密码错误，请重试！"
        return result["errorMessage"]
    elif result["errorCode"] == 401:
        assert result["success"] is False
        assert result["errorMessage"] == "验证码错误,请检查"
        return result["errorMessage"]
    elif result["errorCode"] == 407:
        assert result["success"] is False
        assert result["errorMessage"] == "请输入正确的手机号"
        return result["errorMessage"]
    elif result["errorCode"] == 101:
        assert result["success"] is False
        return result["errorMessage"]
    else:
        return result["errorCode"]
