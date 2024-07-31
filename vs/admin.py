from django.contrib import admin
from vs.models import person
class personAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age', 'email', 'dob','is_married')
    
admin.site.register(person,personAdmin)
# Register your models here.
