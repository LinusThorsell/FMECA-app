# Generated by Django 4.1.1 on 2022-12-01 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_application_automated_test_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationinstance',
            name='node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.node'),
        ),
    ]
