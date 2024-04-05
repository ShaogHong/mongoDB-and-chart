# coding: UTF-8
"""
@IDE     ：PyCharm 
@Author  ：娄南湘先生
@Date    ：2024/4/5,0005 0:36 
"""
import subprocess
import webbrowser

# 启动allQuery_api.py
api_process = subprocess.Popen(['python', 'allQuery_api.py'])

# 打开浏览器访问 http://localhost:63342/py_mongoDB_work/index.html
webbrowser.open('http://localhost:63342/py_mongoDB_work/index.html')

# 等待用户手动关闭allQuery_api.py
api_process.wait()
