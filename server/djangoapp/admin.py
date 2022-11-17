from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ()
    list_filter = ['year',"Type"]
=======
    list_display = ('name', 'year', "Type")
    list_filter = ['year', "Type"]
>>>>>>> 503844a5246934b36e25e3addf59128248af2c63
    search_fields = ['name', 'dealer_id']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
<<<<<<< HEAD
    list_display = ()
=======
    list_display = ('name')
>>>>>>> 503844a5246934b36e25e3addf59128248af2c63
    search_fields = ['name', 'description']

# Register models here

admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)