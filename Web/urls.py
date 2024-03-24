from django.urls import path
import Web.views as view

urlpatterns = [
    path('', view.Home.as_view(), name='home'),
    path('<str:page>', view.Home.as_view(), name='page'),
]
