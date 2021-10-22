from django.contrib import admin
from .models import Category, Process

# Register your models here.

class ListProcess(admin.ModelAdmin):
    list_display = ('cod', 'title', 'created_date', 'category')
    list_display_links = ('cod', 'title')
    search_fields = ('title',)
    list_filter = ('category',)
    list_per_page = 5

admin.site.register(Category)
admin.site.register(Process, ListProcess)
