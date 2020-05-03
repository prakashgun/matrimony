# Generated by Django 3.0.5 on 2020-05-03 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='employed_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employed_in_profile_set', to='matrimony.EmployedIn'),
        ),
    ]