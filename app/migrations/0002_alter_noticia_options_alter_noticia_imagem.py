# Generated by Django 5.1.1 on 2024-10-03 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticia',
            options={'verbose_name_plural': 'Notícias'},
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='noticias/'),
        ),
    ]
