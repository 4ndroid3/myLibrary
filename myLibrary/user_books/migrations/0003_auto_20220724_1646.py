# Generated by Django 3.2.13 on 2022-07-24 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_libro_autor'),
        ('user_books', '0002_libroguardado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libroguardado',
            name='estante',
            field=models.ForeignKey(blank=True, help_text='Estante donde está guardado el libro', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='estante_libro_leido', to='user_books.estante'),
        ),
        migrations.AlterField(
            model_name='libroguardado',
            name='libro',
            field=models.ForeignKey(help_text='Libro guardado por un usuario', on_delete=django.db.models.deletion.CASCADE, related_name='libro_libro_leido', to='books.libro'),
        ),
    ]
