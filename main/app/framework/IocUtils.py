import ioc

class IocUtils:
    container = None

    @staticmethod
    def init():
        print("init ioc")
        IocUtils.container = ioc.build(['resource/services.yml'])
        for serviceName in IocUtils.container.services:
            try:
                service = IocUtils.container.get(serviceName)
                service.autowired()
            except Exception:
                pass
        for serviceName in IocUtils.container.services:
            try:
                service = IocUtils.container.get(serviceName)
                service.postConstruct()
            except Exception:
                pass

    @staticmethod
    def getBean(beanName):
        return IocUtils.container.get(beanName)

