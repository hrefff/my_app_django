from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import ListView
from blog.models import Article, Image
from blog.forms import UploadFileForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def all_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def detail_article(request, id):
    article = get_object_or_404(Article, id=id)
    images = Image.objects.filter(article=article)
    return render(request, 'detail_article.html', {
        'article': article,
        'images': images
    })

# def add_article(request):
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save(commit=False)
#             return redirect('articles')
#     else:
#         form = UploadFileForm()

#     return render(request, 'add_article.html', {'form': form})


class AddArticleView(FormView):
    form_class = UploadFileForm
    template_name = "add_article.html"  # Replace with your template.
    success_url = reverse_lazy('all_articles')  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        title = form.cleaned_data["title"]
        new_article = Article.objects.create(title=title)
        files = form.cleaned_data["images"]
        for f in files:
            Image.objects.create(article=new_article, image=f)
        return super().form_valid(form)
