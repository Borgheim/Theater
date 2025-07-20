from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add-actor/', views.add_actor, name='add_actor'),
    path('actors/', views.actor_list, name='actor_list'),
    path('directors/', views.director_list, name='director_list'),

]
