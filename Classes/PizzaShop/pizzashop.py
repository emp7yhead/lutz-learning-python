"""Example of composition."""
from employees import PizzaRobot, Server


class Customer:
    def __init__(self, name) -> None:
        self.name = name

    def order(self, server):
        print(f'{self.name} orders from {server}')

    def pay(self, server):
        print(f'{self.name} pays for item to {server}')


class Oven:
    def bake(self):
        print('oven bakes')


class PizzaShop:
    def __init__(self) -> None:
        self.server = Server('Pat')
        self.oven = Oven()
        self.chef = PizzaRobot('Bob')

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == '__main__':
    scene = PizzaShop()
    scene.order('Homer')
    print('...')
    scene.order('Shaggy')
