from django.db import models
from django.urls import reverse


class Cars(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=120, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to="images", verbose_name='Фото')
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    update = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('cars_info', kwargs={'info_slug': self.slug})


    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ['-published']



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=120, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cars_category', kwargs={'cars_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-name']
