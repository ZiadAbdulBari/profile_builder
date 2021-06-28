# Generated by Django 3.2.3 on 2021-06-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('dob', models.DateField()),
                ('contact_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=100)),
            ],
        ),
    ]