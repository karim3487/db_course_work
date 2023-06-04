# Generated by Django 3.2.19 on 2023-06-04 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bill',
            options={'ordering': ('date_sent',), 'verbose_name': 'Счет за прием', 'verbose_name_plural': 'Счета за приемы'},
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='bill',
            name='appointment',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bill', to='app.appointment'),
        ),
        migrations.AddField(
            model_name='payment',
            name='insurance_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='app.insurancecompany'),
        ),
        migrations.AddField(
            model_name='payment',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='app.patient'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='app.bill'),
        ),
    ]
