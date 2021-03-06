# Generated by Django 4.0.5 on 2022-06-02 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0002_remove_syllabus_courseid'),
        ('course', '0003_rename_coursename_course_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSyllabusMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('syllabusId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.syllabus')),
            ],
        ),
    ]
