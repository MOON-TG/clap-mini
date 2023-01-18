# Generated by Django 4.1.5 on 2023-01-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_exam_delete_info_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battery', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]