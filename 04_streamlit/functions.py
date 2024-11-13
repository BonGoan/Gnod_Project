import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import spotipy
import streamlit as st
import pickle as pkl
import os
from IPython.core.display import display, HTML

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= st.secrets.client_id,
                                                           client_secret= st.secrets.client_secret))


def load_models():
    global df_playlist_new, kmeans_model, scaler_model  # Declare as global to access in other functions

    try:
        # Load dataset
        df_playlist_new = load_data()

        # Load KMeans model
        with open('04_streamlit/kmeans.pkl', 'rb') as file:
            kmeans_model = pkl.load(file)

        # Load Scaler model
        with open("04_streamlit/scaler.pkl", 'rb') as file:
            scaler_model = pkl.load(file)

    except EOFError as e:
        st.error(f"Error loading model: {e}")
        st.stop()  # Stops the app execution





def load_data():
    file_path = os.path.join(os.path.dirname(__file__), '../01_data/df_playlist_new.csv')
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        raise


def bring_song(song_name):
    result = sp.search(q=song_name, limit=1, market="DE")
    song_id = result['tracks']['items'][0]['id']  # Get the song ID
    
    return song_id


def classify_song (selected_id):
    features= sp.audio_features(selected_id)
    song_features = pd.DataFrame(features)
    song_features= song_features [["danceability", "energy", "loudness", "speechiness", "acousticness",
                 "instrumentalness", "liveness", "valence", "tempo", "id", "duration_ms"]]
    song_features= song_features.drop ("id", axis=1)
    
    pred_cluster = kmeans_model.predict(song_features)
    
    pred_cluster= pred_cluster[0]                          
   
    
    return pred_cluster


def song_recommender(pred_cluster):
    same_cluster_songs = df_playlist_new.loc[df_playlist_new["cluster_knn"] == pred_cluster]
    recommended_songs = same_cluster_songs.sample(n=3)
    return recommended_songs
    #{
        #'names': recommended_songs['names'].tolist(),
        #'ids': recommended_songs['id'].tolist()
    #}

def bring_track_id(recommended_songs):
    track_id = recommended_songs['id'][0]
    return track_id

# Step 3: Play Song Function
def play_song(track_id):
    spotify_embed_code = f"""
    <iframe src="https://open.spotify.com/embed/track/{track_id}" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
    """
    outcome = display(HTML(spotify_embed_code))
    return outcome



# Play the first recommended song
#track_id = recommended_songs['ids'][0]
#embed_code = play_song(track_id)

# Display the embed code (as HTML in Jupyter)
#display(HTML(embed_code))

#Bring track_id and show display
#track_id_new = bring_track_id(recommended_songs)
#display = play_song(track_id_new)
