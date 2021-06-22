# Generated by Django 3.2.4 on 2021-06-17 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_name', models.CharField(max_length=50)),
                ('open_hours', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('clinic', models.CharField(max_length=50)),
                ('pharmacy', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy_name', models.CharField(max_length=50)),
                ('open_hours', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_full_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
                ('clinic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aidApp.clinics')),
                ('doctor_last_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aidApp.doctors')),
                ('pharmacy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aidApp.pharmacies')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback_Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_or_complaint', models.CharField(max_length=10)),
                ('patient_message', models.CharField(max_length=200)),
                ('admin_reply', models.CharField(max_length=200)),
                ('patient_full_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aidApp.patients')),
            ],
        ),
        migrations.CreateModel(
            name='Consultations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
                ('clinic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aidApp.clinics')),
                ('doctor_last_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aidApp.doctors')),
                ('patient_full_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aidApp.patients')),
                ('pharmacy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aidApp.pharmacies')),
            ],
        ),
    ]