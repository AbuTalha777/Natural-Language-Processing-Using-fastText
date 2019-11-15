import pandas as pd
import numpy as np
imdbmovies=pd.read_csv("~/Downloads/movie_metadata.csv") #read the movie data downloaded from kaggle
data=""
#print(imdbmovies.loc[1,])
for index, row in imdbmovies.iterrows():
    genre=row['genres'].split('|') #using the genres as the tags
    for g in genre:
        data = data + ("__label__" + g.replace(" ","-") + " ") #add "__label__" before each genre
    data = data + (row['movie_title'] + "\n") #use movie title as text
print(data)
text_file = open("movie_train.txt", "w") #write the data into a file
text_file.write(data)
text_file.close()