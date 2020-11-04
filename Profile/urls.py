from django.urls import path, re_path

from Profile import views

urlpatterns = [
    # re_path(r'^profileModel_url', views.ProfileModelView.as_view()),
    re_path(r'^userModel_url',views.UsersViewset.as_view()),
    re_path(r'^userModel_post/',views.UsersViewset.as_view()),
    path(r'userModel_delete/<int:pk>/',views.UsersViewset.as_view()),
    path(r'userModel_update/<int:pk>/',views.UsersViewset.as_view()),
]