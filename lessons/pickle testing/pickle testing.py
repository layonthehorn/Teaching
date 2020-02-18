import pickle


class Testing:
    def __init__(self):
        self.number_one = 1
        self.number_two = 2

    def get_number_one(self):
        print(self.number_one)

    def get_number_two(self):
        print(self.number_two)

    def increase_numbers(self):
        self.number_one += 1
        self.number_two += 1


class_one = Testing()
class_one.increase_numbers()

f = open('data', 'rb+')
pickle.dump(class_one, f)
f.close()

x = open('data', "rb")
y = pickle.load(x)
x.close()

y.get_number_one()
y.get_number_two()

