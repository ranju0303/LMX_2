# Generated by Django 3.1.4 on 2021-01-02 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0008_auto_20210102_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assign_to',
            field=models.ManyToManyField(blank=True, null=True, to='lms.Course'),
        ),
    ]
