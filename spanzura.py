#spanzuratoarea cu functii inspirat de pe net
import random
word_list = ["rosu", "orange", "galben", "verde", "albastru", "indigo", "violet"]

def get_word(word_list):    # selectare cuvant aleatoriu
    word = random.choice(word_list)
    return word.upper()


def play(word):             # incepe jocul
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Sa jucam Spanzuratoarea")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("ghiceste o litera: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("ai incercat deja litera", guess, "!")
            elif guess not in word:
                print(guess, "nu exista in cuvant :(")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Bravo,", guess, "exista in cuvant!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Ai incercat deja ", guess, "!")
            elif guess != word:
                print(guess, " nu ai ghicit cuvantul :(")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("invalid input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Bravo, ai ghicit cuvantul!")
    else:
        print("Imi pare rau, ai epuizat toate incercarile. Cuvantul era " + word + ". Poate ai noroc data viitoare!")




def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]

def main():
    word = get_word(word_list)
    play(word)
    while input("Joci din nou? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)

if __name__ == "__main__":
    main()