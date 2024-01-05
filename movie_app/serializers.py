from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Movie, Director, Review


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

    def get_movies_count(self, obj):
        return obj.movies.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie stars'.split()


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id title description duration director reviews'.split()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=55, min_length=5)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, min_length=5)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(min_value=3, max_value=150)
    director_id = serializers.IntegerField(required=False)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError("Director does not exist")
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=156, min_length=1)
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField(max_value=5, min_value=1)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError("Movie does not exist")
        return movie_id
