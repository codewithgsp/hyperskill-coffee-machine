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
