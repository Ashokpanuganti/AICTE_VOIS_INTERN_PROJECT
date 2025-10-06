
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set a style for better visualization
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# --- 1. Setup & Data Preparation ---

# Assuming your dataset is named 'netflix_titles.csv'
# Replace 'your_dataset_path.csv' with the actual path or filename.
try:
    df = pd.read_csv('netflix_titles.csv')
except FileNotFoundError:
    print("Error: Dataset file not found. Please ensure 'netflix_titles.csv' is in the correct directory.")
    # Create a dummy DataFrame structure for the code to run without error, if the actual data is missing.
    data = {
        'show_id': range(1, 12),
        'type': ['Movie', 'TV Show', 'Movie', 'Movie', 'TV Show', 'Movie', 'Movie', 'TV Show', 'Movie', 'TV Show', 'Movie'],
        'title': ['Title ' + str(i) for i in range(1, 12)],
        'director': ['Director ' + str(i) for i in range(1, 12)],
        'cast': ['Cast ' + str(i) for i in range(1, 12)],
        'country': ['United States', 'India', 'United States', 'Canada', 'United States', 'India', 'United States', 'UK', 'United States', 'India', 'Canada'],
        'date_added': ['2021-09-25', '2021-09-24', '2020-01-01', '2019-05-15', '2018-07-20', '2017-11-01', '2021-01-10', '2020-05-05', '2019-12-12', '2018-03-30', '2017-06-06'],
        'release_year': [2021, 2020, 2019, 2018, 2017, 2016, 2020, 2019, 2018, 2017, 2016],
        'rating': ['TV-MA', 'TV-14', 'R', 'PG-13', 'TV-G', 'PG', 'TV-MA', 'TV-14', 'R', 'TV-G', 'PG-13'],
        'duration': ['90 min', '1 Season', '120 min', '95 min', '2 Seasons', '100 min', '110 min', '3 Seasons', '105 min', '1 Season', '92 min'],
        'listed_in': ['Dramas, International Movies', 'Crime TV, International TV Shows', 'Comedies', 'Dramas, International Movies', 'Kids\' TV', 'Comedies', 'Dramas, Thrillers', 'British TV Shows, Dramas', 'Action & Adventure', 'Documentaries', 'Sci-Fi, Thrillers']
    }
    df = pd.DataFrame(data)
    print("Using a dummy DataFrame for demonstration.")


# Data Cleaning & Feature Engineering
# Convert 'date_added' to datetime and extract 'year_added'
df.dropna(subset=['date_added'], inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year

# Fill missing 'country' values with 'Unknown' for analysis
df['country'].fillna('Unknown', inplace=True)

# --- 2. Exploratory Data Analysis (EDA) ---

# Check the ratio of Movies vs. TV Shows
content_ratio = df['type'].value_counts()
print("\n--- Content Type Distribution ---")
print(content_ratio)

# --- 3. Visualization & Analysis for Objectives ---

# Objective 1: Analyze the distribution of Movies vs. TV Shows over the years.
df_type_year = df.groupby(['year_added', 'type']).size().reset_index(name='count')
df_type_year_filtered = df_type_year[df_type_year['year_added'] >= 2015] # Focus on recent trend

plt.figure(figsize=(14, 7))
sns.lineplot(data=df_type_year_filtered, x='year_added', y='count', hue='type', marker='o', palette='coolwarm')
plt.title('Content Added to Netflix Over Time (Movies vs. TV Shows)', fontsize=16)
plt.xlabel('Year Added', fontsize=12)
plt.ylabel('Number of Titles Added', fontsize=12)
plt.legend(title='Content Type')
plt.xticks(df_type_year_filtered['year_added'].unique().astype(int))
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

print("\n--- Content Distribution Trend Analysis ---")
print("This line plot shows the yearly growth in content added, comparing Movies and TV Shows. Look for changes in their relative growth rates to understand the evolving content strategy.")
print("-" * 50)

# Objective 2: Identify the most common genres and how their popularity has changed.
# The 'listed_in' column contains comma-separated genres, which needs to be unnested.
def get_all_genres(df):
    all_genres = df['listed_in'].str.split(', ', expand=True).stack()
    return all_genres.value_counts().reset_index(name='count').rename(columns={'index': 'genre'})

genre_counts = get_all_genres(df)

# Top 10 most common genres overall
plt.figure(figsize=(14, 7))
sns.barplot(data=genre_counts.head(10), x='count', y='genre', palette='viridis')
plt.title('Top 10 Most Common Genres on Netflix', fontsize=16)
plt.xlabel('Total Count', fontsize=12)
plt.ylabel('Genre', fontsize=12)
plt.tight_layout()
plt.show()

# Analyze Top Genres by Type (for more nuanced trend)
df_movies = df[df['type'] == 'Movie']
df_tv = df[df['type'] == 'TV Show']

top_movie_genres = get_all_genres(df_movies).head(5)
top_tv_genres = get_all_genres(df_tv).head(5)

print("\n--- Top 5 Movie Genres ---")
print(top_movie_genres)
print("\n--- Top 5 TV Show Genres ---")
print(top_tv_genres)
print("-" * 50)

# Objective 3: Compare country-wise contributions to Netflix’s catalog.
# The 'country' column can also contain multiple comma-separated values.
def get_all_countries(df):
    all_countries = df['country'].str.split(', ', expand=True).stack()
    return all_countries.value_counts().reset_index(name='count').rename(columns={'index': 'country'})

country_counts = get_all_countries(df)

# Top 10 country contributions (excluding 'Unknown' for clarity)
top_countries = country_counts[country_counts['country'] != 'Unknown'].head(10)

plt.figure(figsize=(14, 7))
sns.barplot(data=top_countries, x='count', y='country', palette='magma')
plt.title('Top 10 Countries Contributing Content to Netflix', fontsize=16)
plt.xlabel('Total Content Count', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.tight_layout()
plt.show()

print("\n--- Country Contribution Analysis ---")
print("This bar plot shows which countries are the primary content contributors. This highlights global representation and potential focus markets.")
print("-" * 50)

# --- Expected Outcomes: Strategic Recommendations (Based on analysis outputs) ---
print("\n--- Expected Outcomes & Strategic Recommendations Placeholder ---")
print("1. **Content Strategy Evolution**: Observe the line plot (Movies vs. TV Shows). If TV Shows' count approaches or surpasses Movies, it indicates a pivot towards more series/original programming.")
print("2. **Top-Performing Genres**: The bar plots highlight dominance of genres like 'International Movies', 'Dramas', and 'Comedies'. Recommendation: Strategic investment should be made here, but also explore underrepresented genres for niche markets.")
print("3. **Global Content Focus**: The country analysis confirms key markets (e.g., US, India, UK). Recommendation: Invest in original or acquired content from the next tier of contributing countries (e.g., in Europe, Asia, Latin America) to boost global market penetration.")
print("-" * 50)