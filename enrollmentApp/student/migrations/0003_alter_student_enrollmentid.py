# Generated by Django 4.0.5 on 2022-06-02 03:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_enrollmentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrollmentId',
            field=models.UUIDField(default=uuid.UUID('a8568189-db05-464f-bb0e-d24a298db829'), editable=False, primary_key=True, serialize=False),
        ),
    ]