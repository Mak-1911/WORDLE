from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('playnow/',views.play,name = 'play'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('signout/',views.logout_view,name='logout'),
    path('playnow/wordlegame/',views.wordlegame,name='wordlegame'),
    path('playnow/wordlegame/playnow2/<key>',views.play2,name = 'play2'),
    path('leaderboard/',views.leaderboard,name='leaderboard'),
    path('choosetheme/',views.choosetheme,name='choosetheme'),
]
