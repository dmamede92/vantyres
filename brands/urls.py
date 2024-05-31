"""
    @author: David Mamede
"""

from django.urls import path

from brands import views

# Create your views here.
urlpatterns = [
    path('brands/', views.list),
    path('brands/<int:id>', views.edit, name="User Edit"),
    path('brands/new', views.new, name="User New"),
    path('brands/delete/<int:id>', views.delete, name="User Delete")
]
