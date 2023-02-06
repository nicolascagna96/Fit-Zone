from django.contrib import admin
from .models import Plan

# Register your models here.

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    """This class defines admin page for the Workout Plan Service"""
    fields = (
        'first_name',
        'last_name',
        'phone_number',
        'email_address',
        'your_goal',
        'plan_type',)
    list_display = ('first_name', 'last_name', 'plan_type', 'your_goal')
