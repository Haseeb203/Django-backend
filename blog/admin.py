from django.contrib import admin
from .models import Post , Author , Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter=("date" , "tags" , "author" ,)
    list_display=("title", "date" ,"author" ,)
    prepopulated_fields={"slug" : ("title" ,) }
    






admin.site.register(Post , PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)