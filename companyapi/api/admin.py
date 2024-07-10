from django.contrib import admin
from api.models import Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'name', 'location', 'about', 'type', 'added_date', 'active')

admin.site.register(Company, CompanyAdmin)
