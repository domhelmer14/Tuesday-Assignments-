class NumberStats:
    def __init__(self):
        self.numbers = 0

    def add_number(self, number: int):
        self.numbers += 1

    def count_numbers(self):
        return self.numbers


stats = NumberStats()
stats.add_number(3)
stats.add_number(5)
stats.add_number(1)
stats.add_number(2)
print("Numbers added:", stats.count_numbers())  
