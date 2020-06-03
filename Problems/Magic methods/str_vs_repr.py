class Transactions:

    def __init__(self, number, funds, status='active'):
        self.number = number
        self.funds = funds
        self.status = status

    def __repr__(self):
        return 'Transaction({}, {})'.format(self.number, self.funds)

    def __str__(self):
        return 'Transaction {} for {} ({})'.format(self.number, self.funds, self.status)


payment = Transactions('00001', 3490.0)
print(payment)

# __repr__ is more for debugging and for developers,
# __str__ is more for users

# if both __repr__ and __str__ are used, __str__ will be picked for print
# if __str__ not present, __repr__ will be called automatically
