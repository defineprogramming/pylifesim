# Life Simulator

# import random module for random number generation
import random

# define initial variables
age = 0
money = 0
hunger = 0
thirst = 0
happiness = 0

# define list of possible job titles and salary ranges
jobs = [
  ["Janitor", [500, 700]],
  ["Teacher", [1200, 1500]],
  ["Police Officer", [1500, 2000]],
  ["Software Engineer", [4000, 6000]],
  ["Doctor", [6000, 8000]]
]

# define a function to handle aging
def age_up():
  global age
  age += 1
  print("You are now " + str(age) + " years old.")

# define a function to handle going to work
def work():
  global money
  print("You go to work.")
  job_title, salary_range = random.choice(jobs)
  salary = random.randint(salary_range[0], salary_range[1])
  money += salary
  print("You work as a " + job_title + " and make $" + str(salary) + ".")

# define a function to handle eating food
def eat():
  global hunger, money
  print("You eat some food.")
  hunger -= random.randint(10, 30)
  money -= random.randint(5, 15)
  if hunger < 0:
    hunger = 0

# define a function to handle drinking water
def drink():
  global thirst, money
  print("You drink some water.")
  thirst -= random.randint(10, 30)
  money -= random.randint(1, 5)
  if thirst < 0:
    thirst = 0

# define a function to handle having fun
def have_fun():
  global happiness
  print("You have some fun.")
  happiness += random.randint(10, 30)

# define a function to handle going to the doctor
def go_to_doctor():
  global money, health
  print("You go to the doctor.")
  money -= random.randint(100, 300)
  health += random.randint(10, 30)

# define a function to handle going to the gym
def go_to_gym():
  global happiness, health
  print("You go to the gym.")
  happiness -= random.randint(5, 10)
  health += random.randint(5, 10)

# define a function to handle going to the bar
def go_to_bar():
  global happiness, money
  print("You go to the bar.")
  happiness += random.randint(10, 20)
  money -= random.randint(20, 50)

# define a function to handle user input
def handle_input():
  global hunger, thirst, happiness
  user_input = input("Enter a command (1 to eat, 2 to drink, 3 to work, etc.) or Q to age up: ")
  if user_input == "Q":
    age_up()
  elif user_input == "1":
    eat()
  elif user_input == "2":
    drink()
  elif user_input == "3:
    work()
