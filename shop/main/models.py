from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from unidecode import unidecode

# class PubMenage(models.Model):
#     def get_queryset(self):
#         return super().get_queryset().filter(public=1)


class SpaceObj(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Адресация')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    public = models.BooleanField(default=True, verbose_name='Публикация')
    file = models.FileField(upload_to='uploads/', verbose_name='Файл', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    tags = models.ManyToManyField('TagsSpace', blank=True, related_name='tags', verbose_name='Тэг')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Космический объект'
        verbose_name_plural = 'Космическиe объекы'
        ordering = ['title']
        indexes = [
            models.Index(fields=['title'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'p_slug': self.slug})

    def save(self, *args, **kwargs):
        translate = unidecode(self.title)
        self.slug = slugify(translate)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class TagsSpace(models.Model):
    names = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.names

    def get_absolute_url(self):
        return reverse('tags', kwargs={'tags_slug': self.slug})
