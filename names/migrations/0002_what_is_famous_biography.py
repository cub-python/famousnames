# Generated by Django 4.1.2 on 2022-10-24 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('names', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='What_is_famous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=64)),
                ('names', models.ManyToManyField(to='names.name')),
            ],
        ),
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('names', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='names.name')),
            ],
        ),
    ]