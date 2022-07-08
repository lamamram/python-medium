import pytest
from bank import Account, Client


account_set = [
    (Account(k, Client(k)), b) 
    for k, b in {1: 500.00, 2: 300.00}.items()
]

acc_bal = [{"account": 1, "balance": 500.00}, {"account": 2, "balance": 300.00}]
# CMD: pytest path/to/tests -v (verbose) -q (quiet) --tb=no (pas de code d'erreur)
#      -k "balance and not alt"
#      -m custom_markers (cf pytest.ini)
#      --durations=n ou --duration-min=0.5 => tests lents
# avec pip install pytest-xdist , -n nb_workers => exécution en parallèle

## autouse: la fixture est chargée 
# dans toutes les fixtures ???? et fcts de test

##
# scope: périmétre d'utilisation d'une fixture
# avant suppression (function, class, module, package, session (pytest))
# attention aux tests qui modifient la fixture si scope large
@pytest.fixture(autouse=True, scope="function")
def client_1():
    c = Client(1)
    yield c
    # code de cleanup
    print("released !")
    del c

@pytest.fixture(scope="function")
def account_1(client_1):
    return Account(1, client_1)

@pytest.fixture(scope="package", params=[1, 2])
def account(request):
    return Account(request.param, Client(request.param))

# fixture mêlant objets à tester et résultats attendus
@pytest.fixture(scope="package", params=acc_bal)
def test_balance(request):
    return {
        "account": Account(
            request.param["account"], 
            Client(request.param["account"])
        ), 
        "balance": request.param["balance"]
    }

@pytest.fixture
def debug(request):
    print(request.getfixturevalue("account_1"))
    yield
    print("end")

# fonction globale de stratégie de test pytests
def pytest_generate_tests(metafunc):
    if "balance" in metafunc.fixturenames and "acc" in metafunc.fixturenames:
        metafunc.parametrize("acc,balance", account_set)