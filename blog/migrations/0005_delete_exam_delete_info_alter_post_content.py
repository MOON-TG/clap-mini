# Generated by Django 4.1.5 on 2023-01-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_exam'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.DeleteModel(
            name='Info',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=30),
        ),
    ]