# Generated by Django 4.2.7 on 2024-06-26 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_api', '0005_alter_transition_t_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transition',
            new_name='Transaction',
        ),
    ]
