# Generated by Django 4.2.1 on 2023-05-11 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_alter_payrecord_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payrecord',
            name='userId',
            field=models.ForeignKey(db_column='userId', null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.user'),
        ),
    ]
