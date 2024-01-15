from django.urls import path
from . import views


urlpatterns = [
    # path('register/', views.register),
    path('register/', views.RegisterView.as_view()),
    # path('confirm/', views.confirm),
    path('confirm/', views.ConfirmView.as_view()),
    # path('login/', views.login_view),
    path('login/', views.LoginView.as_view()),
]
