# Generated by Django 3.2.7 on 2021-09-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('long_url', models.URLField()),
                ('short_url', models.CharField(max_length=15, unique=True)),
                ('times_followed', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
