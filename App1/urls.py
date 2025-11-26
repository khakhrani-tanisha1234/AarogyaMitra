from django.contrib import admin
from django.urls import path
from App1 import views

urlpatterns = [
    path("",views.index, name="home"),
    path("home",views.index, name="homepage"),
    path("features",views.features, name="features"),
    path("contact",views.Contact, name="contact"),
    path("about",views.About, name="about"),
    path("login",views.Login, name="login"),
    path("signup",views.SignUp, name="signup"),
    path("pulse",views.pulse, name="pulse"),
    path("doctor",views.documentation, name="doctor"),
    path('schedule-therapy', views.schedule_therapy, name='schedule_therapy'),
    path('send_notification', views.send_notification, name='send_notification'),
    path("patient",views.education, name="patient"),
    path("prescription",views.prescription, name="prescription"),    
    
]
