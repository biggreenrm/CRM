from django.contrib import admin
from .models import Partnership


@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_display = ("company1", "company2", "start_date")