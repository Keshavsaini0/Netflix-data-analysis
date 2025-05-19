import pandas as pd
import matplotlib.pyplot as plt


# load the data 
df = pd.read_csv('E:/netflix_titles.csv', encoding='latin1')

print(df.columns)
#clean the data 
df = df.dropna(subset=['type','release_year', 'rating', 'duration'])

type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
plt.title('Number of Movies vs TV shows on Netflix')
plt.xlabel('type')
plt.ylabel('count')
plt.tight_layout()
plt.savefig('movie_vs_tvshows.png')

plt.show()

rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,4))
plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%',startangle=90)
plt.title('percentage of content ratings')
plt.tight_layout()
plt.savefig('contnt_rating.png')
plt.show()

movie_df = df[df['type'] == 'Movie'].copy()

# Drop rows with missing or malformed durations
movie_df = movie_df.dropna(subset=['duration'])

# Remove 'min' and convert to integer safely
movie_df['duration_int'] = movie_df['duration'].str.replace('min', '').str.strip()

# Filter out non-numeric values (in case some durations like "1 Season" sneak in)
movie_df = movie_df[movie_df['duration_int'].str.isnumeric()]

# Convert to int
movie_df['duration_int'] = movie_df['duration_int'].astype(int)


plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins=30,color='blue',edgecolor='black')
plt.title('Distribution of Movie Duration')
plt.xlabel('Duration(minutes)')
plt.ylabel("Number of movies")
plt.tight_layout()
plt.savefig('movie_duration.png')
plt.show() 



release_counts =df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index,release_counts.values,color='red')
plt.title('Relase Year vs Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.savefig('release_year.png')
plt.show()


country_counts=df['country'].value_counts().head(10)
plt.figure(figsize=(10,6))
plt.barh(country_counts.index,country_counts.values,color ='teal')
plt.title('Top 10 country by Number of Shows')
plt.xlabel('Number of Shows')
plt.ylabel('country')
plt.tight_layout()
plt.savefig('Top_10_country.png')
plt.show()

content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)
fig,ax = plt.subplots(1,2,figsize=(12,5))
#first subplots movies
ax[0].plot(content_by_year.index, content_by_year['Movie'],color='ORANGE' )
ax[0].set_title('Movies Release per year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')
#second subplots tv shows
ax[0].plot(content_by_year.index,content_by_year['TV Show'],color= 'purple')
ax[0].set_title('Tv shows release per year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of movies')

fig.suptitle('Comparision of movies and tv shows Release Per year')
plt.tight_layout()
plt.savefig('movie_tvshow_comparision')
plt.show()