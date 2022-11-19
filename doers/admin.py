from django.contrib import admin

# Register your models here.

from .models import Doer, Biography, Success

admin.site.register(Doer)
admin.site.register(Biography)
admin.site.register(Success)
