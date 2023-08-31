from . import views
from  django.urls import  path

urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('', views.home, name='home'),
    path('district/<int:district_id>/', views.district_wikipedia, name='district_wikipedia'),
    path('logout', views.logout, name='logout'),
    path('applicant/', views.applicant_form_view, name='applicant_form'),
    path('success/', views.success, name='success'),
    path('api/get_branches/', views.get_branches_api, name='get_branches_api'),
]