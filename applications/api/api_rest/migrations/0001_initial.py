# Generated by Django 5.0.6 on 2024-05-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_nickname', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('user_name', models.CharField(default='', max_length=150)),
                ('user_email', models.EmailField(default='', max_length=254)),
                ('user_age', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nickname', models.CharField(default='', max_length=100)),
                ('user_task', models.CharField(default='', max_length=255)),
            ],
        ),
    ]