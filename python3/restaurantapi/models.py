from django.contrib.auth.models import User
from django.db import models

from .validators import validate_acceptable_cost_to_make


class Menu(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=200)
    chef = models.ForeignKey(User)
    available = models.BooleanField(default=False)

    def __str__(self):
        return '%s by %s %s' % (self.name, self.chef.first_name, self.chef.last_name)


class MenuItem(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=200)
    cost_to_make = models.DecimalField(decimal_places=2, max_digits=5, validators=[validate_acceptable_cost_to_make])
    sale_price = models.DecimalField(decimal_places=2, max_digits=5)
    available = models.BooleanField(default=False)
    menu = models.ForeignKey(Menu)

    def profit(self):
        return str(self.sale_price - self.cost_to_make)

    def __str__(self):
        return '%s' % (self.name)
