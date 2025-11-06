import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

'''for index, item in enumerate(data):
   print(f"{index} : {item['title']}")'''

'''year = int(input("What year"))
for index, item in enumerate(data):
   if item["year"] > year:
      print(f"{index} : {item['title']}")'''


'''before = int(input("Before what year"))  
after = int(input("After what year?"))
for index, item in enumerate(data):
    if item["year"] > after and item["year"] < before:
        print(f"{index} : {item['title']}")'''

'''year = int(input("What year?"))
for index, item in enumerate(data):
    if item["year"] == year:
        print(f"{index} : {item['title']}")'''


'''name = input("Whats the name of the movie?")
for index, item in enumerate(data):
    if item["title"] == name:
        print(f"{index} : {item['title']}")'''

'''genres = input("What Genre?")
for index, item in enumerate(data):
    if item["genres"] == [genres]:
        print(f"{index} : {item['title']}")'''
         