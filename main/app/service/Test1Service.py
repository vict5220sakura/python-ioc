from main.app.framework.IocApi import IocApi
from main.app.framework.IocUtils import IocUtils


class Test1Service(IocApi):

    def autowired(self):
        self.testJavaApi = IocUtils.getBean("TestJavaApi")

    def postConstruct(self):
        self.testJavaApi.test()

