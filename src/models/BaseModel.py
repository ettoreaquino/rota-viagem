from abc import ABC, abstractmethod


class BaseModel(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()