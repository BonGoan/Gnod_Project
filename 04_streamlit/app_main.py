import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from functions import bring_song, classify_song, song_recommender, load_data, load_models
from IPython.core.display import display, HTML

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= st.secrets.client_id,
                                                           client_secret= st.secrets.client_secret))

load_data ()
load_models ()

# Streamlit App
def main():

    st.title("Spotify Song Recommender")

    # Menu options
    options = ["Home", "Songs"]
    choice = st.sidebar.selectbox("Menu", options, key='1')

    if choice == 'Home':
        st.text("🎶 Welcome to the Spotify Song Recommender! 🎶")
        st.write("Simply navigate to the 'Songs' section and enter the name of your favorite song to discover new music!")
        
    elif choice == "Songs":
        st.write("🎶 Find songs similar to your favorites! 🎶")
        st.title("Choose the song")
        song_name = st.text_input("Enter the song name")  
        st.write("The song chosen is:", song_name)

    

        if song_name:
            try:
                st.write("Searching for similar songs...")
            # Get song ID using the Spotify API
                song_id = bring_song(song_name)

            # Classify the song based on its audio features
                pred_cluster = classify_song(song_id)

            # Recommend similar songs from the playlist
                recommended_songs = song_recommender(pred_cluster)
            
            

            # Display the recommended songs
                st.write("Recommended Songs:")
                #st.write(recommended_songs['names'])
                #st.write(display)

            # Display the recommended songs with embedded players in a single column
                for index, row in recommended_songs.iterrows():
                    track_id = row['id']
                    st.markdown(f"""
                    <div style="margin: 10px; display: flex; flex-direction: column; align-items: center;">
                        <iframe src="https://open.spotify.com/embed/track/{track_id}"
                                width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
                        <p style="text-align: center;">{row['names']}</p>
                    </div>
                    """, unsafe_allow_html=True)
 

            # Display the recommended songs with a play button for each
                #st.write("Recommended Songs:")
                #for idx, (song_name, track_id) in enumerate(zip(recommended_songs['names'], recommended_songs['ids'])):
                    #st.write(f"{idx + 1}. {song_name}")
                    
            # Create a button to play the song when clicked
                #if st.button(f"Play {song_name}", key=f"play_{idx}"):
                #play_song(track_id)  # Call play_song function with the track ID
            
        
            except Exception as e:
                st.error(f"Error: {e}")
                st.write("Make sure the song name is valid and try again.")

if __name__ == '__main__':
    main()
