# -*- coding: utf-8 -*-
import os
import time
import calendar
import hashlib
import json
import requests

# 获取任务的详细信息
# name 任务中文名 必填
# code 资产编号 必填
# options 额外参数 非必填
def get_task_detail(name, code, options):
    params = {"code": code, "name": name, "options": options}

    sign, userName, timestamp, appSign = _get_sign()
    headers = {"VG-Request-User": userName, "VG-Request-Sign": sign,
               "VG-Request-Time": str(timestamp)}
    url = 'http://mvango.37wan.com/openapi/task/detail'

    response = requests.get(url=url, params=params, headers=headers)
    if response.status_code == 200:
        return json.loads(response.text)
    return response.json()

# 上传文件
# task_id 任务ID 必填
# file_path 本地文件路径 必填
# options 额外参数 非必填
def upload_task_file(task_id, file_path, options):
    data = {"task_id": task_id, "options": options}

    try:
        with open(file_path, "rb") as upload_file:
            files = {"file": upload_file}

            sign, userName, timestamp, appSign = _get_sign()
            headers = {"VG-Request-User": userName, "VG-Request-Sign": sign,
                       "VG-Request-Time": str(timestamp), "VG-Request-App": "openapi",
                       "VG-Request-AppSign": appSign}
            url = 'http://internal.vango-openapi.data-ad.37ops.com/openapi/task/file_upload'

            response = requests.post(url=url, files=files, data=data, headers=headers)
            if response.status_code == 200:
                return json.loads(response.text)
            return response.json()

    except Exception as e:
            return '文件上传错误：{e}'



def _get_sign():
    user = _get_user_info()
    userName = ''
    password = ''
    if user[0]:
        userName = user[0]
    if user[1]:
        password = user[1]
    timestamp = calendar.timegm(time.gmtime())

    md5 = hashlib.md5()
    md5.update(userName.encode('utf-8'))
    md5.update(password.encode('utf-8'))
    md5.update(str(timestamp).encode('utf-8'))
    sign = md5.hexdigest().upper()

    appSignStr = _get_app_sign()
    md5 = hashlib.md5()
    md5.update(appSignStr.encode('utf-8'))
    md5.update(str(timestamp).encode('utf-8'))
    appSign = md5.hexdigest().upper()

    return sign, userName, timestamp, appSign


def _get_user_info():
    if os.path.exists(r"c:\tmp\user.txt"):
        userFile = r"c:\tmp\user.txt"
    elif os.path.exists(r"C:\tmp\user.txt"):
        userFile = r"C:\tmp\user.txt"
    else:
        userFile = r'./user.txt'
    user = []
    if os.path.exists(userFile):
        with open(userFile, 'r') as f:
            userInfo = f.read()
            f.close()
            user = userInfo.split(' ')
    return user

def _get_app_sign():
    signFile = './sign.txt'
    sign = 'S*zVvcWOU*2p7$H%'
    if os.path.exists(signFile):
        with open(signFile, 'r') as f:
            sign = f.read()
            f.close()
    return sign