import pytest
from ..models import Cheese

pytestmark = pytest.mark.django_db


def test___str__():
    cheese = Cheese.objects.create(
        name='HashimCheese',
        description='Newly created test cheese',
        firmness=Cheese.Firmness.SEMI_HARD
    )
    assert cheese.__str__() == 'HashimCheese'
    assert str(cheese) == 'HashimCheese'
