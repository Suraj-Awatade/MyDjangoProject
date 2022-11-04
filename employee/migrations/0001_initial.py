# Generated by Django 4.1.2 on 2022-10-21 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('contact_no', models.BigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('zip_code', models.IntegerField()),
                ('landmark', models.CharField(max_length=200)),
                ('street_area', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.details')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
