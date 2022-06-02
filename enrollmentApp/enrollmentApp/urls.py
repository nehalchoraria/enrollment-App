"""enrollmentApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.urls import include, path
from university.views import UserViewDetail, UserViewList
from course.views import CourseViewDetail, CourseViewList, CourseSyllabusMappingViewDetail, CourseSyllabusMappingViewList
from syllabus.views import SyllabusViewDetail, SyllabusViewList
from student.views import StudentViewList, StudentViewDetail, findStudents

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('university/', UserViewList.as_view()),
    path('university/<int:pk>', UserViewDetail.as_view()),
    path('course/', CourseViewList.as_view()),
    path('course/<int:pk>', CourseViewDetail.as_view()),
    path('syllabus/', SyllabusViewList.as_view()),
    path('syllabus/<int:pk>', SyllabusViewDetail.as_view()),
    path('course-syllabus/', CourseSyllabusMappingViewList.as_view()),
    path('course-syllabus/<int:pk>', CourseSyllabusMappingViewDetail.as_view()),
    path('student/', StudentViewList.as_view()),
    path('student/<int:pk>', StudentViewDetail.as_view()),
    path('search-students/', findStudents)
]