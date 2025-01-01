import pickle
import streamlit as st
import pandas as pd
import requests


# Function to fetch movie poster
def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommended_movies_posters


# Load the movies and similarity data
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))

# Set up the page configuration
st.set_page_config(page_title="Movie Recommender System", layout="wide")

# Embed aesthetic background color and styling using CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2E3440;
        color: #D8DEE9;
    }

    .stApp header, .stApp footer {
        display: none;
    }

    .stButton>button {
        background-color: #5E81AC;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 16px;
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #81A1C1;
    }

    .stTextInput>div>div>input {
        background-color: #3B4252;
        color: #D8DEE9;
        border-radius: 5px;
        border: 1px solid #4C566A;
    }

    .movie-poster img {
        transition: transform 0.2s ease-in-out;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.4);
    }

    .movie-poster img:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.6);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Movie selection box
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'What would you like to watch?',
    movies['title'].values
)

# Display recommendations when the button is pressed
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    # Wrap images in a div with a custom class
    with col1:
        st.markdown(f'<div class="movie-poster"><img src="{posters[0]}" width="100%"></div>', unsafe_allow_html=True)
        st.text(names[0])
    with col2:
        st.markdown(f'<div class="movie-poster"><img src="{posters[1]}" width="100%"></div>', unsafe_allow_html=True)
        st.text(names[1])
    with col3:
        st.markdown(f'<div class="movie-poster"><img src="{posters[2]}" width="100%"></div>', unsafe_allow_html=True)
        st.text(names[2])
    with col4:
        st.markdown(f'<div class="movie-poster"><img src="{posters[3]}" width="100%"></div>', unsafe_allow_html=True)
        st.text(names[3])
    with col5:
        st.markdown(f'<div class="movie-poster"><img src="{posters[4]}" width="100%"></div>', unsafe_allow_html=True)
        st.text(names[4])
