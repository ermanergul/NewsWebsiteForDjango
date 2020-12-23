from django import forms
from .models import Article,VideoArticle

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_file"]
class VideoArticleForm(forms.ModelForm):
    class Meta:
        model = VideoArticle
        fields= ['videoarticletitle','videoarticlecontent','article_video']