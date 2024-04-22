from django.urls import path
from .views import RegisterUserApiView, LoginUserApiView, \
    UserApiView, UserDetailApiView
urlpatterns = [
    path('', UserApiView.as_view()),
    path('<uuid:id>/', UserDetailApiView.as_view()),
    path('register/', RegisterUserApiView.as_view()),
    path('login/', LoginUserApiView.as_view()),
  
]
