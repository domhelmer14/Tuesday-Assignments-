class Checklist:
    def __init__(self, header, entries):
        self.header = header
        self.entries = entries

class Customer:
    def __init__(self, id, balance, discount):
        self.id = id
        self.balance = balance
        self.discount = discount

class Cable:
    def __init__(self, model, length, max_speed, bidirectional):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional


checklist = Checklist("Grocery List", ["Apples", "Bananas", "Carrots"])
customer = Customer("C123", 150.75, 10)
cable = Cable("ModelX", 2.5, 1000, True)

print(f"Checklist Header: {checklist.header}, Entries: {checklist.entries}")
print(f"Customer ID: {customer.id}, Balance: {customer.balance}, Discount: {customer.discount}")
print(f"Cable Model: {cable.model}, Length: {cable.length}, Max Speed: {cable.max_speed}, Bidirectional: {cable.bidirectional}")
