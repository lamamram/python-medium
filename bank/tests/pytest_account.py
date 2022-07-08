import pytest
from bank import Account, Client

# appliquer des marqueurs à tous les tests
# pytestmark = [
#     pytest.mark.usefixtures("debug")
# ]

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

@pytest.mark.truc
def test_alt_balance(test_balance):
    assert test_balance["balance"] == test_balance["account"].getBalance()

# @pytest.mark.skip
# @pytest.mark.xfail
# ajout de fixtures non resources: ex debug
# @pytest.mark.usefixtures("debug")
@pytest.mark.truc
def test_overdraft(account_1: Account):
    account_1.withdraw(600)
    assert account_1.overdraft

# paramétrage du mock
@pytest.mark.parametrize("firstname,lastname", [("michel", "lefebvre")])
def test_client_name(account_1: Account, firstname, lastname, monkeypatch):
    # création du mock
    class ClientMock:
        def get_full_name(self):
            return f"{firstname.capitalize()} {lastname.upper()}"
    # remplacement de la dépendance lente par le mock
    monkeypatch.setattr(account_1, "_Account__client", ClientMock())
    assert "Michel LEFEBVRE" == account_1.get_client_name()