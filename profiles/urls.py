"""
    @author: David Mamede
"""

from django.urls import path

from profiles import views

# Create your views here.
urlpatterns = [
    path('profiles/', views.list),
    path('profiles/<int:id>', views.edit, name="User Edit"),
    path('profiles/new', views.new, name="User New"),
    path('profiles/delete/<int:id>', views.delete, name="User Delete")
]
