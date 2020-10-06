
"""
   Example of a class representing a bank account
   and its transactions.

   Author: Johan Öfverstedt
"""

import random

class Money:
    def __init__(self, n=None):
        if isinstance(n, int):
            self.n = n*100
        elif isinstance(n, float):
            self.n = int(round(n * 100))
        elif isinstance(n, type(None)):
            self.n = 0
        else:
            raise ValueError('Number is neither integer-valued or float')
    
    def is_zero(self):
        return self.n == 0
    
    def is_positive(self):
        return self.n > 0

    def is_negative(self):
        return not (self.is_zero() or self.is_positive())

    def __add__(self, other):
        assert type(other) is Money
        res = Money(None)
        res.n = self.n + other.n
        return res
    
    def __sub__(self, other):
        assert type(other) is Money
        res = Money(None)
        res.n = self.n - other.n
        return res
        
    def __str__(self):
        first = self.n // 100
        second = self.n % 100

        s = f'{first}.{second}'
        return s

    def __repr__(self):
        return f'Money({self.__str__()})'

class Account:
    def __init__(self, name, account_number, overdraft_allowed):
        self.name = name
        self.account_number = account_number
        self.overdraft_allowed = overdraft_allowed
        self.amount = Money(None)
        self.transactions = []
    
    def deposit(self, amt):
        assert isinstance(amt, Money)

        if amt.is_positive():
            self.amount = self.amount + amt
            self.transactions.append(('d', amt, self.amount))
        elif amt.is_zero():
            raise ValueError('A zero deposit is not a transaction.')
        else:
            raise ValueError('A negative deposit should be a withdrawal.')

    def withdraw(self, amt):
        assert isinstance(amt, Money)

        if amt.is_positive():
            new_amount = self.amount - amt
            if not new_amount.is_negative() or self.overdraft_allowed:
                self.amount = new_amount
                self.transactions.append(('w', amt, self.amount))
            else:
                self.transactions.append(('f', amt, self.amount))
                raise ValueError('No overdrafts are allowed.')
        elif amt.is_zero():
            raise ValueError('A zero withdrawal is not a transaction.')
        else:
            raise ValueError('A negative withdrawal should be a deposit.')

    def print_history(self):
        print(f'Account history for account {self.account_number} belonging to {self.name}')
        print('Type             Amount       Total')
        for transaction_type, amt, total in self.transactions:
            s1 = str(amt)
            s2 = str(total)
            if transaction_type == 'd':
                print(f'Deposit:           {s1:>11s} {s2:>11s}')
            elif transaction_type == 'w':
                print(f'Withdrawal:        {s1:>11s} {s2:>11s}')
            elif transaction_type == 'f':
                print(f'Failed withdrawal: {s1:>11s} {s2:>11s}')

def random_amount(max_value):
    random_value = 0.01 + random.random() * max_value
    return Money(random_value)

if __name__ == '__main__':
    # Change the seed to get different random behavior
    random.seed(54321)

    a = Account('Johan Öfverstedt', '123456789', overdraft_allowed=True)
    a.deposit(Money(100))
    for i in range(50):
        amt = random_amount(100)
        if random.random() < 0.5:
            a.deposit(amt)
        else:
            a.withdraw(amt)
    
    a.print_history()

    b = Account('Johan Öfverstedt', '987654321', overdraft_allowed=False)
    b.deposit(Money(100))
    for i in range(50):
        amt = random_amount(100)
        if random.random() < 0.5:
            b.deposit(amt)
        else:
            try:
                b.withdraw(amt)
            except ValueError as e:
                print(f'*** {e} ***: Withdrawal of {amt} failed.')
    
    b.print_history()

print(b.transactions)