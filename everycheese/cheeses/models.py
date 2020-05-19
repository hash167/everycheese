from autoslug import AutoSlugField
from django.db import models
from model_utils.models import TimeStampedModel
from django.urls import reverse
from django.conf import settings

from django_countries.fields import CountryField


class Cheese(TimeStampedModel):

    def get_absolute_url(self):
        """Return the absolute url of the Cheese Detail page"""
        return reverse(
            'cheeses:detail',
            kwargs={'slug': self.slug}
        )

    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"

    name = models.CharField('Name of Cheese', max_length=255)
    slug = AutoSlugField(
            'Cheese Address', unique=True,
            always_update=False, populate_from='name')
    description = models.TextField('description of cheese', blank=True)
    firmness = models.CharField('firmness', max_length=20,
                                choices=Firmness.choices,
                                default=Firmness.UNSPECIFIED)
    country_of_origin = CountryField(
        "Country of Origin", blank=True
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name
