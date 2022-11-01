from django.contrib import admin

# Register your models here.

from .models import Name, Biography, What_is_famous

admin.site.register(Name)
admin.site.register(Biography)
admin.site.register(What_is_famous)
