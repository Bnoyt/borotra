# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 14:12
from __future__ import unicode_literals

import datetime
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
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournoi', models.CharField(choices=[('0', 'simple'), ('1', 'équipes')], default='1', max_length=1)),
                ('date_inscription', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_prevue', models.DateField(default=datetime.date.today)),
                ('date_match', models.CharField(max_length=20)),
                ('typematch', models.CharField(choices=[('0', 'debutants'), ('1', 'nextgen'), ('2', 'classique')], default='1', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('joueur2_prenom', models.CharField(max_length=100)),
                ('joueur2_nom', models.CharField(max_length=100)),
                ('joueur2_classement', models.CharField(max_length=100)),
                ('joueur3_prenom', models.CharField(max_length=100)),
                ('joueur3_nom', models.CharField(max_length=100)),
                ('joueur3_classement', models.CharField(max_length=100)),
                ('joueur4_prenom', models.CharField(max_length=100)),
                ('joueur4_nom', models.CharField(max_length=100)),
                ('joueur_classement', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_prevue', models.DateField(default=datetime.date.today)),
                ('date_match', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TennisScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typematch', models.CharField(choices=[('0', 'debutants'), ('1', 'nextgen'), ('2', 'classique')], default='1', max_length=1)),
                ('s1j1', models.IntegerField(default=0)),
                ('s1j2', models.IntegerField(default=0)),
                ('s2j1', models.IntegerField(default=0)),
                ('s2j2', models.IntegerField(default=0)),
                ('s3j1', models.IntegerField(default=0)),
                ('s3j2', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profil', models.CharField(choices=[('0', 'admin'), ('1', 'joueur')], default='1', max_length=1)),
                ('promo', models.IntegerField(default=2016)),
                ('ecole', models.CharField(default='Polytechnique', max_length=35)),
                ('classement', models.CharField(default='NC', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='teammatch',
            name='score_double',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_double', to='app.TennisScore'),
        ),
        migrations.AddField(
            model_name='teammatch',
            name='score_simple1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_simple1', to='app.TennisScore'),
        ),
        migrations.AddField(
            model_name='teammatch',
            name='score_simple2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_simple2', to='app.TennisScore'),
        ),
        migrations.AddField(
            model_name='teammatch',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='app.Team'),
        ),
        migrations.AddField(
            model_name='teammatch',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='app.Team'),
        ),
        migrations.AddField(
            model_name='team',
            name='capitaine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Utilisateur'),
        ),
        migrations.AddField(
            model_name='playermatch',
            name='score',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TennisScore'),
        ),
        migrations.AddField(
            model_name='playermatch',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='app.Utilisateur'),
        ),
        migrations.AddField(
            model_name='playermatch',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='app.Utilisateur'),
        ),
        migrations.AddField(
            model_name='participation',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Utilisateur'),
        ),
    ]
