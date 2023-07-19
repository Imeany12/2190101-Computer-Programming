# load users' watching info
import math
users = dict()
users["Pop"] = {"minion", "spiderman"}
users["Tim"] = {"ju-on", "minion"}
users["Pun"] = {"minion"}
users["Puk"] = {"avenger", "batman", "spiderman"}
users["Tan"] = {"spiderman"}

def calculate_user_scores(query, users):
  # query: a dictionary of watching histories for a specific user
  # users: a dictionary of watching histories for all users
  # Return: a dictionary of all user's scores (round 2 decimal points)
    
  user_scores = {'Pop': 0, 'Tim': 0, 'Pun': 0, 'Puk': 0, 'Tan': 0}
  #fill your code here!
  for movie in sorted(query):
      for name in sorted(users):
          mu = users[name].union(query)
          recm =users[name].union(query)-query

          if movie in users[name]:
              print(len(recm))
              print(len(mu))
              s = math.ceil(len(recm)/len(mu)*100)/100
              user_scores[name]+= s
          
  return user_scores


def recommend_movies(query, users, user_scores):
  # query: a dictionary of watching histories for a specific user
  # users: a dictionary of watching histories for all users
  # user_scores: a dictionary of all user's scores (round 2 decimal points)
  # Return: a list of recommend movies in alphabetically order

  recommend = list()
  
  # fill your code here!
  allm = {}
  k=set()
  for x in users:
      allm = users[x].union(allm)
  if query ==set():
      return "No recommendation"
  for x in query:
      if x not in allm :
          return "No recommendation"
  score = [user_scores[e] for e in user_scores]
  lmovie = [users[e] for e in user_scores if user_scores[e] == max(score)]
  for x in lmovie:
      k = k.union(x)
  recommend = k-query
  recommend = list(recommend)
  return sorted(recommend)


def main():
  n = int(input())
  query = set()
  for i in range(n):
    query.add(input().lower())

  user_scores = calculate_user_scores(query, users)
  print(user_scores)
  recommend = recommend_movies(query, users, user_scores)
  print(recommend)

main()

