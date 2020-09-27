# Generated by Django 3.1.1 on 2020-09-26 07:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('group', models.UUIDField(db_column='Group', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=20)),
                ('description', models.CharField(db_column='Description', max_length=20)),
            ],
            options={
                'db_table': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('person', models.UUIDField(db_column='Person', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(db_column='FirstName', max_length=20)),
                ('last_name', models.CharField(db_column='LastName', max_length=20)),
            ],
            options={
                'db_table': 'Persons',
            },
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('subscription', models.UUIDField(db_column='Subscription', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('admin', models.BooleanField(db_column='Admin')),
                ('group', models.ForeignKey(db_column='Group', on_delete=django.db.models.deletion.CASCADE, to='subs.groups')),
                ('person', models.ForeignKey(db_column='Person', on_delete=django.db.models.deletion.CASCADE, to='subs.persons')),
            ],
            options={
                'db_table': 'Subscriptions',
            },
        ),
    ]