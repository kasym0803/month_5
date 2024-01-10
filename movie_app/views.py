from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import (MovieSerializer,
                          DirectorSerializer,
                          ReviewSerializer,
                          MovieReviewSerializer,
                          MovieValidateSerializer,
                          DirectorValidateSerializer,
                          ReviewValidateSerializer)


@api_view(['GET', 'PUT', 'DELETE'])
def director_view_id(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error: Director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(director)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': serializer.data})
        director.name = serializer.validated_data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def director_view(request):
    if request.method == 'GET':
        director = Director.objects.all().prefetch_related('movies')
        serializer = DirectorSerializer(director, many=True)
        return Response(data=serializer.data)
    else:
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

        elif request.method == 'POST':
            name = request.data.get('name')
            director = Director.objects.create(name=name)
            serializer = DirectorSerializer(director)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_view_id(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error: Director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie)
    if request.method == 'GET':
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': serializer.errors})
        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director_id')
        movie.save()
        return Response(data=MovieSerializer(movie).data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movie_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(data=serializer.data)
    else:
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

        elif request.method == 'POST':
            title = request.data.get('title')
            description = request.data.get('description')
            duration = request.data.get('duration')
            director_id = request.data.get('director_id')
            movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
            serializer = MovieSerializer(movie)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_view_id(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error: Director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': serializer.errors})
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(data=serializer.data)
    else:
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

        elif request.method == 'POST':
            text = request.data.get('text')
            movie_id = request.data.get('movie_id')
            stars = request.data.get('stars')
            review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
            serializer = ReviewSerializer(review)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_review_view_id(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error: Director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MovieReviewSerializer(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_review_view(request):
    movie = Movie.objects.all()
    serializer = MovieReviewSerializer(movie, many=True)
    return Response(data=serializer.data)
