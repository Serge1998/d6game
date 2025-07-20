from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('historique/', views.historique, name='historique'),
    
    # Authentification
    path('login/', auth_views.LoginView.as_view(template_name='game/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    
    # API
    path('api/derniere-partie/', views.derniere_partie_ajax, name='derniere_partie_ajax'),
    path('api/historique/', views.historique_ajax, name='historique_ajax'),

    # Réinitialisation du mot de passe
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='game/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='game/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='game/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='game/password_reset_complete.html'), name='password_reset_complete'),
]
