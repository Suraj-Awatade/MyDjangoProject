# Generated by Django 4.1.2 on 2022-11-03 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_delete_bloguser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(default='Suraj Awatade', max_length=100),
            preserve_default=False,
        ),
    ]