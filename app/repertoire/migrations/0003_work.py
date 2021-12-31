# Generated by Django 3.2.10 on 2021-12-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repertoire', '0002_auto_20211222_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('contributers', models.CharField(max_length=200)),
                ('iswc', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('proprietary_id', models.IntegerField()),
            ],
        ),
    ]