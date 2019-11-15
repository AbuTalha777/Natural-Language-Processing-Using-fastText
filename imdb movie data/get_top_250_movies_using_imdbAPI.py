import imdb
# create an instance of the IMDb class
ia = imdb.IMDb()

movie=ia.get_top250_movies() #function to get a list of top 250 movies from imdb website

data=""
for m in movie :
    full = ia.get_movie(m.movieID) #getting data of each movie from the list
    for genre in full['genres'] : #using genres as the tags
        data=data+("__label__" + genre.replace(" ","-") + " ") #adding prefix "__label__" and replacing space with hyphen
    data=data + (m['title'] + "\n") #adding movie title as text
print(data)

text_file = open("movie_test.txt", "w") #saving the data into a txt file
text_file.write(data)
text_file.close()
