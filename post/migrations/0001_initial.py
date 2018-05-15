# Generated by Django 2.0.4 on 2018-05-15 02:13

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
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('distance', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True)),
                ('gender', models.CharField(blank=True, max_length=1)),
                ('occupation', models.CharField(blank=True, max_length=20)),
                ('know_m_1', models.CharField(blank=True, max_length=100)),
                ('know_m_2', models.CharField(blank=True, max_length=100)),
                ('know_m_3', models.CharField(blank=True, max_length=100)),
                ('know_m_4', models.CharField(blank=True, max_length=100)),
                ('know_m_5', models.CharField(blank=True, max_length=100)),
                ('know_m_6', models.CharField(blank=True, max_length=100)),
                ('know_m_7', models.CharField(blank=True, max_length=100)),
                ('know_m_8', models.CharField(blank=True, max_length=100)),
                ('know_m_9', models.CharField(blank=True, max_length=100)),
                ('know_m_10', models.CharField(blank=True, max_length=100)),
                ('rec_m_1', models.CharField(blank=True, max_length=100)),
                ('rec_m_2', models.CharField(blank=True, max_length=100)),
                ('rec_m_3', models.CharField(blank=True, max_length=100)),
                ('rec_m_4', models.CharField(blank=True, max_length=100)),
                ('rec_m_5', models.CharField(blank=True, max_length=100)),
                ('rec_m_6', models.CharField(blank=True, max_length=100)),
                ('rec_m_7', models.CharField(blank=True, max_length=100)),
                ('rec_m_8', models.CharField(blank=True, max_length=100)),
                ('rec_m_9', models.CharField(blank=True, max_length=100)),
                ('rec_m_10', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
