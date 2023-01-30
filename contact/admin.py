from django.contrib import admin
from .models import Contact
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'body', 'created_on')
    search_fields = ('name', 'email', 'subject', 'body')

    def approve_contact(self, request, queryset):
        queryset.update(approved=True)
