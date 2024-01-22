from django.urls import path
from . import views
urlpatterns=[
    path('',views.login,name="login"),
    path('Newuser-registration/',views.createuser,name="newuser"),
    path('login_request/', views.login_request, name='login_request'),
    path('Newuser-registration/Newuser-registration/',views.createuser),
    path('search/',views.search,name="search"),
    path('chat/',views.chat,name="chat"),
]