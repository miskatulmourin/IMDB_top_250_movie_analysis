import pandas as pd
import numpy as np

# Load dataset
file_path= 'D:\imdb_top_250.csv'
df = pd.read_csv(file_path)

# 1️⃣ Which year had the most top-rated movies
most_movies_year = df['year'].value_counts().idxmax()
most_movies_count = df['year'].value_counts().max()
print(f"Year with the most top-rated movies: {most_movies_year} ({most_movies_count} movies)")

# 2️⃣ Average rating of all movies
average_rating = df['rating'].mean()
print(f"Average rating of all movies: {average_rating:.2f}")

# 3️⃣ Most popular genres
# Split multiple genres, clean spaces, and count
genre_series = df['genre'].str.split(',').explode().str.strip()
most_popular_genres = genre_series.value_counts()
print("\nMost Popular Genres:")
print(most_popular_genres.head(10))

# 4️⃣ Top directors by number of movies in Top 20
top20_df = df[df['rank'] <= 20]
top_directors_top20 = top20_df['directors'].value_counts()
print("\nTop Directors by Number of Movies in Top 20:")
print(top_directors_top20)

# 5️⃣ Check for 'votes' column before finding movie with highest votes
if 'votes' in df.columns:
    highest_votes_movie = df.loc[df['votes'].idxmax()]
    print(f"\nMovie with highest votes:\n{highest_votes_movie[['name', 'votes']]}")
else:
    print("\nNo 'votes' column found in this dataset.")

# 6️⃣ Rating distribution
rating_distribution = df['rating'].value_counts().sort_index()
print("\nRating Distribution:")
print(rating_distribution)

# ✅ Summary Output
print("\n----- Summary -----")
print(f"Most movies in a year: {most_movies_year} ({most_movies_count})")
print(f"Average rating: {average_rating:.2f}")
print("Most common genres:")
print(most_popular_genres.head(5))
print("Top directors in Top 20 movies:")
print(top_directors_top20)
print("Rating distribution:")
print(rating_distribution)