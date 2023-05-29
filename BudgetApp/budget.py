class Category:
    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.total_expenses = 0
        self.available_money = 0
        self.ledger = []

    def deposit(self, amount, *args):
        self.amount += amount
        self.available_money += amount
        amount = '{:.2f}'.format(self.amount)
        if len(args) > 0:
            description = args[0]

            self.add_to_ledger(amount, description)
            return {"amount": self.amount, "description": f"{description}"}

        else:
            self.add_to_ledger(amount)
            return {"amount": self.amount, "description": ""}

    def add_to_ledger(self, *args):
        amount = str(args[0])
        description = ""
        max_descript = 23
        max_amount = 7
        new_desc = ""
        new_ligne_ledger = ""

        if len(args) > 1:
            description = str(args[1])

            if len(description) > max_descript:
                for i, j in enumerate(description):
                    new_desc += description[i]
                    if i == max_descript - 1:
                        description = new_desc
                        new_ligne_ledger += description
                        break

        space_found = 30 - (len(description) + len(amount))
        if space_found > 0:
            message = f"{description}{space_found * ' '}{amount}"
        else:
            message = f"{description}{amount}"

        self.ledger.append(message + "\n")

    def withdraw(self, amount, *args):
        if len(args) != 0:
            description = args[0]

        else:
            description = ""

        if self.check_funds(amount):

            self.available_money -= amount
            self.total_expenses += amount
            self.add_to_ledger("-" + str(amount), description)
            return True

        else:

            return False

    def get_balance(self):
        return self.available_money

    def transfer(self, transfer_amount, destination_category):
        if self.check_funds(transfer_amount):
            transfer_description = f"Transfer to {destination_category.name}"
            self.withdraw(transfer_amount, transfer_description)

            deposit_description = f"Transfer from {self.name}"
            destination_category.deposit(transfer_amount, deposit_description)
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.available_money - amount < 0:
            return False
        elif self.available_money - amount >= 0:
            return True

    def __str__(self):
        number_of_stars = 30 - len(self.name)
        if number_of_stars % 2 == 0:
            stars_begin = int(number_of_stars / 2)
            stars_end = int(number_of_stars / 2)
        else:
            stars_begin = int(number_of_stars / 2) + 1
            stars_end = int(number_of_stars / 2)

        ticket = f"{stars_begin * '*'}{self.name}{stars_end * '*'}""\n"

        for item in self.ledger:
            ticket += item
        available_money = '{:.2f}'.format(self.available_money)
        ticket += f"Total: {available_money}"
        print(self.amount)
        return ticket


def create_spend_chart(categories):
    pass
