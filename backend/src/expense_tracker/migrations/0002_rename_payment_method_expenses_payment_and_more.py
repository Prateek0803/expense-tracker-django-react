# Generated by Django 4.1.2 on 2022-10-05 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenses',
            old_name='payment_method',
            new_name='payment',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]