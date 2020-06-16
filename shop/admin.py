from django.contrib import admin

from .models import Item, OrderItem, Order, Address, UserProfile, PopularItem, ChoiceItem, Address, ContactForm



class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']



admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(ChoiceItem)
admin.site.register(PopularItem)
admin.site.register(Address)
admin.site.register(ContactForm)
