from django.template.defaultfilters import slugify
import factory
import factory.fuzzy

from ..models import Cheese


class CheeseFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    description = factory.Faker(
        'paragraph', nb_sentences=3, variable_nb_sentences=True
    )
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    firmness = factory.fuzzy.FuzzyChoice([x[0] for x in Cheese.Firmness.choices])

    class Meta:
        model = Cheese
