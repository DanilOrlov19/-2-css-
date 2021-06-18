from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin

from .models import *



class OilsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='Oils'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class PillsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='Pills'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
class ClayAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='Clay'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
class CosmeticAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='Cosmetic'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Category)
admin.site.register(Clay,ClayAdmin)
admin.site.register(Pills,PillsAdmin)
admin.site.register(Oils,OilsAdmin)
admin.site.register(Cosmetic,CosmeticAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)

