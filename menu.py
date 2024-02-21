class Translation:
    def __init__(self, number):
        self.number = number

    def get_num(self):
        return self.number

    def set_num(self, number):
        self.number = number

    def translate_num_8x(self):
        return oct(self.number)

    def translate_num_16x(self):
        return hex(self.number)

    def translate_num_2x(self):
        return bin(self.number)

num1 = Translation(int(10))
print(num1.get_num())
# print(num1.set_num())
print(num1.translate_num_8x())
print(num1.translate_num_16x())
print(num1.translate_num_2x())