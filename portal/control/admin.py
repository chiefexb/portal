from django.contrib import admin
from django.db import models
from portal.control.models import Assignment,Departament,Order_Kind,Perodic_Type
# Register your models here.
#editable=True
class AssignmentAdmin (admin.ModelAdmin):

admin.site.register(Assignment)
admin.site.register(Departament)
admin.site.register(Order_Kind)
admin.site.register(Perodic_Type)
