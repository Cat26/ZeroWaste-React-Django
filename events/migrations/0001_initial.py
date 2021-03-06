# Generated by Django 2.2.7 on 2019-11-22 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=220)),
                ('scores', models.FloatField()),
                ('participants', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('photo', models.ImageField(null=True, upload_to='images/')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
