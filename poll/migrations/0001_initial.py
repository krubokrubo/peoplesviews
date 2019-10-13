# Generated by Django 2.2.6 on 2019-10-12 17:25

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
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datestamp', models.DateTimeField(auto_now=True)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll')),
                ('voter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VoteLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Candidate')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Vote')),
            ],
        ),
        migrations.CreateModel(
            name='PollResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datestamp', models.DateTimeField(auto_now=True)),
                ('result', models.TextField()),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll'),
        ),
    ]