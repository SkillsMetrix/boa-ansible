
from abc import ABC ,abstractmethod


class Bank(ABC):
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass


class SBI(Bank):
    def deposit(self):
        return "deposit done"

    def withdraw(self):
        return "withdraw done"
   
user=SBI()
print(user.deposit())
print(user.withdraw())

 

 