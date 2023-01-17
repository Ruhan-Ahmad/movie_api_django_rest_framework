from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename="users")  # url for admin to view all users of movie_info app
router.register(r'movies', views.MovieViewSet, basename="movies")  # url for movies info
router.register(r'currentuser', views.CurrentUser, basename='currentuser')  # url for current user

urlpatterns = [
    path('', include(router.urls)),
    path(r'rate/<int:movie_id>/', views.MovieReview.as_view(), name='rate_detail')
]
