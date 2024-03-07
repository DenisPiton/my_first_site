from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home),
    path("", views.login2),
    path("req", views.submit),
    path("<int:item_id>/detail", views.card),
    path("profile", views.profile),
    path("profile/create_item", views.item_creating),
    path("create_item/api", views.create_item_tool)
]