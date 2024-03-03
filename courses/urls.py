"""smartlearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path 
from .views import CourseDashboardView, CourseDetailView, CourseListView
from courses import views 
urlpatterns = [
    path('courses', CourseListView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('userpage', views.userpage, name='userpage'),
    path('userpage/<int:pk>/', CourseDashboardView.as_view(), name='page_detail'),
    # path('userpage', CourseView.as_view(), name='userpage'),
    # path('playlist', views.playlist, name='playlist'),
    
    # path('playlistcss', views.playlistcss, name='playlistcss'),
    # path('playlistjs', views.playlistjs, name='playlistjs'),
    # path('enroll/<int:course_id>/', views.enroll_in_course, name='enroll_in_course'),
    # path('complete_lesson/<int:course_id>/<int:lesson_id>/', views.complete_lesson, name='complete_lesson'),
    # path('generate_certificate/<int:course_id>/', views.generate_certificate, name='generate_certificate'),
]