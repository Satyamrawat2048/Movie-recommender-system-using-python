import streamlit as st
import pickle
import pandas as pd
import requests
st.title('Movie Recommender System')

def fetch_poster(id):
    response =requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8517a7947531f5365c5a67e661a4696f&language=en-US".format(id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']

mov_dict=pickle.load(open('moviesdict.pkl','rb'))
similarity= pickle.load(open('similarity.pkl','rb'))
movies= pd.DataFrame(mov_dict)

movie_ch = st.selectbox('Choose a movie to recommend :',movies['title'].values)


def recommend(movie):
    ind = movies[movies['title'] == movie].index[0]
    distances = similarity[ind]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetching poster from api using id
        recommended_movies_posters.append(fetch_poster(id))

    return recommended_movies, recommended_movies_posters


if st.button('Recommend me'):
    rec_movies,posters = recommend(movie_ch)

    col1,col2,col3,col4 , col5= st.beta_columns(5)

    with col1:
        st.text(rec_movies[0])
        st.image(posters[0])
    with col2:
        st.text(rec_movies[1])
        st.image(posters[1])
    with col3:
        st.text(rec_movies[2])
        st.image(posters[2])
    with col4:
        st.text(rec_movies[3])
        st.image(posters[3])
    with col5:
        st.text(rec_movies[4])
        st.image(posters[4])
