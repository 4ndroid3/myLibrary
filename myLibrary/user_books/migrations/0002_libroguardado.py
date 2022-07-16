# Generated by Django 3.2.13 on 2022-07-16 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_libro_genero'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibroGuardado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('fecha_leido', models.DateField(blank=True, help_text='Fecha en la que se leyo el libro', null=True)),
                ('leido', models.BooleanField(default=False, help_text='Decreta si el libro se leyo o solo se almaceno.')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='libro_leido_creation', to=settings.AUTH_USER_MODEL)),
                ('estante', models.ForeignKey(blank=True, help_text='Estante donde está guardado el libro', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='estante_libro_leido', to='user_books.estante')),
                ('libro', models.ForeignKey(help_text='Libro guardado por un usuario', on_delete=django.db.models.deletion.DO_NOTHING, related_name='libro_libro_leido', to='books.libro')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='libro_leido_update', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
