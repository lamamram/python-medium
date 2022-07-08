import pytest
from bank import Account, Client

# account_set = [
#     (Account(k, Client(k)), b) 
#     for k, b in {1: 500.00, 2: 300.00}.items()
# ]

# def test_balance(account_1):
#     assert 500.00 == account_1.getBalance()

# pb si on paramètres les fixtures et les paramètres de fonctions
# pb si on crée plusieurs paramètres de fonctions
# => autant de test que le produit cartésiens => les tests croisés seront faux

# @pytest.mark.parametrize("acc,balance", account_set)
def test_balance(acc, balance):
    assert balance == acc.getBalance()


def test_alt_balance(test_balance):
    assert test_balance["balance"] == test_balance["account"].getBalance()

def test_overdraft(account_1: Account):
    account_1.withdraw(600)
    assert account_1.overdraft