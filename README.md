# Spotify Song Recommender
## Project Overview
This project is the Spotify Song Recommender application built using Streamlit, Spotipy, and Tableau Public. 
The application allows users to enter a song name and receive a cluster-based song recommendation using audio features retrieved from the Spotify API. 

## Key Features
1) Song Classification: Utilizes K-Means Clustering based on audio features of songs.
2) Spotify Song Recommendations: Provides song recommendations from the same cluster using Spotify’s API.

## Technologies Used
Python: Main programming language for the application.
Streamlit: For building the web application.
Spotipy: A lightweight Python library for accessing the Spotify Web API.
Pandas: For data manipulation and analysis.
Scikit-learn: For implementing the K-Means clustering model.
Tableau Public: For creating and displaying visualizations.

### How to Run the Application
Spotify Credentials: Ensure you have your Spotify credentials stored in a config file.

## Running the Streamlit App: 
Execute the following command in your terminal:
streamlit run main.py
This will launch the app in your default browser.

## Choose from Tabs:
Home: Overview of the application and its functionalities.
Songs: Enter a song name and receive a recommendation from the same cluster.
Songs Tab
Enter a song name in the input field.
The app will retrieve the song’s audio features and classify it into a cluster.
A recommendation from the same cluster will be displayed along with the original song.

## Project Links
Tableau Dashboard: [Gnod Clustering Project Dashboard](https://public.tableau.com/app/profile/nicole.pinto6998/viz/GnodClusteringProject/GnodProject_Dashboard2?publish=yes)

## Conclusion
This application leverages Spotify music data to recommend songs based on shared characteristics, providing an engaging user experience.
