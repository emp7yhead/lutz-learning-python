class AttrDisplay:
    """
    Show name of the instance and
    pair key=value for attributes of instance.
    """
    def gatherAttributes(self) -> str:
        attributes = []
        for key in sorted(self.__dict__):
            attributes.append(f'{key}={getattr(self, key)}')
        return ', '.join(attributes)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.gatherAttributes()}'


if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)
