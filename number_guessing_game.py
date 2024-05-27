import random

top_of_range = input ("type a number:")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type in a  number larger than 0 next time')
        quit()
else:
    print('please type a number next time')
    quit()



random_number =random.randint(0, top_of_range)
#print(random_number)
guesses = 0
max_guesses = 4

while guesses< max_guesses:
    guesses += 1
    user_guess =input ("make a guess:")

    if user_guess.isdigit():
        user_guess =int(user_guess)
    else:
        print("please type a number next time")
        continue

    if user_guess == random_number:
     print("you got it!")
     break
    elif user_guess > random_number:
           print("You were above the number")
    else:
           print("You were below the number")
   
    

#print("You got it in" , guesses, "guesses")

#if guesses == max_guesses:
   # print("you ran out of guesses! the number was" , random_number)

     







    


