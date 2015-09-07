from django.contrib import admin
from restaurantapi.models import Menu, MenuItem

class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'chef', 'available']

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'cost_to_make', 'sale_price', 'available', 'menu']

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
