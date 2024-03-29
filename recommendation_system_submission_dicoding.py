# -*- coding: utf-8 -*-
"""Recommendation System - Submission Dicoding

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_KPK5AberC35FKXX4jzd28c6siE2KsI_

# Movie Recommendation system

## Import Library
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import drive
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import re
# Filter out specific warning by category
warnings.filterwarnings("ignore")
# Your code here that triggers the warning
drive.mount('/content/drive')

"""## Data Understanding

### Data Loading
"""

movies_df = pd.read_csv("/content/drive/MyDrive/portofolio/Movie Recommendation System/Dataset/movies.csv")
ratings_df = pd.read_csv("/content/drive/MyDrive/portofolio/Movie Recommendation System/Dataset/ratings.csv")

movies_df.head()

ratings_df.head()

print('Jumlah data movies: ', len(movies_df.movieId.unique()))
print('Jumlah data ratings: ', len(ratings_df.movieId.unique()))

#get dataset info movies_df
movies_df.info()

#get dataset info ratings_df
ratings_df.info()

#get summary from movies_df
movies_df.describe(include="all")

#get summary from ratings_df
ratings_df.describe(include="all")

"""### Exploratory Data Analysis

**Univariate Analysis**
"""

#plotting rating distribution data
categorical_feats = ['rating']
count_categorical_cols = len(categorical_feats)
num_rows = (count_categorical_cols + 1) // 2  # Calculate the number of rows needed for the grid layout

fig, axes = plt.subplots(num_rows, 2, figsize=(15, 5*num_rows))  # Create a grid layout
axes = axes.flatten()  # Flatten the 2D array of axes to simplify indexing

for index, col in enumerate(categorical_feats):
    count = ratings_df[col].value_counts()
    percent = 100 * ratings_df[col].value_counts(normalize=True).round(2)
    df = pd.DataFrame({'jumlah sampel': count, 'persentase': percent})
    ax = axes[index]
    count.plot(kind='bar', ax=ax, title=col)
    ax.set_ylabel('Count')

# Hide any remaining empty subplots
for ax in axes[count_categorical_cols:]:
    ax.axis('off')

plt.tight_layout()
plt.show()

#separate genres by "|"
movie_id = []
movies = []
genres = []
# Iterate over the rows
for index, row in movies_df.iterrows():
    # Split the string by "|"
    split_result = row["genres"].split("|")
    for i in split_result:
      movie_id.append(row["movieId"])
      movies.append(row["title"])
      genres.append(i)
genres = {
    "movieId":movie_id,
    "title":movies,
    "genre":genres
}

#make df from genres dict
genres_df = pd.DataFrame(genres)
genres_df.head()

#plotting distribution genre
genres_df["genre"].value_counts().plot(kind="bar")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.title("Distribution of Genres")
plt.show()

#separate year from movie title
movie_id = []
movies = []
years=[]
# Iterate over the rows
for index, row in movies_df.iterrows():
  # Use regular expression to find the year in parentheses
  year_match = re.search(r'\((\d{4})\)', row["title"])
  # Extract the year if found
  if year_match:
        year = year_match.group(1)
        years.append(year)
  else:
    continue
  movie_id.append(row["movieId"])
  movies.append(row["title"])
years_df = {
    "movieId":movie_id,
    "title":movies,
    "year":years
}

#make df from years_df
years_df = pd.DataFrame(years_df)
years_df.head()

# plotting distribusion year
years_df["year"].value_counts().head(10).plot(kind="bar")
plt.xlabel("year")
plt.ylabel("Count")
plt.title("Top 10 years with the most movie publications")
plt.show()

"""**Multivariate Analysis**"""

# genre and ratings
# menggabungkan data movies dengan rating
genre_ratings = pd.merge(genres_df, ratings_df, on='movieId', how='inner')

# Print dataframe movies
genre_ratings.head()

# Calculate the top 5 genres by count
top_genres = genre_ratings[genre_ratings["rating"] == 5.0]['genre'].value_counts().nlargest(5).index.tolist()

# Filter the DataFrame to include only the top 5 genres
genre_ratings_top5 = genre_ratings[(genre_ratings['genre'].isin(top_genres)) & (genre_ratings["rating"] == 5.0)]
# Calculate the count of each genre
genre_counts = genre_ratings_top5['genre'].value_counts()

# Sort the genres by count
genre_ratings_top5_sorted = genre_counts.sort_values(ascending=False).reset_index()

# Rename the columns
genre_ratings_top5_sorted.columns = ['genre', 'count']


# Create a bar plot
sns.barplot(x='genre', y='count', data=genre_ratings_top5_sorted)
plt.title('Count of Ratings by Genre (Top 5)')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# Calculate the top 5 genres by count
top_genres = genre_ratings[genre_ratings["rating"] == 0.5]['genre'].value_counts().nlargest(5).index.tolist()

# Filter the DataFrame to include only the top 5 genres
genre_ratings_top5 = genre_ratings[(genre_ratings['genre'].isin(top_genres)) & (genre_ratings["rating"] == 0.5)]
# Calculate the count of each genre
genre_counts = genre_ratings_top5['genre'].value_counts()

# Sort the genres by count
genre_ratings_top5_sorted = genre_counts.sort_values(ascending=False).reset_index()

# Rename the columns
genre_ratings_top5_sorted.columns = ['genre', 'count']


# Create a bar plot
sns.barplot(x='genre', y='count', data=genre_ratings_top5_sorted)
plt.title('Count of Ratings by Genre (Top 5)')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# genre and ratings
# menggabungkan data movies dengan rating
year_ratings = pd.merge(years_df, ratings_df, on='movieId', how='inner')

# Print dataframe movies
year_ratings.head()

# Calculate the top 5 years by count
top_years = year_ratings[year_ratings["rating"] == 5.0]['year'].value_counts().nlargest(5).index.tolist()

# Filter the DataFrame to include only the top 5 years
years_top5 = year_ratings[(year_ratings['year'].isin(top_years)) & (year_ratings["rating"] == 5.0)]
# Calculate the count of each year
year_counts = years_top5['year'].value_counts()

# Sort the years by count
years_top5_sorted = year_counts.sort_values(ascending=False).reset_index()

# Rename the columns
years_top5_sorted.columns = ['year', 'count']


# Create a bar plot
sns.barplot(x='year', y='count', data=years_top5_sorted)
plt.title('Count of Ratings by Year (Top 5)')
plt.xlabel('year')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# Calculate the top 5 years by count
top_years = year_ratings[year_ratings["rating"] == 0.5]['year'].value_counts().nlargest(5).index.tolist()

# Filter the DataFrame to include only the top 5 years
years_top5 = year_ratings[(year_ratings['year'].isin(top_years)) & (year_ratings["rating"] == 0.5)]
# Calculate the count of each year
year_counts = years_top5['year'].value_counts()

# Sort the years by count
years_top5_sorted = year_counts.sort_values(ascending=False).reset_index()

# Rename the columns
years_top5_sorted.columns = ['year', 'count']


# Create a bar plot
sns.barplot(x='year', y='count', data=years_top5_sorted)
plt.title('Count of Ratings by Year (Top 5)')
plt.xlabel('year')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

"""## Data Preparation

### Merge Data
"""

# menggabungkan data movies dengan rating
movies = pd.merge(movies_df, ratings_df, on='movieId', how='inner')

# Print dataframe movies
movies.head()

print('Jumlah seluruh data movies dan rating berdasarkan movie_id: ', len(movies))

"""### Missing Value"""

#menghitung jumlah missing value
movies.isna().sum().plot(kind="bar")
plt.title("Count of missing value")

"""### Change Datatype"""

movies['movieId'] = movies['movieId'].astype('category')
movies['userId'] = movies['userId'].astype('category')

# Membuang data duplikat pada variabel preparation
preparation = movies.drop_duplicates('movieId')
preparation

# Mengonversi data series ‘movieId’ menjadi dalam bentuk list
movieId = preparation['movieId'].tolist()

# Mengonversi data series ‘title’ menjadi dalam bentuk list
movie_title = preparation['title'].tolist()

# Mengonversi data series ‘genre’ menjadi dalam bentuk list
genre = preparation['genres'].tolist()

print(len(movieId))
print(len(movie_title))
print(len(genre))

# Membuat dictionary untuk data ‘movieId’, ‘movie_title’, dan ‘genre’
movie = pd.DataFrame({
    'id': movieId,
    'title': movie_title,
    'genres': genre
})
movie.head()

"""## Modelling

### Modelling Content Based Filtering
"""

data = movie

# Words to exclude from TF-IDF
exclude_words = ['no', 'fi', 'imax']

# Inisialisasi TfidfVectorizer
vec = TfidfVectorizer(stop_words=exclude_words)

# Melakukan perhitungan idf pada data genres
vec.fit(data['genres'])

# Mapping array dari fitur index integer ke fitur nama
vec.get_feature_names_out()

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = vec.fit_transform(data['genres'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan genre
# Baris diisi dengan movie title

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=vec.get_feature_names_out(),
    index=data.title
).info()

"""**Cosine Similiarity**"""

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama movie
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['title'], columns=data['title'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap movie
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

def movie_recommendation(title, similarity_data=cosine_sim_df, items=data[['title', 'genres']], k=5):
    """
    Rekomendasi movie berdasarkan kemiripan dataframe

    Parameter:
    ---
    title : tipe data string (str)
                Judul Film (index kemiripan dataframe)
    similarity_data : tipe data pd.DataFrame (object)
                      Kesamaan dataframe, simetrik, dengan movie sebagai
                      indeks dan kolom
    items : tipe data pd.DataFrame (object)
            Mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan
    k : tipe data integer (int)
        Banyaknya jumlah rekomendasi yang diberikan
    ---


    Pada index ini, kita mengambil k dengan nilai similarity terbesar
    pada index matrix yang diberikan (i).
    """


    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,title].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop title agar nama movie yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(title, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

#mencari data dengan judul sama
data[data.title.eq('Old Boy (2003)')]
actual = data[data.title.eq('Old Boy (2003)')]

# Mendapatkan rekomendasi movie yang mirip dengan Old Boy (2003)
movie_recommendation('Old Boy (2003)')

# Mendapatkan rekomendasi movie yang mirip dengan Old Boy (2003) untuk perhitungan precision
predict = movie_recommendation('Old Boy (2003)')

actual["genres"].values

#formula precision recommendation system
total_relevant = predict[predict["genres"].isin(actual["genres"].values)]["genres"].value_counts().values[0]
total_recommendation = len(predict)
precision = (total_relevant/total_recommendation)*100
print(precision)

"""### Modelling Collaborative Based Filtering"""

data = movies
data.head()

# Mengubah rating menjadi nilai float
data['rating'] = data['rating'].values.astype(np.float32)

# Nilai minimum rating
min_rating = min(data['rating'])

# Nilai maksimal rating
max_rating = max(data['rating'])
# jumlah user
num_users = len(data['userId'].unique())
num_movies = len(data['movieId'].unique())
print('Number of User: {}, Number of movie: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_movies, min_rating, max_rating
))

data.describe()

# dikarenakan title mencapai 193609 namun jumlah movie hanya 9724, encoding dilakukan terhadap title.
# hal tersebut dapat mempengaruhi hasil karena title dijadikan sebagai index

# Mengubah title menjadi list tanpa nilai yang sama
movie_ids = data['title'].unique().tolist()

# Melakukan proses encoding title
movie_to_movie_encoded = {x: i for i, x in enumerate(movie_ids)}

# Melakukan proses encoding angka ke title
movie_encoded_to_movie = {i: x for i, x in enumerate(movie_ids)}

# begitu juga dengan userId karena dimulai dari 1, sedangkan indexing dimulai 0 hal ini dapat menimbulkan error pada saat training model
# maka dari itu, userId akan dilakukan encoding seperti movieId

# Mengubah userId menjadi list tanpa nilai yang sama
user_ids = data['userId'].unique().tolist()

# Melakukan proses encoding userId
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}

# Melakukan proses encoding angka ke userId
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}

print(user_to_user_encoded)
print(movie_to_movie_encoded)

# Mapping movieId ke dataframe movie
data['movieId'] = data['title'].map(movie_to_movie_encoded)
data['userId'] = data['userId'].map(user_to_user_encoded)

# Mengacak dataset
training = data.sample(frac=1, random_state=42)
training.head()

# Membuat variabel x untuk mencocokkan data user dan movie menjadi satu value
x = training[['userId', 'movieId']].values

# Membuat variabel y untuk membuat rating dari hasil
y = training['rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * training.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

class RecommenderNet(tf.keras.Model):
  # Insialisasi fungsi
  def __init__(self, num_users, num_movies, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_movies = num_movies
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.movie_embedding = layers.Embedding( # layer embeddings movie
        num_movies,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.movie_bias = layers.Embedding(num_movies, 1) # layer embedding movie bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    movie_vector = self.movie_embedding(inputs[:, 1]) # memanggil layer embedding 3
    movie_bias = self.movie_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_movie = tf.tensordot(user_vector, movie_vector, 2)

    x = dot_user_movie + user_bias + movie_bias

    return tf.nn.sigmoid(x) # activation sigmoid

model = RecommenderNet(num_users, num_movies, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 1024,
    epochs = 100,
    validation_data = (x_val, y_val)
)

"""## Evaluation

### Recommendation Score
"""

#plotting result of training and validation
plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""### Get Recommendation"""

user_id = movies.userId.sample(1).iloc[0]
movie_visited_by_user = movies[movies.userId == user_id]

movie_not_visited = movies[~movies['movieId'].isin(movie_visited_by_user.movieId.values)]['movieId']
movie_not_visited = list(
    set(movie_not_visited)
)

movie_not_visited = [[x] for x in movie_not_visited]
user_movie_array = np.hstack(
    ([[user_id]] * len(movie_not_visited), movie_not_visited)
)

ratings = model.predict(user_movie_array).flatten()
top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_movie_ids = [
    movie_encoded_to_movie.get(movie_not_visited[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('movie with high ratings from user')
print('----' * 8)

top_movie_user = (
    movie_visited_by_user.sort_values(
        by = 'rating',
        ascending=False
    )
    .head(5)
    .movieId.values
)

data_rows = data[data['movieId'].isin(top_movie_user)]
high_rating = []
for row in data_rows.itertuples():
  if row.title in high_rating:
    continue
  else:
    high_rating.append(row.title)
  print(row.title, ':', row.genres)

print('----' * 8)
print('Top 10 movie recommendation')
print('----' * 8)

recommended_movie = data[data['title'].isin(recommended_movie_ids)]
recommended = []
for row in recommended_movie.itertuples():
  if row.title in recommended:
    continue
  else:
    recommended.append(row.title)
  print(row.title, ':', row.genres)