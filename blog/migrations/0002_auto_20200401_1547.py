# Generated by Django 2.2.12 on 2020-04-01 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blog_user',
            field=models.CharField(max_length=20),
        ),
    ]