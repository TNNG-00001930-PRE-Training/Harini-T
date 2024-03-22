import random
def Guess_number():
  random_number=random.randint(1,100)
  nearest_random_no=int(str(random_number)[0])
  #print(random_number)
  chances=5
  print("Number of Chances you have to guess is ",chances)
  while(chances>=1):
    guess_number=int(input())
    nearest_no=int(str(guess_number)[0])
    if guess_number==random_number:
      print("Congratulations You Won the game")
      break
      chances-=1
    elif nearest_no==nearest_random_no:
      print("You are closer to the number")
      if guess_number<random_number:
        print("Your number is little Low")
        print("Try again you are left with ",chances-1,"chances")
        chances-=1
      if guess_number>random_number:
        print("Your number is little High")
        print("Try again you are left with ",chances-1,"chances")
        chances-=1
    else:
      if guess_number<random_number:
        print("Your number is Low")
        print("Try again you are left with ",chances-1,"chances")
        chances-=1
      if guess_number>random_number:
        print("Your number is High")
        print("Try again you are left with ",chances-1,"chances")
        chances-=1
  else:
    print("Better luck next time!!!!!\t The number is ",random_number)
    main_program()

  
def main_program():
  choice=input("Enter 'Y or y' to play:")
  if choice=='Y' or choice=='y':
    Guess_number()
  else:
    print("Ok You are Done with the game.......")

main_program()