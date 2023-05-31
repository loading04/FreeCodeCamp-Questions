class Category:
    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.total_expenses = 0
        self.available_money = 0
        self.ledger2 = []
        self.ledger = []

    def deposit(self, amount, *args):
        self.amount += amount
        self.available_money += amount

        if len(args) > 0:
            description = args[0]

            self.add_to_ledger('{:.2f}'.format(self.amount), description)

            self.ledger.append({"amount": self.amount, "description": description})
            return {"amount": self.amount, "description": f"{description}"}

        else:
            self.add_to_ledger(amount)
            self.ledger.append({"amount": self.amount, "description": ""})
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

        self.ledger2.append(message + "\n")

    def withdraw(self, amount, *args):
        if len(args) != 0:
            description = args[0]

        else:
            description = ""

        if self.check_funds(amount):

            self.available_money -= amount
            self.total_expenses += amount
            self.ledger.append({"amount": float("-" + str(amount)), "description": description})

            self.add_to_ledger("-" + str('{:.2f}'.format(amount)), description)
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

        for item in self.ledger2:
            ticket += item
        available_money = '{:.2f}'.format(self.available_money)
        ticket += f"Total: {available_money}"
        return ticket


def create_spend_chart(categories):
    cats = {}
    list_cats = []
    for cat in categories:
        if cat.amount == 0:
            cats[cat.name] = 0
        else:
            cats[cat.name] = round((cat.total_expenses * 100) / cat.amount)

    s = "Percentage spent by category\n"

    for i in range(10, -1, -1):
        if i * 10 == 100:
            s += str(i * 10) + "|"
        elif i == 0:
            s += "  0|"
        else:
            s += " " + str(i * 10) + "|"

        for val in cats.values():
            s += " "
            if i * 10 <= val:
                s += "o"
            else:
                s += " "
            s += " "

        s += "\n"

    length = len(cats.values())
    s += f"    {(length * 3 + 1) * '-'} \n"
    i = 0

    greatest_name_length = 0
    for i in categories:
        if len(i.name) > greatest_name_length:
            greatest_name_length = len(i.name)

    for i in range(greatest_name_length):
        s += "    "
        for c in categories:
            if i < len(c.name):
                s += " " + c.name[i] + " "
            else:
                s += "   "
        s += " \n"

    return s
