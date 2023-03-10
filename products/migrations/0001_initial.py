# Generated by Django 3.2 on 2023-02-25 18:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='name')),
                ('caption', models.TextField(blank=True, verbose_name='caption')),
                ('avatar', models.ImageField(upload_to='CategoryImage/', verbose_name='ImagePro')),
                ('published_time', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='parents')),
            ],
            options={
                'verbose_name': 'Category',
                'db_table': 'categories',
                'ordering': ['-published_time'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Name')),
                ('caption', models.TextField(blank=True, verbose_name='caption')),
                ('avatar', models.ImageField(upload_to='Products/', verbose_name='ProImage')),
                ('published_time', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, to='products.Category', verbose_name='categories')),
            ],
            options={
                'verbose_name': 'product',
                'db_table': 'products',
                'ordering': ['-published_time'],
            },
        ),
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='file/%Y/%M/&D/', verbose_name='file')),
                ('published_time', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'file',
                'db_table': 'files',
                'ordering': ['-published_time'],
            },
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-published_time'], name='products_publish_f82cf3_idx'),
        ),
        migrations.AddIndex(
            model_name='file',
            index=models.Index(fields=['-published_time'], name='files_publish_2e1a81_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['-published_time'], name='categories_publish_d13991_idx'),
        ),
    ]
