def random_number():
  
  import random
  
  n = random.randint (1,75)
  guess = int(raw_input("Enter an integer from 1 to 75: "))
  attempts = 1
  
  while guess != n:
    
    if guess > n:
      print "Your guess is too high."
      attempts = attempts + 1
      guess = int(input("Guess:"))
      
    elif guess < n:
      print("Your guess is too low.")
      attempts = attempts + 1
      guess = int(input("Guess:"))
      
  print "You guessed the correct number in " + str(attempts) + " attempts !!!"   

random_number()