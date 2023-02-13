from django.contrib import admin
from .models import Currency, Wallet, User

# Register your models here.
admin.site.register(User)
admin.site.register(Currency)
admin.site.register(Wallet)