class Strings:
    def ___init__(self):
        self.name=''
    def get_name(self):
        self.name=input("Enter name:")
    def print_name(self):
        print(self.name.upper())
def test_case():
    s=Strings()
    s.get_name()
    s.print_name()
test_case()