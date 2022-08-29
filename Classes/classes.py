from typing import Optional

from classtools import AttrDisplay


class Person(AttrDisplay):
    def __init__(
        self,
        name: str,
        job: Optional[str] = None,
        pay: int = 0
    ):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent: float):
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    def __init__(self, name: str, pay: int = 0):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent: float, bonus: float = .10):
        Person.giveRaise(self, percent+bonus)  # Source code extension


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
