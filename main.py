import random
import string
from Words import words


def get_valid_word(words):
    word = random.choice(words)  # random chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangmany():
    while not 'a' or 'b':

        hangman = input(
            'Select the type of hangman you will love to play: A for (hangman letters) and B for (hangman word): ').upper()
        if hangman == 'A':
            def hangman_letters():
                word = get_valid_word(words)
                word_letters = set(word)  # letters in the word
                alphabet = set(string.ascii_uppercase)
                used_letters = set()  # what the user has guessed

                lives = 6

                # getting user input
                while len(word_letters) > 0 and lives > 0:
                    # letters used
                    # ' '.join(['a'
                    print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

                    # what current word is (ie W - R D)
                    word_list = [letter if letter in used_letters else '_' for letter in word]
                    print('Current word: ', ' '.join(word_list))

                    user_letter = input('Guess a letter: ').upper()
                    if user_letter in alphabet - used_letters:
                        used_letters.add(user_letter)
                        if user_letter in word_letters:
                            word_letters.remove(user_letter)

                        else:
                            lives -= 1  # takes away a life if wrong
                            print('Letter is not in word.')

                    elif user_letter in used_letters:
                        print('You have already used that character. Please try again.')

                    else:
                        print('Invalid character. Please try again.')

                # gets here when len(word_letters
                if lives == 0:
                    print('Sorry! you died. The word was', word)
                else:
                    print('You guessed the word', word, '!!')

            hangman_letters()



        # another d

        elif hangman == 'B':
            def hangman_word():
                word = get_valid_word(words)
                word_letters = set(word)  # letters in the word
                alphabet = set(string.ascii_uppercase)
                guessed_word = ' '  # what the user has guessed
                used_words = set()

                lives = 6
                print('The following letters make up the word: ', word_letters)

                # getting user input
                while guessed_word != word and lives > 0:
                    # letters used
                    # ' '.join(['a'
                    print('You have', lives, 'lives left and the word is made up of', len(word), 'letters')
                    # what current word is (ie W - R D)
                    first_letter = word[0]
                    print(f'The word start with letter "{first_letter}"')

                    guessed_word = input('Guess a word: ').upper()

                    if len(guessed_word) == len(word):
                        used_words.add(guessed_word)
                        lives -= 1  # takes away a life if wrong
                        if guessed_word != word:
                            print('You have used the following words:', set(guessed_word),
                                  'wrongly and the words you produced are:', guessed_word)

                    elif len(guessed_word) > len(word):
                        print('The letters in the word is too much. Please try again!')

                    elif len(guessed_word) < len(word):
                        print('The letters in the word is not enough. Please try again!')

                    else:
                        print('You guessed the wrong word. Please try again.')

                # gets here when len(word_letters
                if lives == 0:
                    print('Sorry! you died. The word was', word)

                else:
                    print('You guessed the word', word, '!!')

            hangman_word()

    else:
        print('please select the option A or B')


hangmany()
