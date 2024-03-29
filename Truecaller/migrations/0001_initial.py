# Generated by Django 2.0 on 2019-11-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile_primary', models.IntegerField()),
                ('mobile_secondary', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
    ]
