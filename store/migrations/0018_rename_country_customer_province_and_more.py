# Generated by Django 5.0.3 on 2024-06-02 13:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0017_alter_order_total_price_alter_orderitem_price_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer", old_name="country", new_name="province",
        ),
        migrations.RenameField(
            model_name="shipping", old_name="state", new_name="province",
        ),
        migrations.RemoveField(model_name="customer", name="password",),
        migrations.RemoveField(model_name="customer", name="postal_code",),
        migrations.AlterField(
            model_name="customer",
            name="username",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
