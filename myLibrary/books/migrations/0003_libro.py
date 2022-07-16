# Generated by Django 3.2.13 on 2022-07-15 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('nombre', models.CharField(help_text='Nombre del libro', max_length=150, verbose_name='Nombre')),
                ('anio_publicacion', models.IntegerField(blank=True, help_text='Año en que se publico el libro', null=True, verbose_name='Año Publicación')),
                ('hojas', models.IntegerField(blank=True, help_text='Cantidad de hojas del libro', null=True, verbose_name='Cantidad de Hojas')),
                ('img_cover', models.CharField(help_text='Imagen de Portada del Libro', max_length=150, verbose_name='Imagen')),
                ('autor', models.ForeignKey(help_text='Autor del libro', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='autor_libro', to='books.autor')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='libro_creation', to=settings.AUTH_USER_MODEL)),
                ('genero', models.ManyToManyField(help_text='Genero Literario asociado al libro', related_name='genero_libro', to='books.Autor')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='libro_update', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
