# Generated by Django 3.2.13 on 2022-07-16 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_libro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.ManyToManyField(help_text='Genero Literario asociado al libro', related_name='genero_libro', to='books.Genero'),
        ),
    ]