import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

for index, item in enumerate(data):
   '''print(f"{index} : {item['title']}")'''


   year = input("What year?")
   if year < item['year']:
      print(f"{index} : {item['title']}")