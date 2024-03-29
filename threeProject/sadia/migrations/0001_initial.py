# Generated by Django 2.2.3 on 2019-07-17 01:34

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='nnn', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='nnn', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='nnn', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telephone', models.CharField(max_length=11)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SaveNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='nnn', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField(default=0)),
                ('addTime', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('size', models.CharField(max_length=10)),
                ('img1', models.ImageField(upload_to='goods')),
                ('img2', models.ImageField(upload_to='goods')),
                ('img3', models.ImageField(upload_to='goods')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadia.Brand')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadia.Categorie')),
                ('classify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadia.Classify')),
                ('saveNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadia.SaveNum')),
                ('tag', models.ManyToManyField(to='sadia.Tag')),
            ],
        ),
    ]
