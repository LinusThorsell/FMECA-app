# Generated by Django 4.1.1 on 2022-12-06 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_pacport_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='provider_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider_set', to='api.applicationinstance'),
        ),
        migrations.AddField(
            model_name='connection',
            name='provider_thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider_set', to='api.thread'),
        ),
        migrations.AddField(
            model_name='connection',
            name='requirer_app',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requirer_set', to='api.applicationinstance'),
        ),
        migrations.AddField(
            model_name='connection',
            name='requirer_thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requirer_set', to='api.thread'),
        ),
    ]