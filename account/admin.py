from django.contrib import admin
from account.models import Profile


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'married',
        'education',
        'birth_date',
        'phone_num',
        'street',
    ]
