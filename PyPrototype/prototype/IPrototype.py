from abc import ABC, abstractmethod

class IPrototype(ABC):

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def deep_clone(self):
        pass
