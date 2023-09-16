# Generated by Django 4.2.4 on 2023-09-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Превью')),
                ('about', models.TextField(verbose_name='содержимое')),
                ('created_at', models.DateTimeField(verbose_name='Дата создания')),
                ('published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('slug', models.CharField(max_length=30, verbose_name='slug')),
                ('views_count', models.IntegerField(default=0, verbose_name='счетчик просмотров')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
