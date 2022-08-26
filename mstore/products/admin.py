from django.contrib import admin
from . import models
# Register your models here.


class Salam(admin.ModelAdmin):
    # list_display = [
    #     "name",
    #     "price",
    #     "count",
    #     "description",
    #     "category",
    # ]
    mahdi_display = [i.name for i in models.Product._meta.get_fields()]
    mahdi_display.remove('id')
    mahdi_display.remove('image')
    list_display = mahdi_display
    # list_filter = mahdi_display
    # search_fields = mahdi_display
    # list_per_page = 20


admin.site.register(models.SubCategory)
admin.site.register(models.Category)
admin.site.register(models.Product, Salam)
