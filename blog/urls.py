from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('articles/', views.ArticleListView.as_view(), name='articles_list'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='articles_detail'),
    path('category/<int:id>/', views.ArticleByCategoryListView.as_view(), name='articles_by_category'),
    path('subcategory/<int:id>/', views.ArticleBySubCategoryListView.as_view(), name='articles_by_subcategory'),
]
