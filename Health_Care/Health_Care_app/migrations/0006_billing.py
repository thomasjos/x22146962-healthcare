# Generated by Django 2.0.2 on 2023-04-16 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Health_Care_app', '0005_medicalrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Health_Care_app.Patient')),
            ],
        ),
    ]
