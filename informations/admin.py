from django.contrib import admin
from .models import InformationsModel
# Register your models here.

class InformationsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'family', 'phone', 'email']

    class Meta:
        model = InformationsModel

admin.site.register(InformationsModel, InformationsAdmin)