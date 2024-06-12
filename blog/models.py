from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.urls import reverse

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Pavadinimas')
    description = HTMLField(max_length=2000, blank=True, verbose_name='Aprašymas')

    class Meta:
        verbose_name = 'Tėvinė kategorija'
        verbose_name_plural = 'Tėvinės kategorijos'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:articles_by_category', kwargs={'id': self.id})

class SubCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Pavadinimas')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='subcategories', verbose_name='Tėvinė kategorija')
    description = HTMLField(max_length=2000, blank=True, verbose_name='Aprašymas')
    image = models.ImageField(upload_to='images/article/%Y/%m/%d/', blank=True, verbose_name='Nuotrauka')

    class Meta:
        verbose_name = 'Vaikinė kategorija'
        verbose_name_plural = 'Vaikinės kategorijos'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:articles_by_subcategory', kwargs={'id': self.id})

class Article(models.Model):
    STATUS_OPTIONS = (
        ('published', 'Paskelbta'),
        ('hidden', 'Paslėpta'),
    )

    subcategory = models.ForeignKey(to=SubCategory, on_delete=models.CASCADE, related_name='articles', verbose_name='Subkategorija')
    title = models.CharField(max_length=255, verbose_name='Pavadinimas')
    short_description = models.TextField(max_length=2000, blank=True, verbose_name='Trumpas aprašymas')
    full_description = HTMLField(blank=True, verbose_name='Pilnas aprašymas')
    image = models.ImageField(upload_to='images/article/%Y/%m/%d/', blank=True, verbose_name='Nuotrauka')

    status = models.CharField(choices=STATUS_OPTIONS, default='published', max_length=10, verbose_name='Statusas')
    author = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, related_name='author_posts', default=1, verbose_name='Autorius')
    updater = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='updater_posts', blank=True, verbose_name='Atnaujino')

    class Meta:
        indexes = [models.Index(fields=['status'])]
        verbose_name = 'Straipsnis'
        verbose_name_plural = 'Straipsniai'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:articles_detail', kwargs={'pk': self.pk})
