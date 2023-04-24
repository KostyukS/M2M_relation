# Generated by Django 4.0.6 on 2023-04-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_scope'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='articles.Scope', to='articles.tag'),
        ),
    ]