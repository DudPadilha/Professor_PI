# Generated by Django 5.1.2 on 2024-11-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_noticia_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='link',
            field=models.URLField(null=True),
        ),
    ]