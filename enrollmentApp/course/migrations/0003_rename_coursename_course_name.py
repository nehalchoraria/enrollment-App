# Generated by Django 4.0.5 on 2022-06-02 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_universityid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='courseName',
            new_name='name',
        ),
    ]
