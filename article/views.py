from django.shortcuts import render, HttpResponse, redirect, get_object_or_404,reverse
from .forms import ArticleForm,VideoArticleForm
from django.contrib import messages
from .models import Article,Comment,VideoArticle
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.template import RequestContext

def page_not_found(request, exception, template_name="404.html"):
    response = render(request,template_name)
    response.status_code = 404
    return response
def articles(request):
    keyword = request.GET.get("keyword")  # <--------search function
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})

    articles = Article.objects.all()

    return render(request, "articles.html", {"articles": articles})

def videoarticles(request):
    videoarticles = VideoArticle.objects.all()
    return render(request, "videoarticles.html", {"videoarticles": videoarticles})
def nofilearticles(request):
    articles = Article.objects.all()
    return render(request,"nofilenews.html",{"articles":articles})

def index(request):
    articles = Article.objects.all()
    videoarticle = VideoArticle.objects.all()
    return render(request, "index.html", {"articles":articles,'videoarticles':videoarticle})


def detail(request, id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id=id)

    #comments = Comment.objects.all()
    comments = article.comments.all()
    return render(request, "detail.html", {"article": article,"comments":comments})


@login_required(login_url="user:login")
def dashboard(request):
    # authorized user is all articles
    articles = Article.objects.filter(author=request.user)
    context = {  # articles is dictionary type data
        "articles": articles
    }
    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale Başarıyla Oluşturuldu")
        return redirect("index")
    return render(request, "addarticle.html", {"form": form})
@login_required(login_url="user:login")
def addVideoArticle(request):
    form = VideoArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        videoarticle = form.save(commit=False)
        videoarticle.videoarticleauthor = request.user
        videoarticle.save()
        messages.success(request, "Makale Başarıyla Oluşturuldu")
        return redirect("index")
    return render(request, "addvideoarticle.html", {"form": form})


@login_required(login_url="user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None,
                       request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Güncelleme İşlemi Başarılı")
        return redirect("index")
    return render(request, "update.html", {"form": form})


@login_required(login_url="user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "Makale Başarıyla Silindi")
    return redirect("article:dashboard")


def addComment(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        new_Comment = Comment(comment_author=comment_author,comment_content=comment_content)
        new_Comment.article = article
        new_Comment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))#kwargs add comment id

