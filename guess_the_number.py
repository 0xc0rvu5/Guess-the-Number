import random
from art import logo


#initialize global variables
EASY_COUNT = 10
HARD_COUNT = 5
CONT = True


def difficulty():
  '''Determine game difficulty level.'''
  level = input('Choose a difficulty. Type "easy" or "hard".\n ~ ')
  match level:
    case 'easy':
        return EASY_COUNT
    case 'hard':
        return HARD_COUNT


def check_answer(guess, answer, turn):
  '''Checks answer against guess and reduce turn count. Paramaters taken: guess, answer, turn'''
  if guess > answer:
    print('Too high.')
    return turn - 1
  elif guess < answer:
    print('Too low.')
    return turn - 1
  else:
    print(f'Winner winner chicken dinner! You won with {answer} as your answer!')


def game():
  '''Main game function.'''
  print(logo)
  print('Welcome to the Number Guessing Game!')
  print('I\'m thinking of a number between 1 and 100.')
  #initialize final answer, guess counter and determine game difficulty
  answer = random.randint(1, 100)
  guess = 0
  turn = difficulty()
  
  #if condition is not met continue game
  while guess != answer: 
    print(f'You have {turn} remaining to guess the number. ')
    guess = int(input('Guess a number...\n ~ '))
    turn = check_answer(guess, answer, turn)
    #if 0 turns are left then end game
    if turn == 0:
      print('You ran out of guesses. Game over.')
      return


#initialize game functionality
try:
    game()
except KeyboardInterrupt:
    print('\nSee you later.')