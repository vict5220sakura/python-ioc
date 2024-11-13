from flask import Blueprint

from main.app.framework.IocApi import IocApi

class TestController(IocApi):
    api = Blueprint('api', __name__)

    def autowired(self):
        pass

    def postConstruct(self):
        pass

    @staticmethod
    @api.route("/test1")
    def test1():
        return "i am python"
