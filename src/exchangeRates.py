from abc import ABC, abstractmethod
from collections import UserDict

class Field(ABC):
    def __init__(self, value: str|float) -> None:
        self.value = value

    @property
    def value(self) -> str|float:
        return self._value
    
    @value.setter
    def value(self, value: str|float) -> None:
        if self._is_valid(value):
            self._value = value

    @abstractmethod
    def _is_valid(self, value: str|float) -> bool:
        pass


class Currency(Field):
    def _is_valid(self, value: str) -> bool:
        if (type(value) is str and
            value.isalpha() and
            len(value) == 3):
            return True
        else:
            raise ValueError("Incorrect currency")

class Rate(Field):
    def _is_valid(self, value: float) -> bool:
        if type(value) is float:
            return True
        else:
            raise ValueError("Incorrect rate")

class ExchangeRate:
    def __init__(self,
                 currency: str,
                 sale_rate: float,
                 purchase_rate: float)  -> None:

        self.currency = Currency(currency)
        self.sale_rate = Rate(sale_rate)
        self.purchase_rate = Rate(purchase_rate)
        

class ExchangeRates(UserDict):
    def add_currency(self, cur: ExchangeRate) -> None:
        self.data.update({cur.currency.value: cur})

    def get_currency(self, cur: str):
        return self.data.get(cur)
