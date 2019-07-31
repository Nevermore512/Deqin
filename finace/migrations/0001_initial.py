# Generated by Django 2.2.3 on 2019-07-29 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('balance_sheet', models.FileField(upload_to='balance')),
                ('income', models.FileField(upload_to='income')),
                ('cash_flow', models.FileField(upload_to='carsh')),
            ],
        ),
    ]