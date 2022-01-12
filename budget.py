class Category:

    #this is the class's init method, where three important variables are being initalised
    def __init__(self, category: str) -> None:
        self.category = category
        self.ledger = []
        self.balance = 0
        self.total_spend = 0

    #this is the deposite method which will deposite the ask amount in the used category, and 
    #add description and add the amount to the total balance in that category
    def deposit(self, amount: int, description = "") -> None:
        #run validations to recived arguments
        assert amount >= 0, f"inputed amount {amount} is less that zero, invalid"

        self.ledger.append(dict({"amount": amount, "description": description}))
        self.balance += amount

    #this withdraw method does same as deposite, but first it checks if the transction is possible or not
    #and then subtracts that amount from total balance and adds that amount to total_spend instance variable 
    def withdraw(self, amount: int, description = "") -> bool:
        #run validations to recived arguments
        assert amount >= 0, f"inputed amount {amount} is less that zero, invalid"

        if self.check_funds(amount):
            self.ledger.append(dict({"amount": -amount, "description": description}))
            self.balance -= amount
            self.total_spend += amount
            return True
        else:
            return False

    def get_balance(self) -> int:
        return self.balance

    #transfer method transfers(withdraws) the specified amount to the specified category and
    # withdraws the same amount from the used category, if possible. And then adds
    #description to the transcation
    def transfer(self, amount: int, budget_catageory: object) -> bool:
        #run validations to recived arguments
        assert amount >= 0, f"inputed amount {amount} is less that zero, invalid"
        assert isinstance(budget_catageory, Category), f"inputed budget_category {budget_catageory} is not an object which has be instantioned"

        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_catageory.category}")
            budget_catageory.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount: int) -> bool:
        #run validations to recived arguments
        assert amount >= 0, f"inputed amount {amount} is less that zero, invalid"

        if self.balance<amount:
            return False
        else:
            return True

    #printing, when asked, in the specified pattern
    def __str__(self) -> str:
        f_string = f"{self.category:*^30}\n"
        for item in self.ledger:
            f_string += f"{item['description'][:23]: <23}{item['amount']: >7.2f}\n"
        f_string += f"Total: {self.get_balance():.2f}\n"
        return f_string

#bar plot function
def create_spend_chart(categories: list) -> str:
    #run validations to recived arguments
    assert type(categories) == list, f"inputed categories {categories} is not a list, invalid"

    total_balance = 0
    per = 0 #percentage spend value representing variable
    #getting the total spend for all mentioned categories to calculate per
    for each_category in categories:
        total_balance += each_category.total_spend
    y_axes_indices = ["100|", "90|", "80|", "70|", "60|", "50|", "40|", "30|", "20|", "10|", "0|"]
    Total_string = "Percentage spent by category\n" #main string variable that will be added and then returned

    for i in range(11):
        Total_string += f"{y_axes_indices[i]: >4}"
        for each_category in categories:
            per = int((10*each_category.total_spend)/(total_balance)) 
            if (10-per) > i: 
                Total_string += '   '
            else: #filling the bar plot, but only from bottom
                Total_string += ' o '
        Total_string += "\n"
    str1 = "    " + "-"*(3*len(categories)+1) +"\n" #x-axis
    Total_string += str1
    
    max_len = max(len(x.category) for x in categories)
    str2 = []
    #filling the smaller category names with ' ' to make it easier to pasre through all of them
    for ele in categories:
        str2.append(ele.category.ljust(max_len, ' '))
    #creating the x-indices in the specific manner
    for i in range(max_len):
        Total_string += "    "
        for ele in str2:
            Total_string += f" {ele[i]} "
        Total_string += "\n"
    return Total_string


#Instanttion
food = Category("food")
clothing = Category("clothing")
entertainment = Category("entertainment")
auto = Category("auto")

#some operations
food.deposit(1000, "initial deposite")
entertainment.deposit(1000, "initial deposite")
food.transfer(200, clothing)
clothing.transfer(-300, food)
clothing.deposit(2000.3486985, "extra money")
entertainment.transfer(300, clothing)
clothing.transfer(100, food)
entertainment.withdraw(200, "watched radhe")
entertainment.transfer(300, auto)
auto.withdraw(100, "travel to thearter")
auto.deposit(400, "some extra balance")


#printing output
print(food)
print(clothing)
print(entertainment)
print(auto)

#creating bar plot
print(create_spend_chart([food, entertainment, clothing, auto]))