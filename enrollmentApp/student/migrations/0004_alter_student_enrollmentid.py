# Generated by Django 4.0.5 on 2022-06-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_enrollmentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrollmentId',
            field=models.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
    ]
