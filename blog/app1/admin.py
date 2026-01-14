from django.contrib import admin
from .models import Category, Post ,Comment, Contact

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'date', 'is_read']
    list_filter = ['is_read', 'date']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'date']
    
    # This shows fields when you click on a contact
    fields = ['name', 'email', 'subject', 'message', 'date', 'is_read']
    
    def mark_as_read(self, request, queryset): 
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark as read"
    
    actions = ['mark_as_read']