from django.contrib import admin
from .models import Article,Comment,VideoArticle
# Register your models here.

admin.site.register(Comment)
admin.site.register(VideoArticle)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["title"]
    search_fields = ["title"]
    list_filter = ["created_date"]    
    class Meta:
        model = Article

