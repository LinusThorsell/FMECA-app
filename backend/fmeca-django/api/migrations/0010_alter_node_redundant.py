# Generated by Django 4.1.1 on 2022-11-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_application_cpu_alter_application_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='redundant',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]