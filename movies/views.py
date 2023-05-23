from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer, MovieListSerializer


@api_view(['GET'])
def movie_list_popular(request):
    '''
    최근 인기 있는 상위 20개 영화 데이터를 응답
    '''
    movies = get_list_or_404(Movie.objects.order_by('id')[:20])
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list_top20(request):
    '''
    평점 순으로 상위 20개 영화 데이터를 응답
    '''
    movies = get_list_or_404(Movie.objects.order_by('-vote_average')[:20])
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    '''
    영화의 상세 데이터 응답
    '''
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def movie_search(request, search_string):
    '''
    제목에 search_string을 포함하는 모든 영화를 리턴
    '''
    search_movie_list = Movie.objects.filter(title__icontains=search_string)
    serializer = MovieListSerializer(search_movie_list, many=True)
    return Response(serializer.data)