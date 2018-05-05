from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle
from django.http import Http404, HttpResponse  # to raise 404 page not found


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles\\article_list.html', {'articles': articles})


def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', {'article': article})


def user_articles(request, author):
    user = User.objects.get(username=author)
    user_data = Article.objects.filter(author=user.pk)
    if user_data:
        user = user_data[0].author.username
        return render(request, 'articles/user_articles.html', {'articles': user_data, 'user': user})
    else:
        raise Http404('PAge Not found')
    # return HttpResponse('hello world {}'.format(author))


@login_required(login_url='/accounts/login')
def article_create(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
