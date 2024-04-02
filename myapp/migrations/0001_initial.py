# Generated by Django 5.0.3 on 2024-04-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('progress', models.CharField(max_length=100)),
                ('score', models.CharField(max_length=2)),
            ],
        ),
    ]
