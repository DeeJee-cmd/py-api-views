from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
)

router = routers.DefaultRouter()
router.register(
    r"cinema_hall",
    CinemaHallViewSet,
    basename="cinema_hall",
)
router.register(
    r"movies",
    MovieViewSet,
    basename="movies",
)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("", include(router.urls)),
]
