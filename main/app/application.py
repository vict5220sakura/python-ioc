import os
import sys
# 获取当前工作目录
current_working_directory = os.getcwd()
# 打印输出到控制台
print("当前工作目录: {}".format(current_working_directory))
sys.path.append(current_working_directory)

from flask import Flask

from main.app.config.Common import Common
from main.app.controller.TestController import TestController
from main.app.framework.IocUtils import IocUtils


class Application:
    flaskApp = Flask(__name__)

    @staticmethod
    def run():
        print("init app")
        Common.init()

        IocUtils.init()

        Application.flaskApp.register_blueprint(TestController.api)
        Application.flaskApp.run(port=Common.serverPort, debug=False)

if __name__ == '__main__':
    Application.run()
