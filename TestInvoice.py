import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5,'tax': 10},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10, 'tax': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalucateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalucateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalucateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanCalucateTotalTax(invoice,products):
    invoice.totalTax(products)
    assert invoice.totalTax(products) == 7.5

def test_CanCalucateTotalWithTax(invoice, products):
    invoice.totalWithTax(products)
    assert invoice.totalWithTax(products) == 76.88
