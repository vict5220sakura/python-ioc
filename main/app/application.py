import os

from flask import Flask

from main.app.config.Common import Common
from main.app.controller.TestController import TestController
from main.app.controller.DataApi import DataApi
from main.app.framework.IocUtils import IocUtils


class Application:
    flaskApp = Flask(__name__)

    @staticmethod
    def run():
        print("init app")
        Common.init()

        IocUtils.init()

        Application.flaskApp.register_blueprint(TestController.api)
        Application.flaskApp.register_blueprint(DataApi.api)
        Application.flaskApp.run(port=Common.serverPort, debug=False)

if __name__ == '__main__':
    Application.run()
