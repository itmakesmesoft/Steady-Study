                                            # 404 에러를 뜨게 함
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from .models import Articles
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Articles.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)



@require_http_methods(['GET', 'POST'])
def create(request):
    # 사용자의 입력 후 요청이 왔을 때
    if request.method == "POST":
        form = ArticleForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
        return redirect('articles:create')
    # 사용자가 처음으로 생성 페이지에 접근했을 때
    else:
        # form을 만들고
        form = ArticleForm()
    context = {
        'form' : form,
    }
    # return render
    return render(request, 'articles/create.html', context)

# @require_POST: Post만 가능하도록 만듦 / delete는 페이지가 필요 없기 때문 
@require_POST
def delete(request, pk):
    article = Articles.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')



def update(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    if request.method == "POST" :
        form = ArticleForm(request.POST, instance=article) #기존에 있는 내용 포함
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article' : article,
    }
    return render(request, 'articles/update.html', context)

