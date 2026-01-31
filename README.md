## 🎧 Amazon Music Clustering Dashboard

### Unsupervised Machine Learning Project for Music Analytics

An end-to-end Unsupervised Machine Learning project that groups songs based on their audio characteristics using K-Means clustering, with an interactive Streamlit dashboard for visualization, evaluation, and prediction.

### 1. Project Overview

The Amazon Music Clustering Dashboard is an unsupervised machine learning project that groups songs based on their audio features without using predefined labels. Using K-Means clustering, tracks are organized according to similarities in rhythm, energy, and mood. An interactive Streamlit dashboard is built to visualize clusters, evaluate model performance, and predict the cluster of new songs. This project demonstrates the practical application of clustering techniques in music analytics and recommendation systems.

### 2. Problem Statement

Music platforms host millions of tracks, making manual classification by genre or mood impractical. The objective of this project is to automatically group similar songs using clustering techniques based on audio features such as energy, tempo, and danceability.

### 3. Objectives

Automatically cluster songs based on audio features

Identify patterns and similarities in music data

Evaluate clustering quality using standard metrics

Visualize clusters interactively

Predict the cluster of new songs


### 4.✨ Features

Data Exploration & Preprocessing: Comprehensive EDA, handling missing values, and feature scaling
       
Multiple Clustering Algorithms: K-Means and DBSCAN implementation
       
Optimal Cluster Selection: Elbow method and Silhouette score analysis
       
Dimensionality Reduction: PCA visualization for 2D cluster representation
       
Model Persistence: Trained models saved for production use
       
Interactive Web App: Streamlit-based predictor for real-time cluster prediction
       
Comprehensive Analysis: Cluster profiling and genre inference

### 5.🛠️ Tech Stack

Languages & Libraries:

           Python 3.8+

           Pandas, NumPy - Data manipulation

           Scikit-learn - Machine learning algorithms

           Matplotlib - Data visualization

           Joblib - Model serialization

           Streamlit - Web application framework

Algorithms:

          K-Means Clustering

          DBSCAN (Density-Based Spatial Clustering)

          Principal Component Analysis (PCA)

          StandardScaler for feature normalization


### 6. Dataset Description

The dataset contains audio features extracted from music tracks, representing various musical properties such as rhythm, energy, and mood. Each row corresponds to a song, and numerical features are used for clustering.

### 7. Feature Selection

Selected Features:

             danceability - How suitable a track is for dancing

             energy - Intensity and activity measure

             loudness - Overall loudness in decibels

             speechiness - Presence of spoken words

             acousticness - Confidence measure of acoustic sound

             instrumentalness - Predicts whether a track contains vocals

             liveness - Presence of an audience

             valence - Musical positiveness

             tempo - Beats per minute (BPM)

             duration_ms - Track length in milliseconds

### 8. Data Preprocessing

Removed irrelevant and non-numeric columns

Checked and handled missing values

Scaled features using StandardScaler to ensure equal contribution during clustering

### 9. Clustering Methodology

Applied K-Means clustering as the primary algorithm

Determined the optimal number of clusters using the Elbow Method

Evaluated cluster quality using the Silhouette Score

### 10. Cluster Evaluation

The clustering results were evaluated using:

Silhouette Score

Davies–Bouldin Index

Inertia (for K-Means)

These metrics helped assess cluster compactness and separation.

### 10. Cluster Interpretation

📊 Results

Cluster Distribution (K-Means with k=3)

         Cluster	           Description	                  Key Characteristics
         
         Cluster 0	           Chill Acoustic	               Low energy, high acousticness, calm vibe
         
         Cluster 1	           Party Tracks	                 High danceability, high energy, high tempo, high valence

         Cluster 2	           Rap/Live Recordings	          High danceability, medium energy, high speechiness, high liveness

### 11. Visualization

PCA-based 2D cluster visualization

Feature-wise box plots

Cluster-wise comparison charts

These visualizations aid in understanding the characteristics of each cluster.

### 12. Streamlit Dashboard

An interactive Streamlit dashboard was developed with the following features:

Dataset overview

Cluster evaluation metrics

PCA visualization

Feature analysis

Mood-based cluster recommendation

New song cluster prediction

### 13. Deployment

The application can be deployed using Streamlit Cloud for public access and demonstration.


### How to Run the Project Locally

Step 1: Clone the repository
     
        git clone https://github.com/your-username/Amazon-Music-Clustering.git

        cd Amazon-Music-Clustering

Step 2: Install dependencies

        pip install -r requirements.txt

Step 3: Run the Streamlit application

        streamlit run amazonapp.py


### 14. Conclusion

This project demonstrates how unsupervised learning techniques can be effectively used to analyze and organize large-scale music data, supporting recommendation systems and data-driven decision making.
