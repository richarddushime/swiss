# Generated by Django 3.2.11 on 2022-02-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0002_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Desc', models.TextField(max_length=100)),
            ],
            options={
                'ordering': ('Name', 'Desc'),
            },
        ),
    ]
