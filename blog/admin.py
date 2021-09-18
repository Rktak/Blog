from django.contrib import admin

# Register your models here.
from .models import Post,Author,Tag

class PostAdmin(admin.ModelAdmin):
    list_filter=("author","tag","date")
    list_display=("title","date","author")
    prepopulated_fields={"slug":("title",)}     # it is use to automatically store the 
                                                # slug by title 

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)