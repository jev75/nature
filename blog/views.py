from django.views.generic import ListView, DetailView
from .models import Article, Category, SubCategory
from django.shortcuts import get_object_or_404

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/articles_list.html'
    context_object_name = 'articles'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Pagrindinis puslapis'
        context['categories'] = Category.objects.all()
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/articles_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['related_articles'] = Article.objects.filter(subcategory=self.object.subcategory).exclude(id=self.object.id)[:5]
        context['categories'] = Category.objects.all()
        return context

class ArticleByCategoryListView(ListView):
    model = Article
    template_name = 'blog/articles_list.html'
    context_object_name = 'articles'
    paginate_by = 4

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['id'])
        return Article.objects.filter(subcategory__category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Straipsniai iš kategorijos: {self.category.name}'
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        return context

class ArticleBySubCategoryListView(ListView):
    model = Article
    template_name = 'blog/articles_list.html'
    context_object_name = 'articles'
    paginate_by = 4

    def get_queryset(self):
        self.subcategory = get_object_or_404(SubCategory, id=self.kwargs['id'])
        return Article.objects.filter(subcategory=self.subcategory)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Straipsniai iš subkategorijos: {self.subcategory.name}'
        context['subcategory'] = self.subcategory
        context['categories'] = Category.objects.all()
        return context
