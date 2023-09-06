from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    about = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Превью', **NULLABLE)
    category = models.CharField(max_length=150, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_made = models.DateTimeField(verbose_name='Дата создания')
    date_change = models.DateTimeField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    about = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.name} {self.about}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

