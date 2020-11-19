from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views

router = DefaultRouter()
router.register('', views.AddToken, basename='add_table')
router.register('<str:name>/', views.ShowTables, basename='show_table')

urlpatterns = []

urlpatterns += router.urls
