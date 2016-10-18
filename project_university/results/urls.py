"""project_university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from results import views
from results.views import *

urlpatterns = [
    
    url(r'^hello/', views.hello, name="hello"),

    url(r'^hello_year/([0-9]{4})/$', views.hello_year, name="hello_year"),

    url(r'^find/([\w\-]+)/$', views.display_person, name="display_person"),
    
    url(r'^hello_year_month/([0-9]{4})/([0-9]{2})/$', views.hello_year_month, name="hello_year_month"),
    
    url(r'^year_archive/(?P<year>[0-9]{4})/$', views.year_archive, name="year_archive"),
    
    url(r'^person_registration/$', views.person_registration, name="person_registration"),

    url(r'^submit_person/$', views.submit_person, name="submit_person"),
    
    url(r'^display_all_person/$', views.display_all_person, name="display_all_person"),
    
    url(r'^student_list/$', StudentList.as_view(), name='student_list'),
    
    #url(r'^student_registration/$', views.student_registration, name='student_registration'),
       
    url(r'^create_student/$', CreateStudent.as_view(), name='create_student'),
    
    url(r'^delete_student/(?P<id>\d+)/$', DeleteStudent.as_view(), name='delete_student'),
    
    url(r'^details_student/(?P<pk>\d+)/', StudentDetail.as_view(template_name='results/student_detail.html'), name="details_student"),
     
    url(r'^update_student/(?P<id>\d+)/$', StudentUpdate.as_view(), name='update_student'), 
    
    url(r'^create_marks/$', CreateMarks.as_view(), name='create_marks'),
    
]
