"""
URL configuration for estagios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from estagioapps.views import internship_list, internship_detail,home,\
    login,signup,profile,logout,search,\
    add_review,remove_review,edit_review


from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),



    #Allauth
    path("accounts/", include("allauth.urls")),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path ("search", search, name="search"),


    path("accounts/profile/", TemplateView.as_view(template_name="profile.html")),
    path('internships/', internship_list, name='internship_list'),
    path('internships/<int:company_id>/', internship_detail, name='internship_detail'),
    path('add_review/<int:company_id>/', add_review, name='add_review'),
    path('remove_review/<int:company_id>/<int:review_id>/', remove_review, name='remove_review'),
    path('edit_review/<int:company_id>/<int:review_id>/', edit_review, name='edit_review'),

    # Add more URLs as needed
]

