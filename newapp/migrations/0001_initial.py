# Generated by Django 3.2.5 on 2022-04-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.FileField(upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
    ]
