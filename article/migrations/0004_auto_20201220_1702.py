# Generated by Django 3.1.1 on 2020-12-20 14:02

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Makaleye Görüntü Ekleyin'),
        ),
        migrations.CreateModel(
            name='VideoArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoarticletitle', models.CharField(max_length=50, verbose_name='Başlık')),
                ('videoarticlecontent', ckeditor.fields.RichTextField()),
                ('videoarticlecreated_date', models.DateField(auto_now=True, verbose_name='Oluşturulma Tarihi')),
                ('article_video', models.URLField(blank=True, null=True, verbose_name='Makaleye Video Ekleyin')),
                ('videoarticleauthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
        ),
    ]