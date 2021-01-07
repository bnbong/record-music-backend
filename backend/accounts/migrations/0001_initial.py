# Generated by Django 3.0.5 on 2021-01-06 04:42

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email address')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Username')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('profile_image', models.ImageField(null=True, upload_to='')),
                ('followers', djongo.models.fields.ArrayReferenceField(on_delete=djongo.models.fields.ArrayReferenceField._on_delete, related_name='recordmusic_followers', to=settings.AUTH_USER_MODEL)),
                ('following', djongo.models.fields.ArrayReferenceField(on_delete=djongo.models.fields.ArrayReferenceField._on_delete, related_name='recordmusic_following', to=settings.AUTH_USER_MODEL)),
                ('friends', djongo.models.fields.ArrayReferenceField(on_delete=djongo.models.fields.ArrayReferenceField._on_delete, related_name='recordmusic_friends', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('username',),
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
    ]
