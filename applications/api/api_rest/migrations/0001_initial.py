# Generated by Django 5.0.6 on 2024-09-12 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=150)),
                ('username', models.CharField(default='', max_length=100, unique=True)),
                ('email', models.EmailField(default='', max_length=254)),
                ('dateofbirth', models.DateField(default='2024-08-09')),
                ('gender', models.CharField(choices=[('Man', 'Man'), ('Woman', 'Woman'), ('Other', 'Other')], default='Male', max_length=10)),
                ('location', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('user_task', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
