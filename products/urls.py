from django.urls import path
from .views import CategoryApiView, CategoryDetailApiView, ProductApiView, ProductDetailApiVew, OrderApiView, OrderDetailApiView

urlpatterns = [
    path('', ProductApiView.as_view()),
    path('<uuid:id>/', ProductDetailApiVew.as_view()),
    path('category/', CategoryApiView.as_view()),
    path('category/<uuid:id>/', CategoryDetailApiView.as_view()),
    path('order/', OrderApiView.as_view()),
    path('order/<uuid:id>/', OrderDetailApiView.as_view())
]