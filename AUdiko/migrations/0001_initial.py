# Generated by Django 4.1 on 2022-09-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=400)),
                ('pubDate', models.DateField()),
            ],
        ),
    ]
