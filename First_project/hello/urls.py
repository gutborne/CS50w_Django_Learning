from django.urls import path

from . import views #in order to use views, we have to import it


#urlpatterns will tell us which urls are allowed to be accessed from the app hello.


#worse mode
'''
urlpatterns = [
    path("", views.index, name="index"),
    path("mateus", views.mateus, name="mateus"),
    path("marlena", views.Marlena, name="Marlena"),
    path("zuzia", views.zuzia, name="Zuzia"),
]
'''

#better way
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:user>", views.greetings_user, name="greetings")
]

#
