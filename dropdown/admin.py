from django.contrib import admin

from .forms import OrderItemForm
from .models import (AllowedCombination, Category, Good, Order, OrderItem,
                     Subcategory)

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Good)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    form = OrderItemForm
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    form = OrderItemForm


admin.site.register(OrderItem, OrderItemAdmin)


class AllowedCombinationAdmin(admin.ModelAdmin):
    list_display = ['cat', 'subcat', 'good', ]


admin.site.register(AllowedCombination, AllowedCombinationAdmin)
