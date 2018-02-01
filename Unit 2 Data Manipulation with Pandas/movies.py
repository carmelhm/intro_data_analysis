import pandas as pd

# Read data files
titles_max = pd.read_csv('titles.csv')
actors_max = pd.read_csv('actors.csv')
actors_titles_max = pd.read_csv('actors_titles.csv')

# Select only columns that matters
titles_tmp = titles_max[['id', 'title', 'original_title', 'type', 'imdb_rating', 'tmdb_rating', 'mc_user_score', 'release_date', 'country_release_date',
                         'year', 'plot', 'genre', 'tagline', 'poster', 'runtime', 'budget', 'revenue', 'views', 'season_number', 'tmdb_id', 'language', 'country']]

actors_tmp = actors_max[['id', 'name', 'bio', 'sex', 'full_bio_link',
                         'birth_date', 'birth_place', 'image', 'views', 'tmdb_id']]

actors_titles = actors_titles_max[[
    'actor_id', 'title_id', 'char_name', 'known_for']]

# Rename columns to prepare the data merging
titles = titles_tmp.rename(columns={
    'id': 'title_id',
    'country_release_date': 'local_release_date',
})

people = actors_tmp.rename(columns={
    'id': 'person_id',
})

people_titles = actors_titles.rename(columns={
    'actor_id': 'person_id',
})


def is_crew(x): return True if (x == 'Director' or x == 'Writer') else False


people_titles['is_crew'] = people_titles['char_name'].apply(is_crew)


print people_titles.char_name.value_counts()
print people_titles.is_crew.value_counts()
