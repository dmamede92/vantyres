"""
    @author: David Mamede
"""

from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.list),
    path('users/<int:id>', views.edit, name="User Edit"),
    path('users/new', views.new, name="User New"),
    path('users/delete/<int:id>', views.delete, name="User Delete"),
    path('users/login/', views.custom_login, name='login'),
    path('users/logout/', views.custom_logout, name='logout')
]
