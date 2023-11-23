from django.urls import path,include

from . import views

urlpatterns = [path('hello/', views.say_hello, name='say_hello'),
               path('hellohtml/', views.say_hellohtml, name='say_hellohtml'),
               path('players/', views.list_players, name='list_players'),
               path('addplayer/', views.add_player, name='add_player'),
               path('updateplayer/', views.update_player, name='update_player'),
               path('deleteplayer/', views.delete_player, name='delete_player'),
              ]