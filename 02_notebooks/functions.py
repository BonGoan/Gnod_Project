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


    
    
def song_recommender (pred_cluster):

    same_cluster_songs= df_playlist_new.loc[df_playlist_new["cluster_knn"]== pred_cluster]
    recommended_song= same_cluster_songs.sample(n=3)
   
    return recommended_song 