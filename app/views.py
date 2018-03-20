from .models import *
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.core.urlresolvers import reverse

from django.template import loader

from django.contrib.auth.models import User


def authentification(request):
    email = request.POST['email']
    password = request.POST['mdp']
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return JsonResponse({"text":"success"})
    else:
        return JsonResponse({"text":"error"})


def page_login(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({"text":"deconnect"})
    if 'email' in request.POST:
        return authentification(request)
    else:

    	return JsonResponse({"text":"error"})

def deconnect(request):
	if request.user.is_authenticated:
		logout(request)
		return HttpResponseRedirect(reverse("index"))
	else:
		return HttpResponseRedirect(reverse("index"))


def page_register(request):
    context = {}
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("inscriptions"))
    post = request.POST
    if 'prenom' in post and 'email' in post and 'mdp' in post and 'mdp2' in post and 'nom' in post and 'promo' in post and 'ecole' in post and 'classement' in post:
        if  User.objects.filter(username=post['email']).exists():

            context['message'] = "L'email spécifié existe déjà"

            return render(request, 'register.html', context)
        else:
            if post["mdp"] != post["mdp2"]:
                context['message'] = "Inscrivez vous pour le plus grand tournoi de tennis depuis Vaneau"
                context["notif"] = "Les deux mots de passe ne correspondent pas"
                return render(request, 'register.html', context)

            user = User.objects.create_user(post['email'],post['email'],post['mdp'])
            personne = Utilisateur(user=user)
            personne.save()
            login(request,user)
            context={'page_index':True,'good_notif':"Inscription réussie : vous êtes maintenant connecté"}
            return render(request,"inscriptions.html",context)
    else:
        context['message'] = "Inscrivez vous pour le plus grand tournoi de tennis depuis Vaneau"
        if "csrfmiddlewaretoken" in post:
            context["notif"] = "Vous avez oublié de remplir un champ !"
        return render(request, 'register.html', context)

def index(request):
    #call database
    context = {'page_index':True}

    return render(request, 'index.html', context)
        
def faq(request):
    #call database
    context = {'page_faq':True}

    return render(request, 'index.html', context)

def tableaux(request):
    #call database
    context = {'page_tableaux':True,
    		'nom_page':'Les tableaux',
    		}

    return render(request, 'tableaux.html', context)

def palmares(request):
    #call database
    context = {'page_palmares':True}

    return render(request, 'index.html', context)

def profil(request):
    #call database
    context = {'page_profil':True}

    return render(request, 'index.html', context)

def matchs(request):
    #call database
    context = {'page_matchs':True}

    return render(request, 'index.html', context)

def propos(request):
    #call database
    context = {'page_propos':True}

    return render(request, 'index.html', context)

def inconstruct(request):
    #call database
    context = {'page_propos':True}

    return render(request, 'inconstruct.html', context)

def inscriptions(request):
    #call database
    if request.user.is_authenticated:
        utilisateur = get_object_or_404(Utilisateur,user = request.user)
        pas_inscris_simple = not(Participation.objects.filter(utilisateur=utilisateur,tournoi="0").exists())
        pas_inscris_equipes = not(Participation.objects.filter(utilisateur=utilisateur,tournoi="0").exists())

        context = {
            "pas_inscris_equipes":pas_inscris_equipes,
            "pas_inscris_simple":pas_inscris_simple,

        }
        return render(request, 'inscriptions.html', context)
    else:
        return HttpResponseRedirect(reverse("page_register"))


def inscription_simple(request):
    if request.user.is_authenticated:
        utilisateur = get_object_or_404(Utilisateur,user = request.user)
        pas_inscris_simple = not(Participation.objects.filter(utilisateur=utilisateur,tournoi="0").exists())
        if pas_inscris_simple:
            a = Participation(tournoi="0",utilisateur=utilisateur)
            a.save()
            pas_inscris_simple = not(Participation.objects.filter(utilisateur=utilisateur,tournoi="0").exists())
            pas_inscris_equipes = not(Participation.objects.filter(utilisateur=utilisateur,tournoi="0").exists())
            context = {
                "pas_inscris_equipes":pas_inscris_equipes,
                "pas_inscris_simple":pas_inscris_simple,
                "good_notif":"Vous avez bien été inscrit en simple pour le tournoi Borotra. Nous vous recontacterons bientôt par mail pour vous informer du début de la compétition",

            }
    else:

        context = {
                "pas_inscris_equipes":pas_inscris_equipes,
                "pas_inscris_simple":pas_inscris_simple,
                "notif":"Il y a eu une erreur, merci de réessayer ou de nous contacter par mail",

            }



    return render(request,"inscriptions.html",context)

def inscription_equipes(request):
    if request.user.is_authenticated:
        utilisateur = get_object_or_404(Utilisateur,user = request.user)
        pas_inscris_equipes = not(Participation.objects.filter(utilisateur=utilisateur,tournoi="0").exists())
        post = request.POST
        if pas_inscris_equipes:
            if "joueur2_prenom" in post and "joueur2_nom" in post and  "joueur2_classement" in post and  "joueur3_prenom" in post and  "joueur3_nom" in post and  "joueur3_classement"  in post and "joueur4_prenom" in post and  "joueur4_nom" in post and  "joueur4_classement" and "nom" in post:
                a = Participation(tournoi="1",utilisateur=utilisateur)
                a.save()
                t = Team("nom" = post["nom"],capitaine=utilisateur,joueur2_prenom=post["joueur2_prenom"],joueur2_nom=post["joueur2_nom"],joueur2_classement=post["joueur2_classement"],joueur3_prenom=post["joueur3_prenom"],joueur3_nom=post["joueur3_nom"],joueur3_classement=post["joueur3_classement"],joueur4_prenom=post["joueur4_prenom"],joueur4_nom=["joueur4_nom"],joueur4_classement=post["joueur4_classement"])
                t.save()
                pas_inscris_simple = not(Participation.objects.filter(utilisateur=utilisateur,tournoi="0").exists())
                pas_inscris_equipes = not(Participation.objects.filter(utilisateur=utilisateur,tournoi="0").exists())
                context = {
                    "pas_inscris_equipes":pas_inscris_equipes,
                    "pas_inscris_simple":pas_inscris_simple,
                    "good_notif":"Vous avez bien été inscrits en équipes pour le tournoi Borotra. Nous vous recontacterons bientôt par mail pour vous informer du début de la compétition",

                }
    else:

        context = {
                "pas_inscris_equipes":pas_inscris_equipes,
                "pas_inscris_simple":pas_inscris_simple,
                "notif":"Il y a eu une erreur, merci de réessayer ou de nous contacter par mail",

            }



    return render(request,"inscriptions.html",context)