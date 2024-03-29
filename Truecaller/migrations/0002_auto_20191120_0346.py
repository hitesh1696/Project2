# Generated by Django 2.0 on 2019-11-19 22:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Truecaller', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='mobile_primary',
            new_name='mobile',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='district',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='mobile_secondary',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='state',
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterModelTable(
            name='contact',
            table=None,
        ),
    ]
