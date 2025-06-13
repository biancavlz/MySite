from django.contrib import admin
from .models import Post, Tag, Author

class PostAdmin(admin.ModelAdmin):
  list_filter = ("author", "tags", "date",)
  list_display = ("title", "date", "author",)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)

# Register your models here.
