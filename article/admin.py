from django.contrib import admin
from article.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','category','date_time','content']

admin.site.register(Article,ArticleAdmin)