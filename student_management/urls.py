from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_student, name="home"),
    path("update/<int:id>", views.update_student, name="update"),
    path("delete/<int:id>", views.delete_student, name="delete"),
    path("add/", views.add_student, name="add"),
    path("search_student/", views.search_student, name="search")


]
