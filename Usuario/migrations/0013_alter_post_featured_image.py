# Generated by Django 5.1.5 on 2025-01-20 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0012_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
