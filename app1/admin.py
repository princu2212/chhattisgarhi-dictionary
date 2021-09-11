from django.contrib import admin
from .models import Contact, AddWord

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'query')

@admin.register(AddWord)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','hindi', 'english', 'chhattisgarhi')

