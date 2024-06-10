"""
    @author: David Mamede
"""

from django.urls import path

from clients import views

urlpatterns = [
    path('clients/', views.list),
    path('clients/<int:id>', views.edit, name="Client Edit"),
    path('clients/new', views.new, name="Client New"),
    path('clients/delete/<int:id>', views.delete, name="Client Delete")
]
