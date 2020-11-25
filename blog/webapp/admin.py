from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', "author", "created_at", "updated_at")  # columns
    list_filter = ('status', "created_at", "updated_at", "author")  # sidebar to filter by those fields
    search_fields = ('title', 'body')  # Enable search bar for those fields
    date_hierarchy = 'publish'   #  put the date at the top of the table
    ordering = ('status', "publish")   # allows to ordering by fields with the arrow in the column name
    prepopulated_fields = {'slug': ("author", "title")}    #  autocomplete field with other fields
    raw_id_fields = ('author',)  # open a new window to see the user and search them
