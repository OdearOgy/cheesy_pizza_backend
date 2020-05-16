from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=1720, blank=True)
    phone_code = models.CharField(max_length=25, blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_fullname(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_phone(self):
        return f'{self.phone_code} {self.phone_number}'


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
