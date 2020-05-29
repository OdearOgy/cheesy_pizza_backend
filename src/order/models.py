from django.db import models
from django.db.models.signals import pre_save, post_save
from core.utils import unique_slug_generator


class OrderItem(models.Model):
    item = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    slug = models.SlugField(max_length=64, unique=True, blank=True)

    def __str__(self):
        return f'{self.slug}'


    def save_slug(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance, instance.item.name, instance.slug)


pre_save.connect(OrderItem.save_slug, sender='order.OrderItem')


class Order(models.Model):
    processing = 'processing'
    en_route = 'en_route'
    delivered = 'delivered'
    rejected = 'rejected'
    refunded = 'refunded'
    STATUS_CHOICES = (
        (processing, 'processing'),
        (en_route, 'Order En Route'),
        (delivered, 'Delivered'),
        (rejected, 'Rejected'),
        (refunded, 'Refunded'),
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=processing
    )

    cash = 'cash'
    prepaid = 'prep'
    PAYMENT_CHOICES = (
        (cash, 'Cash on Delivery'),
        (prepaid, 'Prepaid Online'),
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default=cash
    )
    items = models.ManyToManyField('order.OrderItem',)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0,)
    delivery_fee = models.DecimalField(max_digits=7, decimal_places=2, default=0,)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=64, unique=True, blank=True)
    
    def __str__(self):
        return f'{self.slug}'

    def get_total_price(self):
        if self.total_price == 0:
            self.total_price = sum(map(lambda o: o.item.price * o.quantity, self.items.all()), self.get_delivery_fee())
            self.save()
        return self.total_price

    def get_delivery_fee(self):
        if self.delivery_fee == 0:
            self.delivery_fee = sum(map(lambda o: (o.item.price * o.item.slices) / o.quantity / 50, self.items.all()))
            self.save()
        return self.delivery_fee

    def save_slug(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance, 'ord', instance.slug)

pre_save.connect(Order.save_slug, sender='order.Order')
