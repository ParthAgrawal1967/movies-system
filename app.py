import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=933906e0d3729320add2ed9d400df4cb&language=en-US'.format(movie_id))
    data=response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
movies_dict=pickle.load(open('movies_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('simil.pkl', 'rb'))
def set_background():
    background_image_url = "https://s3.amazonaws.com/prod-cdata-secure.sprinklr.com/DAM/3877/24737d83-468d-4a04-859f-7df4b95df217-1390968249/what_is_netflix_1_en.png?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLWVhc3QtMSJGMEQCICqzeu%2BZaPYilKcN0WQhRgQk6SGD3FPNWBjTUkmgwg2sAiBgUBYyuncNQZE1pD3KiPo2Kz7IzRpNWjbESgaRzuB%2BQiqxBQg%2BEAAaDDg2OTM2NzQ3MTY3NCIMgbCGyar2AFamCNaYKo4FC8LPbxtqukMjVkzLSK6vt%2Fzh%2FghvRe4yDKLA9i3QxNpvBm3yzRurvXTHk1g%2Ff1M8EHkNUcmRYQlKSVrlkx9IEGHjCCqnxQ6gk%2B5v8tQjL462Y5MnThuI%2B10iZ0O7ROlzIRyPGWQHeHRGRmrbivZzFKs8agaX9p8CW3u4qAlYHqSkCvn2gAnDVw4pCq7fRVR4%2FBDkOC%2F1ZoXWvL3EssNAxeGMtEwSPJ6xoMvJm77%2FUoIyQMpA8PU2zwG6eJIMK7C7R6tYNkxC9%2FcVB31OXHn3Vv%2BANmmWL%2BmSBV3lDoET%2FIyDjux%2Fiapu3e%2BFR4pPNai%2BbNWdRDV%2FVM5m3ysYaPh1ZaGKveWCKQgorFs8OwSmuqUkJEa9CKfKv5VszonmmNKW16NjmutU4xpvIuNxOxz6GbsCSaS2wCTDzGaoUGS0VZxj6LtAGXaGo6bLIFNthAYLtsDA24JX%2F9r%2B%2FV2pAd402fgeOcB743kMVjBY3aE2Gh1hYGrlk9aNkKva6qrGyvKCHpX3A3%2BsSebcUeNEAzcKzTfGy69XznbxwhFRrJS2C%2BkS4SeLNq10gLeoPsiR5foVY0k6zIi2Wx2Krm4EQT0R9P1EPBvMRms2rz5S2hj19Yk%2BmGAWKhs7bNgVBzK6pN%2BDhuPf2084%2FT6vOlE0NvYRWByqoG0q2K4QO2uL5jRe%2FCO1RJDH%2BwBjLF6W%2Ff1MI2ahJqPUcKSJFClsjArE7R0Wt0yyJcJIpU%2FVWj7ohhnCI59PyV6diNj844DuzIs08tsgpVRFW4ba5oAV9XZu3v5kt3vjF%2Fm9fVVnFezLJzrxW4AF83Po%2BMYaPP2tzdfPxDpzxuVF%2F71TVIqsBrjcVmZ9%2FRZ68pV6yI3ofhJOnHDlMLvDwL0GOrIBH%2FWSn0EERaKT3h38YYNEPLZ0gwH965CTJ5mI6el8v%2FE%2FTuxEIcgJUsNIoAsZuK8r7B8ueZRaykKpiOVAwL1txRvSAtm%2FH6K4fB5U8lE5qs2yg3lWK4PWhgu%2ByPiDGc%2FuOa2UDKliX2%2FZ%2BYpI31B75ELRwLpKgsTcGAOAg%2BN%2BC6quVfS4lxZJRCq5jB1%2BrgCord5mcp6DDjCp%2B0CMgTCUS%2F2trSfvHkyp0Ld0yLAhKafmVA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250215T053841Z&X-Amz-SignedHeaders=host&X-Amz-Expires=1800&X-Amz-Credential=ASIA4U2SW3Y5ACB2PCEJ%2F20250215%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b60a4c6c8b766dd2aed907b6c8a6d29d2ae81574fd27716bd064601942492822"  # Change this to your image URL
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Apply background
set_background()
st.markdown("<h1 style='text-align: center; color: black;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Find your next favorite movie!</h3>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: black;'>Choose a movie for recommendations:</h4>", unsafe_allow_html=True)
selected_movie_name = st.selectbox("", movies['title'].values)


if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(f"<h4 style='text-align: center; color: black;'>{names[0]}</h4>", unsafe_allow_html=True)

        st.image(posters[0])

    with col2:
        st.markdown(f"<h4 style='text-align: center; color: black;'>{names[1]}</h4>", unsafe_allow_html=True)

        st.image(posters[1])

    with col3:
        st.markdown(f"<h4 style='text-align: center; color: black;'>{names[2]}</h4>", unsafe_allow_html=True)

        st.image(posters[2])

    with col4:
        st.markdown(f"<h4 style='text-align: center; color: black;'>{names[3]}</h4>", unsafe_allow_html=True)

        st.image(posters[3])

    with col5:
        st.markdown(f"<h4 style='text-align: center; color: black;'>{names[4]}</h4>", unsafe_allow_html=True)

        st.image(posters[4])