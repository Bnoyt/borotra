from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.page_login, name='login'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^tableaux/$', views.tableaux, name='tableaux'),
    url(r'^a-propos/$', views.propos, name='a-propos'),
    url(r'^palmares/$', views.palmares, name='palmares'),
    url(r'^profil/$', views.profil, name='profil'),
    url(r'^matchs/$', views.matchs, name='matchs'),
    url(r'^deconnect/$', views.deconnect, name='deconnect'),
    url(r'^tableau-simple1/$', views.tableausimple1, name='tableau-simple1'),
    url(r'^tableau-simple2/$', views.tableausimple2, name='tableau-simple2'),
    url(r'^tableau-simple3/$', views.tableausimple3, name='tableau-simple3'),
    url(r'^tableau-equipes/$', views.tableauequipe, name='tableau-equipes'),


]
