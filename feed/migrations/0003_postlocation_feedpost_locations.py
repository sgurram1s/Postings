# Generated by Django 4.2 on 2024-01-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_rename_post_feedpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_location', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='feedpost',
            name='locations',
            field=models.ManyToManyField(to='feed.postlocation'),
        ),
    ]