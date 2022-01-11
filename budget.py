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
        f_string = f"{self.category:*^30}\n"
        for item in self.ledger:
            f_string += f"{item['description'][:23]: <23}{item['amount']: >7.2f}\n"
        else:
            f_string += f"Total: {self.get_balance():.2f}\n"
        return f_string

#bar plot function
def create_spend_chart(categories) -> None:

    total_balance = 0
    per = 0
    for each_category in categories:
        total_balance += each_category.total_spend
    y_axes_indices = ["100|", "90|", "80|", "70|", "60|", "50|", "40|", "30|", "20|", "10|", "0|"]
    Total_string = "Percentage spent by category\n"

    for i in range(11):
        Total_string += f"{y_axes_indices[i]: >4}"
        for each_category in categories:
            per = int((10*each_category.total_spend)/(total_balance))
            if (10-per) > i: Total_string += '   '
            else: Total_string += ' o '
        Total_string += "\n"
    else:
        str1 = "    " + "-"*(3*len(categories)+1) +"\n"
        Total_string += str1
    
    max_len = max(len(x.category) for x in categories)
    str2 = []
    for ele in categories:
        str2.append(ele.category.ljust(max_len, ' '))
    for i in range(max_len):
        Total_string += "    "
        for ele in str2:
            Total_string += f" {ele[i]} "
        Total_string += "\n"
    return Total_string


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
print(create_spend_chart([food, entertainment, clothing]))