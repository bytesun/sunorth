from django.contrib import admin

from .models import Book,BTag

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'language')

class BTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'language')    
admin.site.register(Book,BookAdmin)
admin.site.register(BTag,BTagAdmin)
