from django.db import models


class Order(models.Model):
    in_cart = 'cart'
    ordered = 'ordered'
    en_route = 'en_route'
    delivered = 'delivered'
    rejected = 'rejected'
    refunded = 'refunded'
    STATUS_CHOICES = (
        (in_cart, 'In Cart'),
        (ordered, 'Ordered'),
        (en_route, 'Order En Route'),
        (delivered, 'Delivered'),
        (rejected, 'Rejected'),
        (refunded, 'Refunded'),
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=in_cart
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
    item = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    author = models.ForeignKey('profile.Profile', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    delivery_fee = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.item}'