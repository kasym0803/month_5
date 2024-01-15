from django.urls import path
from . import views


urlpatterns = [
    # path('director/', views.director_view),
    path('director/', views.DirectorListAPIView.as_view()),
    # path('director/<int:id>/', views.director_view_id),
    path('director/<int:id>/', views.DirectorDetailAPIView.as_view()),

    # path('movie/', views.movie_view),
    path('movie/', views.MovieListAPIView.as_view()),
    # path('movie/<int:id>/', views.movie_view_id),
    path('movie/<int:id>/', views.MovieDetailAPIView.as_view()),

    path('movie/review/', views.movie_review_view),
    path('movie/review/<int:id>/', views.movie_review_view_id),

    # path('review/', views.review_view),
    path('review/', views.ReviewListAPIView.as_view()),
    # path('review/<int:id>/', views.review_view_id),
    path('review/<int:id>/', views.ReviewDetailAPIView.as_view()),
]

