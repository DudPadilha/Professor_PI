# Generated by Django 5.1.2 on 2024-11-01 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
