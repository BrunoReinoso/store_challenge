import pytest


@pytest.fixture
def product_payload():
    return {
        'name': 'camisa nike branca',
        'brand': 'nike',
        'color': 'branca',
        'size': 'G',
        'description': 'camisa branca da nike grande futebol etc',
        'price': 180.50,
    } 