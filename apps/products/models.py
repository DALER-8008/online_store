from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils import shared


class Brand(shared.SlugBasedModel):
    class Meta:
        app_label = 'products'
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.title


class Category(shared.SlugBasedModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'products'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Product(shared.BaseModel, shared.SlugBasedModel):
    # TODO: type product field and ikpu field
    store = models.ForeignKey('store.Store', on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey('products.Brand', on_delete=models.CASCADE, related_name='products')
    model = models.CharField(_('model'), max_length=150)
    color = models.CharField(_('color'), max_length=30)
    country = models.CharField(_('country'), max_length=30)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductImage(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/images/%Y/%m/%d/')

    class Meta:
        app_label = 'products'
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')
