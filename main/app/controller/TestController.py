from flask import Blueprint

from main.app.framework.IocApi import IocApi
from main.app.framework.IocUtils import IocUtils

from PIL import Image

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
