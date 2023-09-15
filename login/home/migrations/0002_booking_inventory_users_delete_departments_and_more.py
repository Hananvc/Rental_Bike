# Generated by Django 4.1.5 on 2023-02-11 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Booked_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bikes_name', models.CharField(max_length=255)),
                ('bikes_spec', models.CharField(max_length=255)),
                ('bikes_image', models.ImageField(upload_to='bikes')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='departments',
        ),
        migrations.AddField(
            model_name='booking',
            name='Model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.inventory'),
        ),
    ]