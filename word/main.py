from words import word, word_medium, word_hard
import random

#Custom Error


class IntegerError(Exception):
  "Raised if a.numeric == True and a is not in the list ['e', 'm', 'h', 't', 's', 'q', 'k', 'z']"
  pass


# Decorator scorefx
def scorefx(fx):
  def mscorefx():
    print("Please Calculate your score:")
    fx()
    print("Please go through your socres.\n")

  return mscorefx()


# # Example list of digits representing a number
# digits_list = [1, 2, 3, 4, 5]

# # Convert the list of digits to an integer
# number = int(''.join(map(str, digits_list)))

# print(number)  # Output: 12345

# def set1(fx):
#   def mset1fx():
#     print("SETTINGS:")
#     fx()
#   return mset1fx()

# def score():
#   with open('score.txt', 'a') as f:
#     f.write()


def score():
  y = open('score.txt', 'r')
  reading_text = y.read()
  print(reading_text)
  y.close()


z_used = []


def history():
  o = open('g.txt', 'r')
  m = o.read()
  print(m)
  o.close()


class Settings:

  def __init__(self, chancesforhard, chancesforeasy, chancesformedium):
    try:
      self.chancesforhard = int(
        input(
          "Please enter the settings:\nEnter the chances that should be given when the user is playing on hard mode: "
        ))
      with open('g.txt', 'a') as f:
        f.write(
          f"\nChances for hard mode (default): 5\nChances for hard mode (set by the user): {self.chancesforhard}"
        )
      # empty_1.append(chancesforhard)
      # def num1():
      #   number1 = empty_1 + chancesforhard
      self.chancesformedium = int(
        input(
          "Enter the chances that should be given when the user is playing on the moderate mode: "
        ))
      with open('g.txt', 'a') as f:
        f.write(
          f"\nChances for medium mode (default): 10\nChances for medium mode (set by the user): {self.chancesformedium}"
        )
      # empty_2.append(chancesforhard)
      # def num2():
      #   number2 = empty_2 + chancesformedium
      self.chancesforeasy = int(
        input(
          "Enter the chances that should be given when the user is playing on easy mode: "
        ))
      with open('g.txt', 'a') as f:
        f.write(
          f"\nChances for easy mode (default): 15\nChances for easy mode (set by the user): {self.chancesforeasy}"
        )
      # empty_3.append(chancesforhard)
      # def num3():
      #   number3 = empty_3 + chancesforeasy
    except ValueError:
      print("Invalid Input. Quitting the program...")
      quit()

  def settingspage(self):
    print("\nSo, the settings set by you are: ")
    chancesforhard = f"Chances given when the user is playing on hard mode: {self.chancesforhard}"
    chancesformedium = f"Chances given when the user is playing on medium mode: {self.chancesformedium}"
    chancesforeasy = f"Chances given when the user is playing on easy mode: {self.chancesforeasy}"

    print(chancesforhard)
    print(chancesformedium)
    print(chancesforeasy)


settings_instance = Settings(5, 10, 15)

empty_1 = [settings_instance.chancesforhard]
empty_2 = [settings_instance.chancesformedium]
empty_3 = [settings_instance.chancesforeasy]

# Convert the chances to integers
number1 = int(''.join(map(str, empty_1)))
number2 = int(''.join(map(str, empty_2)))
number3 = int(''.join(map(str, empty_3)))

chances = 1
while chances > 0:
  chances -= 1

  try:
    a = input("""Enter which mode would you like to play? 
          Easy - (e)
          Medium - (m)
          Hard - (h)
          Logs: (t)
          Scores: (s)
          If you want to quit mid game: (q) # Can be used only during the game
          If you want to know the word directly: (k) # Can be used only during the game 
          Remember: -4 is given if the user has used 'k' 
      
          Probability of the user getting the correct answer in their first try:
          Easy Mode - 37.5%
          Medium - 15.625%
          Hard - 7.57%
          """)

    if a.isnumeric() or a not in ["e", "m", "h", "t", "s", "q", "k"]:
      raise IntegerError(
        "You had to choose from the given list. Error code: 305, IntErr")
  except IntegerError:
    a = f"<class interr> Error: You had to choose from the given list. '{a.capitalize()}' , wasn't found in the list (e, m, h, t, s, 'z', 'q', 'k'). Invalid User Input."
    print(a)
    with open('g.txt', 'a') as g:
      g.write(
        f"\nInvalid Input by the user, exception raised: {a}. Program unexpectedly crashed..."
      )
      quit()

  with open('g.txt', 'a') as g:
    g.write("\nGame Starts...\nLoading Functions...")
    g.write(f"\nMethod chosen: {a}")
    g.write("\nLoading Databases...")


def game3():
  ask = input("Enter a word: ")
  with open('g.txt', 'a') as g:
    g.write(f"\nWord Guessed: {ask}")
  correct_word = random.choice(word_hard)
  chances = number1
  # Example list of digits representing a number
  guessed_words = []
  h_used = []

  while chances >= 1:
    if ask.lower() == correct_word:
      congo1 = "Congratulationsssssssss".upper()
      print(congo1.center(50))
      print("You got it in your first try!")
      print('You get 10/10 for thatt')
      with open('score.text', 'a') as f:
        f.write(
          "\n+10"
        )  # 37.5% = probability of getting a +10/getting this block of code executed

      break
    elif ask.lower() != correct_word:
      chances -= 1
      ask1 = input(
        f"""Try again! If you want a hint, type in 'h' 🤭 Enter a word, you have {chances} chances remaining or type in 'q' 
if you wanna quit. If you want to know the word then type in 'k': """
      ) if chances > 0 else quit()

      with open('g.txt', 'a') as g:
        g.write(f"\nWord: {ask1}")

      with open('g.txt', 'a') as g:
        g.write(f'\nWord Guessed: {ask1}')

      if not ask1.isalpha():
        print(
          """Your response cannot contain numbers, special characters and you also can't leave your response
blank, if you wanna quit, type in 'q', Quitting...""")
        quit()

      if ask1 in guessed_words:
        print("You have already guessed that word.")

      guessed_words.append(ask1)
      # with open('guessed.txt', 'a') as f:
      #     f.write(guessed_words)

      if ask1.lower() == 'q':
        print("Quitting.\n.\n.\n.")
        quit()

      if chances == 0:
        print(f"You ran out of chances! Sorry. The word was, '{correct_word}'")

      if ask1.lower() == 'h':
        print(
          f"""SHHHHHH, hINty: The word starts with a '{correct_word[0]}' , ends with a '{correct_word[-1]}'
and is {len(correct_word)} letters long.""")
        h_used.append('h')

      if ask1.lower() == correct_word:
        if 'h' in h_used:
          print("As you used a hint, your score was 4/10")
          print("but yes you did get the correct answer")
          with open('score.txt', 'a') as f:
            f.write("+4")
          with open('g.txt', 'a') as g:
            g.write(f'\nappend +4, score.txt')
          try:
            ask2 = input("Do you wanna play again? y/n: ")
          except Exception as e:
            print(f'Error: {e} , Invalid Input!')
          try:
            if ask2 == 'y' and ask2.isalpha():
              print("here we go again!")
              game()
            elif ask2 == 'n' and ask2.isalpha():
              print("Quitting\n.\n.")
              quit()
            else:
              raise ValueError
          except ValueError:
            print(
              "Error: ValueError, you entered a number. The game will continue from where you stopped"
            )

        elif 'h' not in h_used:
          congrats = "VERYYY GOOD!!!"
          print(congrats.center(50))
          print("As you did not use any of the hints, your score was 10/10")
          ask2 = input("Do you wanna play again? y/n: ")
          if ask2 == 'y':
            # print("here we go again!")
            ask3 = int(
              input(
                "Okay cool, do you want to increase the difficulty of the game? You have 3 options:\nEasy - (1)\nMedium - (2)\nHard - (3)"
              ))
            print("The one you just played was the easy version.")
            if ask3 == 1:
              game()
            elif ask3 == 2:
              game2()
            elif ask3 == 3:
              game3()
          elif ask2 == 'n':
            print("Quitting\n.\n.")
            quit()
      if chances == 0 and ask1 != correct_word:
        print('Sorry you got it all wrong!')
        quit()

      if ask1.lower() == 'k':
        print(f"The correct word was {correct_word}")
        with open('g.txt', 'a') as g:
          g.write(
            f"User couldnt guess the word, 'k' was used. Quitting The program\nUnloading Databases...\nCorrect Word = {correct_word}"
          )
        quit()


def game2():
  ask = input("Enter a word: ")
  correct_word = random.choice(word_medium)
  chances = number2
  guessed_words = []
  h_used = []

  while chances >= 1:
    if ask.lower() == correct_word:
      congo1 = "Congratulationsssssssss".upper()
      print(congo1.center(50))
      print("You got it in your first try!")
      print('You get 10/10 for thatt')
      with open('score.txt', 'a') as f:
        f.write("\n+10")
      break
    elif ask.lower() != correct_word:
      chances -= 1
      ask1 = input(
        f"""Try again! If you want a hint, type in 'h' 🤭 Enter a word, you have {chances} chances remaining or type in 'q' 
if you wanna quit or type 'k' if you just want the word: """
      ) if chances > 0 else quit()

      with open('g.txt', 'a') as g:
        g.write(f"\nWord: {ask1}")

      if not ask1.isalpha():
        print(
          """Your response cannot contain numbers, special characters and you also can't leave your response
blank, if you wanna quit, type in 'q', Quitting...""")
        quit()

      if ask1 in guessed_words:
        print("You have already guessed that word.")

      guessed_words.append(ask1)

      if ask1.lower() == 'q':
        print("Quitting.\n.\n.\n.")
        quit()

      if chances == 0:
        print(f"You ran out of chances! Sorry. The word was, '{correct_word}'")

      if ask1.lower() == 'h':
        print(
          f"""SHHHHHH, hINty: The word starts with a '{correct_word[0]}' , ends with a '{correct_word[-1]}'
and is {len(correct_word)} letters long.""")
        h_used.append('h')

      if ask1.lower() == correct_word:
        if 'h' in h_used:
          print("As you used a hint, your score was 4/10")
          print("but yes you did get the correct answer")
          with open('score.txt', 'a') as f:
            f.write("+4")
          with open('g.txt', 'a') as g:
            g.write(f'\nappend +4, score.txt')
          try:
            ask2 = input("Do you wanna play again? y/n: ")
          except Exception as e:
            print(f'Error: {e} , Invalid Input!')
          try:
            if ask2 == 'y' and ask2.isalpha():
              print("here we go again!")
              game()
            elif ask2 == 'n' and ask2.isalpha():
              print("Quitting\n.\n.")
              quit()
            else:
              raise ValueError
          except ValueError:
            print(
              "Error: ValueError, you entered a number. The game will continue from where you stopped"
            )

        elif 'h' not in h_used:
          congrats = "VERYYY GOOD!!!"
          print(congrats.center(50))
          print("As you did not use any of the hints, your score was 10/10")
          ask2 = input("Do you wanna play again? y/n: ")
          if ask2 == 'y':
            # print("here we go again!")
            ask3 = int(
              input(
                "Okay cool, do you want to increase the difficulty of the game? You have 3 options:\nEasy - (1)\nMedium - (2)\nHard - (3)"
              ))
            print("The one you just played was the easy version.")
            if ask3 == 1:
              game()
            elif ask3 == 2:
              game2()
            elif ask3 == 3:
              game3()
          elif ask2 == 'n':
            print("Quitting\n.\n.")
            quit()
      if chances == 0 and ask1 != correct_word:
        print('Sorry you got it all wrong!')
        quit()

      if ask1.lower() == 'k':
        print(f"The correct word was {correct_word}")
        with open('g.txt', 'a') as g:
          g.write(
            f"User couldnt guess the word, 'k' was used. Quitting The program\nUnloading Databases...\nCorrect Word = {correct_word}"
          )
        quit()


def game():
  ask = input("Enter a word: ")
  correct_word = random.choice(word)
  chances = number3
  guessed_words = []
  h_used = []

  while chances >= 1:
    if ask.lower() == correct_word:
      congo1 = "Congratulationsssssssss".upper()
      print(congo1.center(50))
      print("You got it in your first try!")
      print('You get 10/10 for thatt')
      with open('score.txt', 'a') as f:
        f.write("\n+10")
      break
    elif ask.lower() != correct_word:
      chances -= 1
      ask1 = input(
        f"""Try again! If you want a hint, type in 'h' 🤭 Enter a word, you have {chances} chances remaining or type in 'q' if you wanna quit or type 'k' if you just want the word: """
      ) if chances > 0 else quit()
      with open('g.txt', 'a') as g:
        g.write(f"\nWord: {ask1}")

      if not ask1.isalpha():
        print(
          """Your response cannot contain numbers, special characters and you also can't leave your response blank, if you wanna quit, type in 'q', Quitting..."""
        )
        quit()

      if ask1 in guessed_words:
        print("You have already guessed that word.")

      guessed_words.append(ask1)

      if ask1.lower() == 'q':
        print("Your current scores: ")
        score()
        print("Quitting.\n.\n.\n.")
        quit()

      if chances == 0:
        print(f"You ran out of chances! Sorry. The word was, '{correct_word}'")

      if ask1.lower() == 'h':
        print(
          f"""SHHHHHH, hINty: The word starts with a '{correct_word[0]}' , ends with a '{correct_word[-1]}'
and is {len(correct_word)} letters long.""")
        h_used.append('h')

      if ask1.lower() == correct_word:
        if 'h' in h_used:
          print("As you used a hint, your score was 4/10")
          print("but yes you did get the correct answer")
          with open('score.txt', 'a') as f:
            f.write("\n+4")
          with open('g.txt', 'a') as g:
            g.write(f'\nappend +4, score.txt')
          try:
            ask2 = input("Do you wanna play again? y/n: ")
          except Exception as e:
            print(f'Error: {e} , Invalid Input!')
          try:
            if ask2 == 'y' and ask2.isalpha():
              print("here we go again!")
              game()
            elif ask2 == 'n' and ask2.isalpha():

              @scorefx
              def score():
                y = open('score.txt', 'r')
                reading_text = y.read()
                print(reading_text)
                y.close()
                print("Quitting\n.\n.")
                quit()
            else:
              raise ValueError("YOU CAN NOT ENTER NUMBERS")
          except ValueError:
            print(
              "Error: ValueError. The game will continue from where you stopped"
            )

        elif 'h' not in h_used:
          congrats = "VERYYY GOOD!!!"
          print(congrats.center(50))
          print("As you did not use any of the hints, your score was 10/10")
          ask2 = input("Do you wanna play again? y/n: ")
          if ask2 == 'y':
            # print("here we go again!")
            ask3 = int(
              input(
                "Okay cool, do you want to increase the difficulty of the game? You have 3 options:\nEasy - (1)\nMedium - (2)\nHard - (3)"
              ))
            print("The one you just played was the easy version.")
            if ask3 == 1:
              game()
            elif ask3 == 2:
              game2()
            elif ask3 == 3:
              game3()
          elif ask2 == 'n':
            print("Quitting\n.\n.")
            quit()
      if chances == 0 and ask1 != correct_word:
        print('Sorry you got it all wrong!')
        quit()

      if ask1.lower() == 'k':
        print(f"The correct word was {correct_word}")
        with open('score.txt', 'a') as j:
          j.write('\n-4')
        with open('g.txt', 'a') as g:
          g.write(
            f"User couldnt guess the word, 'k' was used. Quitting The program\nUnloading Databases...\nCorrect Word = {correct_word}"
          )
        quit()

        # ask2 = input("Do you wanna play again? y/n: ")
        #
        # if ask2 == 'y':
        #     print("here we go again!")
        #     game()
        # elif ask2 == 'n':
        #     if 'h' in h_used:
        #         print('Yeah anyways you would use a hint, no point of you playing.')
        #         print("Quitting\n.\n.")
        #         quit()
        #     elif 'h' not in h_used:
        #         print("Okay no problem")
        #         print("As you did not use any of the hints, your score was 10/10")
        #         quit()

        # quit()


if a == 'e':
  game()
elif a == "m":
  game2()
elif a == "h":
  game3()
elif a == "t":
  history()
# elif a == "s":
# score()
elif a == 'q':
  print("Quitting.....")
  with open('g.txt', 'a') as g:
    g.write("User decided to quit....Quitting")
  quit()
elif a == 'k':
  print(
    "You can not use this function right now...You will be playing on easy mode"
  )
  with open('g.txt', 'a') as g:
    g.write('User used {k}, <not_applicable> , mode = easy.')
  game()
elif a == "s":
  score()
