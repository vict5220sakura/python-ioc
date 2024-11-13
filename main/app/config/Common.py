import re
import sys
import yaml
from main.app.framework.IocApi import IocApi

class Common(IocApi):
    serverPort = None
    env = "dev"

    def autowired(self):
        pass

    def postConstruct(self):
        pass

    @staticmethod
    def init():
        for param in sys.argv[1:]:
            try:
                Common.env = re.match("-env=.*$", param, flags=0).group(0)[5:]
            except Exception:
                pass
        if Common.env is None:
            Common.env = "dev"

        print("init Common")
        with open('resource/application-' + Common.env + '.yml', 'r') as file:
            data = yaml.safe_load(file)

        Common.serverPort = data["server"]["port"]

