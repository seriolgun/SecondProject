# Generated by Django 4.2.1 on 2023-05-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ogrenci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
                ('acıklama', models.TextField(max_length=1000)),
                ('no', models.IntegerField()),
            ],
        ),
    ]
