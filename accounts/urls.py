from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),
    path('patient_register/', views.patient_register.as_view(), name='patient_register'),
    path('doctor_register/', views.doctor_register.as_view(), name='doctor_register'),
    path('staff_register/', views.staff_register.as_view(), name='staff_register')
]