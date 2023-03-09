import random

def predict(m):
    random_number = random.randint(1,m)
    predict = 0
    while predict != random_number:
        predict = int(input(f'Guess a number between 1 and {m}:'))
        if predict < random_number:
            print("Sorry, guess again. Too low.")
        elif predict > random_number:
          print("Sorry, guess again. Too high.")

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

predict(10)