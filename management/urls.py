from django.urls import path , include
from rest_framework import routers
from . import views
from .views import signup , signin, package_list,package_create,package_detail , logout
urlpatterns = [
    path('', views.index, name='index'),
    path('packagelist/', package_list, name='package_list'),
    path('package/<int:pk>/', package_detail, name='package_detail'),
    path('package/create/', package_create, name='package_create'),
    # path('packages',views.packages, name='packages'),
    path('signup', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
]

# router = routers.DefaultRouter()
# router.register('package', views.PackageViewSet, basename='package')
# # router.register('magazine', views.MagazineViewSet, basename='magazine')
# # router.register('movies', views.PictureViewSet, basename='movies')
# urlpatterns= router.urls