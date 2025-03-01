from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("diary/", views.diary, name="diary"),
    path('update-nutrition/', views.update_nutrition, name='update_nutrition'),
]