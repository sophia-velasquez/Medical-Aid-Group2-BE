# Generated by Django 3.2.4 on 2021-06-24 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0002_auto_20210619_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400)),
                ('answer', models.CharField(max_length=400)),
            ],
        ),
    ]
