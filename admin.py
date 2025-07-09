from django.contrib import admin
from resturent.models import Contact, booking, veg_item, non_veg_item, Dessert, Cold_Drink
# Register your models here.
admin.site.register(Contact)

admin.site.register(booking)

admin.site.register(veg_item)

admin.site.register(non_veg_item)

admin.site.register(Cold_Drink)

admin.site.register(Dessert)

