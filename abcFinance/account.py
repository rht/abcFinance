# -*- coding: utf-8 -*-
"""
Created on Mon May  7 14:26:31 2018

@author: christoph
"""

from enum import Enum


class AccountSide(Enum):
    """ Side which the balance of an account falls on """
    DEBIT = 1
    CREDIT = -1
    BALANCED = 0

    def __repr__(self):
        return self.name


class AccountType(Enum):
    ASSET = 1
    LIABILITY = 2
    INCOMEEXPENSE = 3
    GAINLOSS = 4
    STOCK = 5
    FLOW = 6


class Account:
    """ An account has two lists of debit and credit bookings """
    def __init__(self, account_type):
        self.debit = 0
        self.credit = 0
        self.account_type = account_type

    def get_balance(self):
        debitsum = self.debit
        creditsum = self.credit
        if debitsum > creditsum:
            return (AccountSide.DEBIT, debitsum - creditsum)
        elif debitsum == creditsum:
            return(AccountSide.BALANCED, 0)
        else:
            return (AccountSide.CREDIT, creditsum - debitsum)

    def add_debit(self, value):
        self.debit += value

    def add_credit(self, value):
        self.credit += value

    def print_balance(self):
        print('debit', self.debit)
        print('credit', self.credit)


class AccountWithHistory(Account):
    """Account with additional logging of debit/credit history"""
    def __init__(self, account_type):
        super().__init__(account_type)
        self.debit_history = []
        self.credit_history = []

    def add_debit(self, value):
        self.debit += value
        self.debit_history.append(value)

    def add_credit(self, value):
        self.credit += value
        self.credit_history.append(value)
