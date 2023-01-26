# Generated by Django 4.1.4 on 2022-12-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_profession_options_profession_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images/', verbose_name='График')),
            ],
            options={
                'verbose_name': 'Статистика',
                'verbose_name_plural': 'Статистика',
            },
        ),
    ]