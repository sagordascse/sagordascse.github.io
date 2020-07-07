from django.contrib import admin

# Register your models here.
from .models import product,Contact,myUserProductOrder,trackerOrder

admin.site.register(product)
admin.site.register(Contact)
admin.site.register(myUserProductOrder)
admin.site.register(trackerOrder)

