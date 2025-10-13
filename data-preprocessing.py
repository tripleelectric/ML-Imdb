import pandas as pd

df = pd.read_csv("data/raw/TMDB_movie_dataset_v11.csv")


# ------ Create a sample with 100k rows ------

columns = [
    "id",
    "title",
    "vote_average",
    "vote_count",
    "status",
    "release_date",
    "revenue",
    "runtime",
    "adult",
    "budget",
    "imdb_id",
    "original_language",
    "original_title",
    "overview",
    "popularity",
    "tagline",
    "genres",
    "production_companies",
    "production_countries",
    "spoken_languages",
    "keywords",
]
# sample = df.sample(n=100000)
# sample.to_csv("data/processed/100k_subset.csv", columns=columns)


# ------ Remove all rows with missing data ------
# cleaned = df.dropna()
# cleaned.to_csv("data/processed/cleaned_full.csv")
# print(cleaned.count)
# >>> 234432

# ------ Cleaned with anticipated relevant columns ------
relevant_columns = [
    "id",
    "title",
    "vote_average",
    "vote_count",
    "release_date",
    "revenue",
    "runtime",
    "adult",
    "budget",
    "original_language",
    "original_title",
    "overview",
    "popularity",
    "tagline",
    "genres",
    "production_companies",
    "production_countries",
]
cleaned_relevant = df[relevant_columns].dropna()
cleaned_relevant.reset_index(drop=True)
cleaned_relevant.to_csv("data/processed/81k_thin_dropped.csv")
print(cleaned_relevant.shape)
