from django.urls import path
from .views import ClientApiView, ClientApiDetailView, OblastApiView, OblastApiDetailView, \
    RayonApiView, RayonDetailApiView, ClientDataAPIView, ClientDataDetailAPIView
urlpatterns = [
    path('', ClientApiView.as_view()),
    path('<uuid:id>/', ClientApiDetailView.as_view()),
    path('oblast/', OblastApiView.as_view()),
    path('oblast/<uuid:id>/', OblastApiDetailView.as_view()),
    path('rayon/', RayonApiView.as_view()),
    path('rayon/<uuid:id>/', RayonDetailApiView.as_view()),
    path('data/', ClientDataAPIView.as_view()),
    path('data/<str:client_id>/', ClientDataDetailAPIView.as_view()),
]
