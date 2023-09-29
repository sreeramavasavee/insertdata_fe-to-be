# Generated by Django 4.2.3 on 2023-09-29 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='school',
            fields=[
                ('schlname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('principal', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('sname', models.CharField(max_length=50)),
                ('semail', models.EmailField(max_length=254)),
                ('schlname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school')),
            ],
        ),
    ]