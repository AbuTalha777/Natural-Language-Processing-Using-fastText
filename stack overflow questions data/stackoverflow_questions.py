from stackapi import StackAPI #using stackapi
si=StackAPI('stackoverflow') #getting questions from stackoverflow website
si.max_pages=150 #getting questions from 150 pages
si.page_size=100 #getting 100 observations from each page
q=si.fetch('questions',min=10) #using fetch function to get the data
#print(q)
data=""
c=0
for quest in q['items']: #tags are stored under items column
    #print(quest['title'])
    c=c+1
    tags = []
    if 'tags' in quest:
        tags = quest['tags']
    for label in tags:
        data = data + ("__label__" + label.replace(" ","-") + " ") #adding the prefix to each tag
    data = data + (quest['title'] + "\n") #questions are stored in the title column
    #print(tags)
print(c)
print(data)
text_file = open("questions.txt", "w") #writing the data to a file
text_file.write(data)
text_file.close()