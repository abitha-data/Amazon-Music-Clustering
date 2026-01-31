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

### 4. Dataset Description

The dataset contains audio features extracted from music tracks, representing various musical properties such as rhythm, energy, and mood. Each row corresponds to a song, and numerical features are used for clustering.

### 5. Feature Selection

The following features are used for clustering:

Danceability

Energy

Loudness

Speechiness

Acousticness

Instrumentalness

Liveness

Valence

Tempo

Duration (ms)

These features effectively capture the musical characteristics required for grouping similar tracks.

### 6. Data Preprocessing

Removed irrelevant and non-numeric columns

Checked and handled missing values

Scaled features using StandardScaler to ensure equal contribution during clustering

### 7. Clustering Methodology

Applied K-Means clustering as the primary algorithm

Determined the optimal number of clusters using the Elbow Method

Evaluated cluster quality using the Silhouette Score

### 8. Cluster Evaluation

The clustering results were evaluated using:

Silhouette Score

Davies–Bouldin Index

Inertia (for K-Means)

These metrics helped assess cluster compactness and separation.

### 9. Cluster Interpretation

      Cluster	                    Description
         
         0	                      Chill and acoustic tracks
         
         1	                      High-energy and party tracks
         
         2	                      Rap, spoken-word, or live tracks

### 10. Visualization

PCA-based 2D cluster visualization

Feature-wise box plots

Cluster-wise comparison charts

These visualizations aid in understanding the characteristics of each cluster.

### 11. Streamlit Dashboard

An interactive Streamlit dashboard was developed with the following features:

Dataset overview

Cluster evaluation metrics

PCA visualization

Feature analysis

Mood-based cluster recommendation

New song cluster prediction

### 12. Deployment

The application can be deployed using Streamlit Cloud for public access and demonstration.

### 13. Learning Outcomes

Practical understanding of unsupervised learning

Hands-on experience with clustering algorithms

Ability to evaluate and interpret clustering results

Experience in building and deploying ML dashboards

### 14. Conclusion

This project demonstrates how unsupervised learning techniques can be effectively used to analyze and organize large-scale music data, supporting recommendation systems and data-driven decision making.
