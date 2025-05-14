class Bank:
    bank_name = "ABC Bank"  # class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Bank Name:", Bank.bank_name)

# Example usage
acc1 = Bank("Ali")
acc2 = Bank("Sara")

acc1.display()
acc2.display()

# Changing bank name using class method
Bank.change_bank_name("XYZ Bank")

print("\nAfter changing bank name:\n")
acc1.display()
acc2.display()
