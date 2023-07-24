from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils import shared


class Wishlist(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='wishlist')
    products = models.ManyToManyField('products.Product')

    class Meta:
        app_label = 'orders'
        verbose_name = _('Wishlist')
        verbose_name_plural = _('Wishlists')


class Cart(shared.BaseModel):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='cart')
    products = models.ManyToManyField('products.Product', through='orders.CartItem')

    @property
    def total(self):
        return sum([product.subtotal for product in self.products.all()])

    class Meta:
        app_label = 'orders'
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')


class CartItem(models.Model):
    cart = models.ForeignKey('orders.Cart', on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.product.price * self.quantity

    class Meta:
        app_label = 'orders'
        verbose_name = _('Cart Item')
        verbose_name_plural = _('Cart Items')


class Order(shared.BaseModel):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        SHIPPED = 'shipped', 'Shipped'
        DELIVERED = 'delivered', 'Delivered'
        CANCELLED = 'cancelled', 'Cancelled'

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField('products.Product', through='orders.OrderItem')
    status = models.CharField(_('status'), max_length=30, choices=Status.choices, default=Status.PENDING)
    address = models.CharField(_('address'), max_length=150)

    @property
    def total(self):
        return sum([product.subtotal for product in self.products.all()])

    class Meta:
        app_label = 'orders'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class OrderItem(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.product.price * self.quantity

    class Meta:
        app_label = 'orders'
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')
