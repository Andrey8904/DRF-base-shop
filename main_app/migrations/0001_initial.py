# Generated by Django 5.0.3 on 2024-03-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=250)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]