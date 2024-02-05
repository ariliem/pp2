class Str:
    def get_string(self):
         self.string = input()

    def print_string(self):
        print(self.string.upper())

x = Str()
x.get_string()
x.print_string()