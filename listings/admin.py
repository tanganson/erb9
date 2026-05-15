from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',"doctor",)
    list_display_links = ('id', 'title',)
    list_filter = ('doctor','services',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'doctor__name', 'services', 'address', 'district')
    list_per_page = 25
    
admin.site.register(Listing, ListingAdmin)