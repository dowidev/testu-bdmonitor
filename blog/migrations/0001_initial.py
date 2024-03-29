# Generated by Django 2.2.6 on 2019-10-16 02:19

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
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.CharField(max_length=15)),
                ('dir_ap', models.CharField(choices=[('CON', 'Controller'), ('DEV', 'Development'), ('FIN', 'Finance & Treasury'), ('HR', 'HR-GA'), ('ICT', 'ICT & DM'), ('AUDIT', 'Internal Audit'), ('LEGAL', 'Legal'), ('NUN', 'Nunukan'), ('ONWJ', 'ONWJ'), ('OPS', 'Operation & Production'), ('PHI', 'PHI'), ('PPRM', 'PPRM'), ('QHSSE', 'QHSSE'), ('REL', 'Relation'), ('SCM', 'SCM'), ('SK', 'Siak-Kampar'), ('CO', 'Commercial'), ('WMO', 'WMO')], max_length=5)),
                ('requirement', models.TextField()),
                ('requirement_type', models.CharField(choices=[('N', 'New Requirement'), ('E', 'Enhancement'), ('R', 'Roll Out'), ('T', 'Training')], max_length=1)),
                ('prioritas', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1)),
                ('target', models.CharField(choices=[('1', 'TW-I'), ('2', 'TW-II'), ('3', 'TW-III'), ('4', 'TW-IV')], max_length=1)),
                ('budget', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateField()),
                ('progress', models.IntegerField()),
                ('status', models.CharField(choices=[('C', 'Closed'), ('D', 'Dropped'), ('E', 'Execution'), ('I', 'Initiation'), ('P', 'Planning')], max_length=1)),
                ('status_akhir', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
    ]
