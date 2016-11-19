from django.contrib import admin

# Register your models here.
from .models import Blog,Comment,News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'language')
    
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(News,NewsAdmin)