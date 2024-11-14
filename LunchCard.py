class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60

    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60


card = LunchCard(50)
print(card) 

card.eat_lunch()
print(card)  

card.eat_special()
card.eat_lunch()
print(card) 


card = LunchCard(4)
print(card) 

card.eat_lunch()
print(card)  

card.eat_lunch()
print(card)  
