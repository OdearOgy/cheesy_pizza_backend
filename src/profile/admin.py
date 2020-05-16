from django.contrib import admin

# Register your models here.
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_fullname')
    # ordering = ('-creation_date', )


admin.site.register(Profile, ProfileAdmin)
