# Generated by Django 3.0.5 on 2020-05-03 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matrimony', '0002_bodytype_caste_city_complexion_country_createdby_currencytype_dosham_drinkinghabit_eatinghabit_educa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('about', models.TextField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('education_institution', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation_in_detail', models.CharField(blank=True, max_length=255, null=True)),
                ('organization', models.CharField(blank=True, max_length=255, null=True)),
                ('annual_income', models.IntegerField(blank=True, null=True)),
                ('no_of_brothers', models.IntegerField(blank=True, null=True)),
                ('brothers_married', models.IntegerField(blank=True, null=True)),
                ('no_of_sisters', models.IntegerField(blank=True, null=True)),
                ('sisters_married', models.IntegerField(blank=True, null=True)),
                ('ancestral_origin', models.CharField(blank=True, max_length=255, null=True)),
                ('about_family', models.TextField(blank=True, null=True)),
                ('citizenship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citizenship_profile_set', to='matrimony.Country')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_profile_set', to='matrimony.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_profile_set', to='matrimony.Country')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by_profile_set', to='matrimony.CreatedBy')),
                ('currency_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='currency_type_profile_set', to='matrimony.MaritalStatus')),
                ('drinking_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drinking_habit_profile_set', to='matrimony.DrinkingHabit')),
                ('eating_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eating_habit_profile_set', to='matrimony.EatingHabit')),
                ('education', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education_profile_set', to='matrimony.Education')),
                ('employed_in', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employed_in_profile_set', to='matrimony.MaritalStatus')),
                ('family_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family_status_profile_set', to='matrimony.FamilyStatus')),
                ('family_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family_type_profile_set', to='matrimony.FamilyType')),
                ('family_value', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family_value_profile_set', to='matrimony.FamilyValue')),
                ('father_occupation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='father_occupation_profile_set', to='matrimony.Occupation')),
                ('marital_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marital_status_profile_set', to='matrimony.MaritalStatus')),
                ('mother_occupation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mother_occupation_profile_set', to='matrimony.Occupation')),
                ('mother_tongue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mother_tongue_profile_set', to='matrimony.Language')),
                ('occupation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='occupation_profile_set', to='matrimony.Occupation')),
                ('physical_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='physical_status_profile_set', to='matrimony.PhysicalStatus')),
                ('smoking_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='smoking_habit_profile_set', to='matrimony.SmokingHabit')),
                ('spoken_languages', models.ManyToManyField(blank=True, null=True, related_name='spoken_languages_profile_set', to='matrimony.Language')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_profile_set', to='matrimony.State')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
