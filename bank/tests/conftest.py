import pytest
from bank import Account, Client


account_set = [
    (Account(k, Client(k)), b) 
    for k, b in {1: 500.00, 2: 300.00}.items()
]

# CMD: pytest path/to/tests -v (verbose) -q (quiet) --tb=no (pas de code d'erreur)

## autouse: la fixture est chargée 
# dans toutes les fixtures et fcts de test

##
# scope: périmétre d'utilisation d'une fixture
# avant suppression (function, class, module, package, session (pytest))
# attention aux tests qui modifient la fixture si scope large
@pytest.fixture(autouse=True, scope="package")
def client_1():
    c = Client(1)
    yield c
    # code de cleanup
    print("released !")
    del c

@pytest.fixture(scope="package")
def account_1():
    return Account(1, client_1)

@pytest.fixture(scope="package", params=[1, 2])
def account(request):
    return Account(request.param, Client(request.param))

# fonction globale de stratégie de test pytests
def pytest_generate_tests(metafunc):
    if "balance" in metafunc.fixturenames and "acc" in metafunc.fixturenames:
        metafunc.parametrize("acc,balance", account_set)