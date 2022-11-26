from art import logo, vs
import random 
from game_data import data
from replit import clear

def game():
  score = 0
  print(logo)
  lost = False
  options = ["spaceholder", random.choice(data)]
  options = print_options(options[1])
  while not lost:
    return_values = compare(options[0], options[1], score)
    score = return_values[1]
    lost = return_values[0]
    if not lost:
      options = print_options(options[1])


# print both persons
def print_options(a):
  char1 = a
  new_list = data
  new_list.remove(char1)
  char2 = random.choice(data)
  new_list.append(char1)
  print(f"Compare A: {char1['name']}, a {char1['description']}, from {char1['country']} ")
  print(vs)
  print (f"Against B: {char2['name']}, a {char2['description']}, from {char2['country']} ")
  return char1, char2


# get input and compare both persons
def compare(adict, bdict, score):
  guess=input("""Who has more followers? Type 'A' or 'B': """)
  a = adict["follower_count"]
  b = bdict["follower_count"]
  if guess == "A" and a > b:
    clear()
    print(logo)
    print(f"Youre right! Current score: {score + 1}")
    return False, score +1
  elif guess == "B" and b > a:
    clear()
    print(logo)
    print(f"Youre right! Current score: {score + 1}")
    return False, score + 1
  else:
    clear()
    print(logo)
    print(f"Sorry, thats wrong. Final score: {score}")
    return True, score



game()
