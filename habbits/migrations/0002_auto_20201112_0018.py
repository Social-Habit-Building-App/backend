# Generated by Django 3.1.3 on 2020-11-12 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('habbits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habbit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile'),
        ),
    ]
