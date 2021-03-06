# Generated by Django 3.1.4 on 2021-01-07 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210105_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='科研成果')),
                ('index', models.IntegerField(default=999, verbose_name='分类排序')),
            ],
            options={
                'verbose_name': '科研成果',
                'verbose_name_plural': '科研成果',
            },
        ),
        migrations.AlterField(
            model_name='banner',
            name='link_url',
            field=models.URLField(default=' ', max_length=100, verbose_name='图片链接'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='text_info',
            field=models.CharField(default=' ', max_length=50, verbose_name='标题'),
        ),
    ]
