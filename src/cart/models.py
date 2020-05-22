from django.db import models
from django.db.models.signals import post_save



class Cart(models.Model):
    empty = 'empty'
    full = 'full'
    STATE_CHOICES = ((empty, 'Empty'), (full, 'Full'))
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='emp')
    orders = models.ManyToManyField('order.Order', blank=True)
    author = models.OneToOneField('profile.Profile', on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Cart'

    def __str__(self):
        return f'{self.author} {self.state} cart'


def post_save_cart_create(sender, instance, created, *args, **kwargs):
    if created:
        Cart.objects.get_or_create(author=instance)


post_save.connect(post_save_cart_create, sender='profile.Profile')