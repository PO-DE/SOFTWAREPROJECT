from django.urls import path , include
from rest_framework import routers
from . import views
from .views import signup , signin
urlpatterns = [
    path('', views.index, name='index'),
    path('packages',views.packages, name='packages'),
    path('signup', signup, name='signup'),
    path('signin/', signin, name='signin'),
]

# router = routers.DefaultRouter()
# router.register('package', views.PackageViewSet, basename='package')
# # router.register('magazine', views.MagazineViewSet, basename='magazine')
# # router.register('movies', views.PictureViewSet, basename='movies')
# urlpatterns= router.urls