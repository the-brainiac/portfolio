from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('projects/', views.projects, name="projects"),

	path('send_email/', views.sendEmail, name="send_email"),
]