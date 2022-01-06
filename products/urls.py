from django.urls import path, re_path

from . import views

app_name = 'products'

urlpatterns = [
    path('categories/', views.CategoriesList.as_view()),
    path('categories/<int:pk>/', views.CategoriesDetail.as_view()),
    path('screws/', views.ScrewsList.as_view()),
    path('screws/<int:pk>/', views.ScrewsDetail.as_view()),
]