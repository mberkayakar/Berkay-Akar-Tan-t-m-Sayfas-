# Generated by Django 3.2.5 on 2021-07-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0002_egitimler'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilFotografı',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProfilFotografı', models.FileField(blank=True, null=True, upload_to='', verbose_name='eklemek isterseniz fotograf seçin ')),
            ],
        ),
    ]
