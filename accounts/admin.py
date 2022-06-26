from django.contrib import admin

from accounts.models import Patient,CartItem

# Register your models here.
admin.site.register(Patient)
admin.site.register(CartItem)

