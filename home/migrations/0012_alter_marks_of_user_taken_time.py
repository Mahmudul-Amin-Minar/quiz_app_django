# Generated by Django 3.2.5 on 2021-10-31 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_marks_of_user_taken_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks_of_user',
            name='taken_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
