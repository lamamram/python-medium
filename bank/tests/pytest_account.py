import pytest
from bank import Account, Client

# CMD: pytest path/to/tests -v (verbose) -q (quiet)

## autouse: la fixture est chargée 
# dans toutes les fixtures et fcts de test

##
# scope: périmétre d'utilisation d'une fixture
# avant suppression (function, class, module, package, session (pytest))
# attention aux tests qui modifient la fixture si scope large
@pytest.fixture(autouse=True, scope="module")
def client_1():
    c = Client(1)
    yield c
    # code de cleanup
    print("released !")
    del c

@pytest.fixture(scope="module")
def account_1():
    return Account(1, client_1)

def test_balance(account_1):
    assert 500.00 == account_1.getBalance()

def test_overdraft(account_1: Account):
    account_1.withdraw(600)
    assert account_1.overdraft