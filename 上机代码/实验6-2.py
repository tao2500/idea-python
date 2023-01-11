class Name:
    name = None

    def __init__(self, name):
        self.name = name

    def getLastName(self):
        return self.name[5:10]

    def split(self):
        return self.name.split()

    def lower(self):
        return self.name.lower()


aName = Name("John Green")
print(aName.getLastName())
print(aName.split())
print(aName.lower())
