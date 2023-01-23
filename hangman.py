from random import choice
from time import sleep
from nltk.corpus import words

WORDS = None

def openFile(category):
    global WORDS

    with open (f'./{category}WordsList.txt') as filename:
        wordBank = filename.read() 
    WORDS = wordBank.split(',')

difficulty = input('\n' * 100 + 'pick a difficulty level:    SHORT  MEDIUM  LONG  IMPOSSIBLE\n').lower()

if difficulty == 'short':
    WORDS = words.words('en-basic')

elif difficulty == 'medium':
    openFile('medium')

elif difficulty == 'long':
    openFile('long')

elif difficulty == 'impossible':
    from nltk.corpus import words
    WORDS = words.words()

elif difficulty == 'flash':
    openFile('flash')

elif difficulty == 'animals':
    openFile('animals')

else:
    print('that is not an option. choosing LONG')
    openFile('long')
    sleep(1)

GRAPHICS = [
    '   ┍━━━━━┓ \n   │     ┃ \n         ┃ \n         ┃ \n         ┃ \n         ┃ \n         ┃ \n         ┃ \n ━━━━━━━━┻━━━━━━━      ',
    '   ┍━━━━━┓ \n   │     ┃ \n   ◯     ┃ \n         ┃ \n         ┃ \n         ┃ \n         ┃ \n         ┃ \n ━━━━━━━━┻━━━━━━━      ',
    '   ┍━━━━━┓ \n   │     ┃ \n   ◯     ┃ \n   │     ┃ \n   │     ┃ \n         ┃ \n         ┃ \n         ┃ \n ━━━━━━━━┻━━━━━━━      ',
    '   ┍━━━━━┓ \n   │     ┃ \n   ◯     ┃ \n   │     ┃ \n   │     ┃ \n  ╱      ┃ \n         ┃ \n         ┃ \n ━━━━━━━━┻━━━━━━━      ',
    '   ┍━━━━━┓ \n   │     ┃ \n   ◯     ┃ \n   │     ┃ \n   │     ┃ \n  ╱ ╲    ┃ \n         ┃ \n         ┃ \n ━━━━━━━━┻━━━━━━━      ',
    '   ┍━━━━━┓ \n   │     ┃ \n   ◯     ┃ \n ╭─┤     ┃ \n   │     ┃ \n  ╱ ╲    ┃ \n         ┃ \n         ┃ \n ━━━━━━━━┻━━━━━━━      ',
    '   ┍━━━━━┓ \n   │     ┃ \n   ◯     ┃ \n ╭─┤─╮   ┃ \n   │     ┃ \n  ╱ ╲    ┃ \n         ┃ \n         ┃ \n ━━━━━━━━┻━━━━━━━      '
]

class hangman:
    
    def __init__(self):
        self.word = choice(WORDS).upper()
        self.progress = list('_' * len(self.word))
        self.running = True
        self.wrongGuesses = []
        self.correctGuesses = []

    def fixWord(self):
        for index in [n for n, l in enumerate(list(self.word)) if l == ' ' or l == '.' or l == '-']:
            self.progress[index] = self.word[index]
            self.correctGuesses.append(index)

    def displayProgress(self):
        print('\n'*100 + GRAPHICS[len(self.wrongGuesses)] + ' '.join(self.progress) + '\n \n \n' + '  '.join(self.wrongGuesses) + '\n \n')

    def getGuess(self):
        userInput = input("guess a letter or phrase:  ")
        if userInput != '' and not userInput.isnumeric():
            userInput.replace(' ', '')
            return userInput.upper()

    def isUserInputLegit(self, userInput):
        return userInput != None and not(userInput in self.wrongGuesses or userInput in self.correctGuesses)

    def isGuessInWord(self, guess):
        return guess in self.word

    def revealGuess(self, guess):
        # the list that index is iterating through = list of indexes of locations of guess
        for index in [n for n, l in enumerate(self.word) if self.word[n : n+len(guess)] == guess]:
            
            # go to each index and make sure each letter in the phrase is not already guessed
            for smallIndex in range(index, index+len(guess)):
                guessIndex = smallIndex - index
                if self.progress[smallIndex] != guess[guessIndex]:
                    self.progress[smallIndex] = guess[guessIndex]
                    self.correctGuesses.append(guess[guessIndex])

    def ifWon(self):
        if len(self.correctGuesses) == len(self.word):
            self.displayProgress()
            print("YOU WON")
            self.running = False

    def wrongGuess(self, guess):
        if len(self.wrongGuesses) < 5:
            self.wrongGuesses.append(guess)
        else:
            self.wrongGuesses.append(guess)
            self.running = False
            self.displayProgress()
            print(f'you ran out of guesses. the word was {self.word}')

    def isWordCorrect(self, guessedWord):
        return guessedWord == self.word

    def outOfGuesses(self):
        if len(self.wrongGuesses) >= 5:
            pass

    def play(self):
        self.fixWord()

        while self.running:
            self.displayProgress()
            userInput = self.getGuess()

            # guessed letter or phrase in word
            if self.isUserInputLegit(userInput) and self.isGuessInWord(userInput):
                self.revealGuess(userInput)
                self.ifWon()
            
            # guess is not correct
            elif self.isUserInputLegit(userInput):
                self.wrongGuess(userInput)

hangman = hangman()
hangman.play()
