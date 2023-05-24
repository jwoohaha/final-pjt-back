from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Genre
from articles.models import Article
from .serializers import MovieSerializer, MovieListSerializer
from articles.serializers import ArticleListSerializer

from collections import defaultdict


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


@api_view(['GET'])
def movie_recommend(request, user_pk):
    '''
    사용자 취향에 맞는 영화 리스트 리턴
    '''

    # user가 남긴 감상평을 토대로 장르별 평점 반영
    article_list = get_list_or_404(Article, user=user_pk)  # user가 남긴 감상평
    n = len(article_list)
    genre_count = defaultdict(int)
    for i in range(n):
        movie = article_list[i].movie
        rating = article_list[i].rating
        genre_list = get_list_or_404(Genre, movie=movie.id)
        for genre in genre_list:
            genre_count[genre.id] += rating - 5
    # print(genre_count)

    recommend_candidates = get_list_or_404(Movie.objects.order_by('-vote_average')[:200])
    personalized_score = []
    # 개인화 된 점수를 계산하여 정렬
    # 평점 기반 선호 장르 + popularity + vote_average 고려 
    for cand in recommend_candidates:
        score = cand.popularity/1000 + cand.vote_average
        genre_list = get_list_or_404(Genre, movie=cand.id)
        for genre in genre_list:
            score += genre_count[genre.id] * 100000
        personalized_score.append((score, cand, cand.pk, cand.title))
    personalized_score.sort(reverse=True)
    recommend_list = []
    for i in range(20):
        recommend_list.append(personalized_score[i][1])
    print(recommend_list)
    serializer = MovieListSerializer(recommend_list, many=True)
    return Response(serializer.data)