# Generated by Django 4.1.2 on 2022-11-07 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_application_cpu_alter_application_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='sync_loss',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
