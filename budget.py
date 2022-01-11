class Category:

    def __init__(self, category) -> None:
        self.category = category
        self.ledger = []
        self.balance = 0
        self.total_spend = 0

    def deposit(self, amount, description = ""):
        self.ledger.append(dict({"amount": amount, "description": description}))
        self.balance += amount

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append(dict({"amount": -amount, "description": description}))
            self.balance -= amount
            self.total_spend += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, budget_catageory):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_catageory.category}")
            budget_catageory.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.balance<amount:
            return False
        else:
            return True

    def __str__(self):
        print(f"{self.category:*^30}")

        def print_it(self):
            for item in self.ledger:

                print(f"{item['description'][:23]: <23}{item['amount']: >7.2f}")
            else:
                print(f"Total: {self.get_balance(): .2f}")
        
        print_it(self)
        return ""

#bar plot function
def create_spend_chart(category_list) -> None:

    total_balance = 0
    per = 0
    for each_category in category_list:
        total_balance += each_category.total_spend
    y_axes_indices = ["100|", "90|", "80|", "70|", "60|", "50|", "40|", "30|", "20|", "10|", "0|"]
    print("Percentage spent by category")

    for i in range(11):
        f_string = f"{y_axes_indices[i]: >4}"
        for each_category in category_list:
            per = int((10*each_category.total_spend)/(total_balance))
            if (10-per) > i: f_string += '   '
            else: f_string += ' o '
        print(f_string)
    else:
        print("    " + "-"*(3*len(category_list)))
    
    max_len = max(len(x.category) for x in category_list)
    str = []
    for ele in category_list:
        str.append(ele.category.ljust(max_len, ' '))
    for i in range(max_len):
        f_str = "    "
        for ele in str:
            f_str += f" {ele[i]} "
        print(f_str)


#Instant tion
food = Category("food")
clothing = Category("clothing")
entertainment = Category("entertainment")

#some operations
food.deposit(1000, "initial deposite")
entertainment.deposit(1000, "initial deposite")
food.transfer(200, clothing)
clothing.transfer(300, food)
clothing.deposit(2000.3486985, "extra money")
entertainment.transfer(300, clothing)
clothing.transfer(100, food)
entertainment.withdraw(200, "watched radhe")

#printing output
print(food)
print(clothing)
print(entertainment)

#creating bar plot
create_spend_chart([food, entertainment, clothing])