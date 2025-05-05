class Bank:

    # Class variable shared by all objects

    bank_name = "HBL Bank"

    # Class method to change the bank name

    @classmethod

    def change_bank_name(cls, name):

        cls.bank_name = name

# Create two objects of Bank class

user1 = Bank()

user2 = Bank()

# Display bank name from both objects before change

print("Before change:")

print("User1's Bank:", user1.bank_name)

print("User2's Bank:", user2.bank_name)

# Change bank name using class method

Bank.change_bank_name("UBL Bank")

# Display bank name from both objects after change

print("\nAfter change:")

print("User1's Bank:", user1.bank_name)

print("User2's Bank:", user2.bank_name)
