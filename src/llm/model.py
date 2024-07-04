from abc import ABC, abstractmethod

class ModelInterface(ABC):
    @abstractmethod
    def query(self, query):
        pass