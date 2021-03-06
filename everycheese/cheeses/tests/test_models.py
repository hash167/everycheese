import pytest
from .factories import CheeseFactory

pytestmark = pytest.mark.django_db


def test___str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name


def test_get_absolute_url():
    cheese = CheeseFactory()
    assert cheese.get_absolute_url() == f'/cheeses/{cheese.slug}/'
