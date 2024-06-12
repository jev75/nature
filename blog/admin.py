from django.contrib import admin
from django.utils.html import format_html
from .models import Category, SubCategory, Article

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)

    fieldsets = (
        ('Pagrindinė informacija', {'fields': ('name', 'description')}),
    )


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',  'thumbnail_display')
    list_filter = ('category',)
    search_fields = ('name',  'category__name')

    fieldsets = (
        ('Pagrindinė informacija', {'fields': ('name', 'category', 'description', 'image')}),
    )

    def thumbnail_display(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="width: 50px; height: auto;" />')
        return "Paveikslėlio nėra"

    thumbnail_display.short_description = 'Peržiūra'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'subcategory', 'status', 'thumbnail_display')
    list_filter = ('status', 'subcategory', 'author')
    search_fields = ('title', 'short_description', 'author__username', 'subcategory__name')

    fieldsets = (
        ('Pagrindinė informacija', {'fields': ('title', 'author', 'subcategory', 'status')}),
        ('Turinys', {'fields': ('short_description', 'full_description', 'image')}),
    )

    def thumbnail_display(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="width: 50px; height: auto;" />')
        return "Paveikslėlio nėra"

    thumbnail_display.short_description = 'Peržiūra'

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        obj.save()

admin.site.site_header = 'Tinklapio valdymas'
