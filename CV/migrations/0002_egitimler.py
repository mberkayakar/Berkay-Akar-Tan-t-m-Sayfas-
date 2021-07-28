# Generated by Django 3.2.5 on 2021-07-28 17:49

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Egitimler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('egitim_adi', models.CharField(max_length=200, verbose_name='Egitim Adı')),
                ('aciklama', ckeditor.fields.RichTextField()),
                ('firmaicon', models.FileField(blank=True, null=True, upload_to='', verbose_name='eklemek isterseniz fotograf seçin ')),
            ],
        ),
    ]
