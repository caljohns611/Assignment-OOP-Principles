# question 1 task 1
class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name
        self.__budget = budget
        self.expense = 0

# task 2

    def name(self):
        return self.__name
    
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self.__name = value

    def budget(self):
        return self.__budget
    
    def budget(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Budget must be a non-negative number.")
        self.__budget = value

# task 3

    def add_budget(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount to add must be a non-negative number.")
        self.__budget += amount

    def adjust_budget(self):
        if self.expense > self.__budget:
            raise ValueError("Expenses exceed the budget. Please adjust expense or budget.")
        self.__budget -= self.expense

# task 4

    def display(self):
        ramaining_budget = self.__budget - self.expense
        print(f"Budget Category: {self.__name}")
        print(f"Allocated Budget: ${self.__budget:.2f}")
        print(f"Total Expenses: ${self.expense:.2f}")
        print(f"Remaining Budget: ${ramaining_budget:.2f}")

if __name__=="__main__":
    category = BudgetCategory("Grocieries", 500)

    category.expense = 200

    category.display()