import requests
import json
import os


'''
TMDB에서 영화 데이터를 받아와서 fixures에 json으로 저장하는 코드
'''

# API Key
# api_key = os.environ.get('TMDB_API_KEY')
api_key = "a24275eaaea1118ecc0e95751086b277"

# API URL
url = f"https://api.themoviedb.org/3/movie/popular"
params = {
    'api_key': api_key,
    'sort_by': 'vote_average.desc',
    'vote_count.gte': 100,
    'language':'ko-KR',
    'page': 1
}
# Number of pages to retrieve
num_pages = 50

# List to store movie data
movies = []

# Loop through pages and retrieve movie data
for page in range(1, num_pages+1):
    params["page"] = page
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    movies += data["results"]

# pre_precess data to choose fields which we will use
processed_movie_data = []
for movie in movies:
    processed_data = {
        "model": "movies.movie",
        "fields": {
            "title": movie["title"],
            "overview": movie["overview"],
            "genres": movie["genre_ids"],
            "popularity": movie["popularity"],
            "poster_path": movie["poster_path"],
            "backdrop_path": movie["backdrop_path"],
            "release_date": movie.get("release_date"),
            "vote_average": movie["vote_average"],
        }
    }
    processed_movie_data.append(processed_data)

# Save movie data to JSON file
with open("movies.json", "w", encoding='utf-8') as f:
    json.dump(processed_movie_data, f, ensure_ascii=False)


