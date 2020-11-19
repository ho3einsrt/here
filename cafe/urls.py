from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('add', views.AddUpdateCafe)

urlpatterns = []

urlpatterns += router.urls
