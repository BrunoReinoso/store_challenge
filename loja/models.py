from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    EXTRA_SMALL = 'PP'
    SMALL = 'P'
    MEDIUM = 'M'
    LARGE = 'G'
    EXTRA_LARGE = 'GG'
    SIZE_CHOICES = (
        (EXTRA_SMALL, 'PP'),
        (SMALL, 'P'),
        (MEDIUM, 'M'),
        (LARGE, 'G'),
        (EXTRA_LARGE, 'GG'),
    )
    name = models.CharField(_('name'), max_length=50)
    brand = models.CharField(_('brand'), max_length=50)
    color = models.CharField(_('color'), max_length=50)
    size = models.CharField(_('size'), max_length=3, choices=SIZE_CHOICES)
    description = models.CharField(_('description'), max_length=100)
    price = models.DecimalField(
        _('price'), max_digits=5, decimal_places=2, default=1.99
    )
    image = models.ImageField(_('image'), upload_to='loja')

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return f'{self.name}'
