from django.urls import path
from .views import add_course, add_instructor

urlpatterns = [
    path('add-course/', add_course, name='add_course'),
    path('add-instructor/', add_instructor, name='add_instructor'),
]
