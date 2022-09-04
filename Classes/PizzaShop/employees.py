"""Example of inheritance."""


class Employee:
    def __init__(self, name: str, salary: int = 0) -> None:
        self.name = name
        self.salary = salary

    def giveRaise(self, percent: float):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(f'{self.name} does stuff')

    def __repr__(self) -> str:
        return f'<Employee: {self.name}, {self.salary}>'


class Chef(Employee):
    def __init__(self, name: str) -> None:
        Employee.__init__(self, name, 50000)

    def work(self):
        print(f'{self.name} makes food')


class Server(Employee):
    def __init__(self, name: str) -> None:
        Employee.__init__(self, name, 40000)

    def work(self):
        print(f'{self.name} interfaces with customer')


class PizzaRobot(Chef):
    def __init__(self, name: str) -> None:
        Chef.__init__(self, name)

    def work(self):
        print(f'{self.name} makes pizza')


if __name__ == '__main__':
    bob = PizzaRobot('bob')
    print(bob)
    bob.work()
    bob.giveRaise(0.20)
    print(bob)

    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()
