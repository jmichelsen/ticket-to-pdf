from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

from tickets.constants import TICKET_TYPES

class AbstractUser(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    @property
    def type(self):
        return self.__class__.__name__

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __unicode__(self):
        return '{} {} (ID: {})'.format(
            self.first_name, self.last_name, self.pk)


class Seller(AbstractUser):
    pass


class Buyer(AbstractUser):
    pass


class Ticket(models.Model):
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    event_title = models.CharField(max_length=100)
    event_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    event_city = models.CharField(max_length=100, blank=True)
    ticket_type = models.CharField(
        max_length=50, default=1, choices=TICKET_TYPES)
    ticket_details = models.TextField(blank=True, null=True, default='')
    seller = models.ForeignKey(Seller, null=True)
    buyer = models.ForeignKey(Buyer, null=True)

    @property
    def qr_code(self):
        return '{}{}'.format(
            settings.HOSTNAME,
            reverse('tickets:detail', kwargs=({'pk': self.pk}))
        )

