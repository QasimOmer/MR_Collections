# Generated by Django 5.0.6 on 2024-05-13 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_rename_sub_category_subcategory_category"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="slug",),
    ]