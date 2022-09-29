from django.urls import re_path as url,path
from card_management import views 
# from .views import LoginView,UserView,LogoutView
 
urlpatterns = [ 
    # path('login', LoginView.as_view()),
    # path('user', UserView.as_view()),
    # path('logout', LogoutView.as_view()),
    

    url(r'^api/card_management/user$', views.User_list),
    url(r'^api/card_management/user/login$', views.user_login),
    url(r'^api/card_management/user/(?P<pk>[0-9]+)$', views.user_detail),
    url(r'^api/card_management/card$', views.Card_list),
    url(r'^api/card_management/card/(?P<pk>[0-9]+)$', views.Card_detail),
    # url(r'^api/card_management$', views.user_list_published),

    ]