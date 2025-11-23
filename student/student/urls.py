"""
URL configuration for student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studentapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    # Authentication
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # CRUD
    path('details/', views.student_details, name='student_details'),
    path('add/', views.add_student, name='add_student'),
    path('eligible/', views.eligible_students, name='eligible_students'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('profile/<int:id>/', views.student_profile, name='student_profile'),
]

