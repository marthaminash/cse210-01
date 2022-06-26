import string
import random

class Game:
    def __init__(self):
        self._wordArray = WordArray()
        self.is_playing = True
        self._guess = Guess()

        self._parachute = Parachute()
        self.guessesCount = 0
        self.guessedLetters = []

    def start_game(self):
        self._parachute.create_text("Welcome! Let's start the game!")

        while self.is_playing:
            self._get_input()
            self._create_update()
            self._create_output()

    def _get_input(self):
        self.word_space = self._wordArray.get_wordLength()
        self.word_selected = self._wordArray.get_wordSelected()
        self.new_letter = self._parachute.read_text("Guess the letter [a-z]: ")


    def _create_output(self):
        continuePlaying = self._parachute.create_parachute(
            self.word_selected,
            self.guessedLetters,
            self.word_space,
            self.guess,
            self.guessesCount,
        )
        if continuePlaying == False:
            self.is_playing = False
        else:
            self.is_playing = True

    def _create_update(self):
        self.guess = self._guess.find_letter(self.word_selected, self.new_letter)


        if self.guess == False:
            self.guessesCount += 1
        else:
            if self.guessesCount == 0:
                self.guessesCount = 0
                self.guessedLetters.append(self.new_letter)
            else:
                self.guessesCount += -1
                self.guessedLetters.append(self.new_letter)

class Parachute:

    #The class draws the parachute in the console and transforms compared to the count of guesses and letter that is being chosen

    def __init__(self):
        self.hideWord = []

    def create_underline(self, wordLength, list):
        for i in range(wordLength):
            print("_", end=" "),
        print(" \n")

    def read_text(self, prompt):
        return input(prompt)

    def read_number(self, prompt):
        return float(input(prompt))

    def create_text(self, text):
        print(text)

    def create_parachute(self, guessWord, letter, wordLength, guess, count_guesses):
        #For Loop
        i = 0
        j = 0

        for _ in guessWord:
            if guessWord[i] in letter:
                print(guessWord[i], end=" "),
                a = guessWord.count(guessWord[i])
                if a > 1:
                    j += 1
                else:
                    j += 1
            else:
                print("_", end=" "),
            i += 1
        print(" \n")

        if j == len(guessWord):
            print("  ___  ")
            print(" /___\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            print("Congratulations! You won!")
            exit()

        if count_guesses == 0:
            print("  ___  ")
            print(" /___\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif count_guesses == 1:
            print("    _  ")
            print(" /___\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif count_guesses == 2:
            print(" /___\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif count_guesses == 3:
            print("   __\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif count_guesses == 4:
            print(" \   / ")
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif count_guesses == 5:
            print("     / ")
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif count_guesses == 6:
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif count_guesses == 7:
            print("    /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif count_guesses == 8:
            print("   x   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            print("Oops, the game is over")
            cont = False

        return cont


class WordArray:
    #Array of the words
    def __init__(self):
        self._array = ["Entry","Elite","Close","Extra","Apple","Drive","Close","Dance","Learn","Shelf","Sheet","Shift","Dream","Dress","Smoke","Steam","Store","Thing","Truth","Truck","Topic","Trully","Water","Whole","Whose","Worth","Youth","Young","Which","Where","Urban","Until","Upper","Upset","Spare","South","Stone","Stake","Guide","Stick","Skill","Since","Roman","Pilot","Ocean","Newly","Music","Mixed","Media","Lying","Legal","Model","North","Night","Lucky","Logic","Month","Links","Metal","Mayor","Limit","March","Rugby","Paper","Prior","Noise","Novel","Needs","Leave","Press","Sport","Stock"]
        self._wordSelected = random.choice(self._array)
        self._wordLength = len(self._wordSelected)
        self._wordDisplayed = []

    def get_wordSelected(self):
        self._wordSelected = self._wordSelected.lower()
        return self._wordSelected

    def get_wordLength(self):
        return self._wordLength

    def get_wordDisplayed(self):
        self._wordDisplayed = list(self._wordSelected)
        index = 0
        for _ in self._wordDisplayed:
            self._wordDisplayed[index] = "_"
            index += 1
        return self._wordDisplayed

class Guess:
    #Counts how many matches are guessed
    def __init__(self):
        pass

    def find_letter(self, guessWord, letter):
        letterCount = guessWord.count(letter)

        if letterCount == 0:
            guess = False
        else:
            guess = True

        return guess

def main():
    game = Game()
    game.start_game()

main()