# Generated by Django 4.0.5 on 2022-06-02 03:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrollmentId',
            field=models.UUIDField(default=uuid.UUID('76672915-053b-4899-8e36-abaecc9d35ce'), editable=False, primary_key=True, serialize=False),
        ),
    ]
