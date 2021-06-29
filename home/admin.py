from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Mobile
from .models import Laptop
# from .models import New_Product
from .models import New_Product2
from .models import Searched_item


admin.site.register(Product)   
admin.site.register(Mobile)
admin.site.register(Laptop)
# admin.site.register(New_Product)
admin.site.register(New_Product2)
admin.site.register(Searched_item)