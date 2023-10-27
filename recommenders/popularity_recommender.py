from recommenders import data_movies, data_ratings, default_poster_url
import pandas as pd


def recommend_popular_movies():

    ######################################################################################################

    movie_ratings = pd.merge(data_movies, data_ratings, on = 'movieId')
    movie_ratings = movie_ratings.groupby('title')['rating'].mean().sort_values(ascending = False).head(20)
    movie_ratings = movie_ratings.to_dict()
    #######################################################################################################
    response = []

    for movie in movie_ratings:
        movie_record = data_movies[data_movies.title == movie].iloc[0]
        movie_poster = str(movie_record.poster_link)
        response.append({
            "movieId": int(movie_record.movieId),
            "title": str(movie),
            "image": movie_poster if movie_poster != "nan" else default_poster_url,
            "genres": str(movie_record.genres).split("|"),
            "average_rating": movie_ratings[movie]
        })


    return {"status": True, "data": {"message": "Here are some of the popular recommendations.", "results" : response}}