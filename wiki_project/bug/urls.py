from django.urls import path
from . import views

#creation of urls for our views
urlpatterns = [
    path('register/', views.register_bug, name='register-bug'),
    path('bug/<int:bug_id>/', views.detail, name='detail'),
    path('bug_list/', views.bug_list, name='bug-list'),
]