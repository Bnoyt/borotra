from __future__ import unicode_literals
import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

class Utilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DROITS = (
        ('0', 'admin'),
        ('1', 'joueur'),
    )
    profil = models.CharField(max_length=1, choices=DROITS, default='1')
    promo = models.IntegerField(default=2016)
    ecole = models.CharField(max_length=35,default="Polytechnique")
    classement = models.CharField(max_length=10,default="NC")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.classement

class Team(models.Model):
    capitaine = models.ForeignKey(Utilisateur)
    nom = models.CharField(max_length=30)
    joueur2_prenom = models.CharField(max_length=100)
    joueur2_nom = models.CharField(max_length=100)
    joueur2_classement = models.CharField(max_length=100)
    joueur3_prenom = models.CharField(max_length=100)
    joueur3_nom = models.CharField(max_length=100)
    joueur3_classement = models.CharField(max_length=100)
    joueur4_prenom = models.CharField(max_length=100)
    joueur4_nom = models.CharField(max_length=100)
    joueur_classement = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    
class Participation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur)
    TOURNOIS = (
        ('0','simple'),
        ('1','équipes')
    )
    tournoi = models.CharField(max_length=1, choices=TOURNOIS, default='1')
    date_inscription = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.utilisateur) + " --> " + self.tournoi

class TennisScore(models.Model):
    TYPESMATCHS = (
        ('0', 'debutants'),
        ('1', 'nextgen'),
        ('2', 'classique')
    )
    typematch = models.CharField(max_length=1, choices=TYPESMATCHS, default="1")
    s1j1 = models.IntegerField(default=0)
    s1j2 = models.IntegerField(default=0)
    s2j1 = models.IntegerField(default=0)
    s2j2 = models.IntegerField(default=0)
    s3j1 = models.IntegerField(default=0)
    s3j2 = models.IntegerField(default=0)

    def __str__(self):
        if self.s3j1 != 0 and self.s3j2 !=0:
            return self.s1j1 + "/" + self.s1j2 + " - " + self.s2j1 + "/" + self.s2j2 + " - " + self.s3j1 + "/" + self.s3j2 
        else:
            return self.s1j1 + "/" + self.s1j2 + " - " + self.s2j1 + "/" + self.s2j2

class PlayerMatch(models.Model):
    user1 = models.ForeignKey(Utilisateur,related_name="user1")
    user2 = models.ForeignKey(Utilisateur,related_name="user2")
    date_prevue = models.DateField(default=datetime.date.today)
    date_match = models.CharField(max_length=20)
    STATUTS = (
        ('0', 'à jouer'),
        ('1', 'joué'),
        ('2', 'forfait')
    )
    TYPESMATCHS = (
        ('0', 'debutants'),
        ('1', 'nextgen'),
        ('2', 'classique')
    )
    typematch = models.CharField(max_length=1, choices=TYPESMATCHS, default="1")
    score = models.ForeignKey(TennisScore)

    def __str__(self):
        return str(self.user1) + " vs " + str(self.user2)

class TeamMatch(models.Model):
    team1 = models.ForeignKey(Team,related_name="team1")
    team2 = models.ForeignKey(Team,related_name="team2")
    date_prevue = models.DateField(default=datetime.date.today)
    date_match = models.CharField(max_length=20)
    STATUTS = (
        ('0', 'à jouer'),
        ('1', 'joué'),
        ('2', 'forfait')
    )
    score_simple1 = models.ForeignKey(TennisScore,related_name="score_simple1")
    score_simple2 = models.ForeignKey(TennisScore,related_name="score_simple2")
    score_double = models.ForeignKey(TennisScore,related_name="score_double")

    def __str__(self):
        return str(self.team1) + " vs " +  str(self.team2)
