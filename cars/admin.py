from django.contrib import admin
from .models import Car

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'color', 'description')
    search_fields = ('title', 'color')
    list_filter = ('color',)


admin.site.register(Car, CarAdmin)