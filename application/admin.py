from django.contrib import admin

from application.models import register
class registerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','age','phoneno','password']

admin.site.register(register,registerAdmin)
    
