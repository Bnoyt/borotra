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
        return redirect(index)
    post = request.POST
    if 'username' in post and 'email' in post and 'mdp' and 'mdp2' in post:
        if User.objects.filter(email=post['email']).exists() or User.objects.filter(username=post['username']).exists():

            context['message'] = "L'email ou le pseudo spécifié existe déjà"

            return render(request, 'register.html', context)
        else:
            if post["mdp"] != post["mdp2"]:
                context['message'] = "Inscrivez vous gratuitement sur Agorado et participez à la première plateforme d'intelligence collective en France"
                context["notif"] = "Les deux mots de passe ne correspondent pas"
                return render(request, 'register.html', context)

            user = User.objects.create_user(post['username'],post['email'],post['mdp'])
            personne = Utilisateur(user=user)
            personne.save()
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
    else:
        context['message'] = "Inscrivez vous gratuitement sur Agorado et participez à la première plateforme d'intelligence collective en France"
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

def tableausimple1(request):
    #call database
    context = {'page_propos':True}

    return render(request, 'tableau-simple1.html', context)

def tableausimple2(request):
    #call database
    context = {'page_propos':True}

    return render(request, 'tableau-simple2.html', context)

def tableausimple3(request):
    #call database
    context = {'page_propos':True}

    return render(request, 'tableau-simple3.html', context)


def tableauequipe(request):
    #call database
    context = {'page_propos':True}

    return render(request, 'tableau-equipe.html', context)