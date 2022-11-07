# Generated by Django 4.1.2 on 2022-11-07 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_node_redundant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='cpu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.cpu'),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connection_provider_set', to='api.application'),
        ),
        migrations.AlterField(
            model_name='connection',
            name='requirer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connection_requirer_set', to='api.application'),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='accs_sync_master',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='domain_border',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='iop_ref',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.node'),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='unit_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='load_set_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='platform',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='sync_loss',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='partition',
            name='cpu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.cpu'),
        ),
        migrations.AlterField(
            model_name='partition',
            name='fixed_start',
            field=models.BigIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='partition',
            name='is_ltm',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='partition',
            name='partition_id',
            field=models.IntegerField(default=None, null=True),
        ),
    ]