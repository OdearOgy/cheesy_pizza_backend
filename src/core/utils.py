
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist
from uuid import uuid4
import time

def unique_slug_generator(instance, name, slug_field):
    name_date = f'{name} {uuid4()}'
    slug = slugify(name_date)
    return slug


def save_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name, instance.slug)


def img_path(instance, filename, *args, **kwargs):
    inst__class = instance.__class__
    path = inst__class.__name__
    try:
        folder = inst__class._default_manager.latest('pk').pk + 1
    except ObjectDoesNotExist:
        folder = 1
    name=int(time.time() * 10)
    extension=filename.split('.')[-1]

    return f'{path}/img/{folder}/{name}.{extension}'

