from django.urls import path, include

# from .views import LatestProductsList
from product import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
]
