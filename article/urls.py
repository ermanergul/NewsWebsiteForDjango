from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import handler404
app_name = "article"

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('addvideoarticle/',views.addVideoArticle,name="addvideoarticle"),
    path('article/<int:id>',views.detail,name = "detail"),
    path('update/<int:id>',views.updateArticle,name = "update"),
    path('delete/<int:id>',views.deleteArticle,name = "delete"),
    path('',views.articles,name = "articles"),
    path('videoarticles/',views.videoarticles,name="videoarticles"),
    path('nofilenews/',views.nofilearticles,name="nofilearticles"),
    path('comment/<int:id>',views.addComment,name = "comment"),
]
handler404 = views.page_not_found