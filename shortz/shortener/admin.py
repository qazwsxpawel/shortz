from django.contrib import admin
from shortener.models import URLEntry

class URLEntryAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('full_url', )
    list_filter = ('code', )

admin.site.register(URLEntry, URLEntryAdmin)
