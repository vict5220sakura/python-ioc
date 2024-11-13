from abc import ABC, abstractmethod

class IocApi(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def autowired(self):
        print("ioc autowired")

    @abstractmethod
    def postConstruct(self):
        print("ioc postConstruct")

