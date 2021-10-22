from django.contrib import admin
from .models import Category, Process

# Register your models here.

class ListProcess(admin.ModelAdmin):
    list_display = ('cod', 'title', 'created_date', 'category')
    list_display_links = ('cod', 'title')
    search_fields = ('title',)
    list_filter = ('category',)
    list_per_page = 5

class ListCate(admin.ModelAdmin):
    list_display = ('cod', 'description')
    list_display_links = ('cod', 'description')

admin.site.register(Category, ListCate)
admin.site.register(Process, ListProcess)
