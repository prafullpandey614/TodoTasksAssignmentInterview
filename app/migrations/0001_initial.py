# Generated by Django 4.2.5 on 2023-09-28 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodoItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('list_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.listitem')),
            ],
        ),
    ]