from django.contrib import admin
from vs.models import person
from vs.models import citizenship, children

class personAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age', 'email', 'dob','is_married')
    
admin.site.register(person,personAdmin)

class citizenAdmin(admin.ModelAdmin):
    list_display = ('citizenship_no','person')
    
admin.site.register(citizenship, citizenAdmin)

class childrenAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age', 'parents')
    
admin.site.register(children,childrenAdmin)
# Register your models here.
