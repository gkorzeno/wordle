import random

def getWord(filePath):
    with open(filePath, 'r') as file:
        randomWord = [word.strip() for word in file.readlines() if len(word.strip()) == 5 and len(set(word.strip())) == 5]
        return random.choice(randomWord).strip()

filePath = "wordList.txt"
randomWord = getWord(filePath)

def convertWordToString(string):
    word = []
    word[:0] = string
    return word

word = convertWordToString(randomWord)

def gamePlay(word):
    attempts = 0

    while attempts < 6:
        word1 = input()
        word1 = convertWordToString(word1)

        while len(word1) != 5:
            word1 = input("Please enter a 5 letter word: ")
            if len(word1) == 5:
                break

        for i in range(len(word)):
            if word1[i] == word[i]:
                print("\033[1;32;40m", word1[i], end="")
            elif word1[i] in word:
                print("\u001b[33m", word1[i], end="")
            else:
                print("\u001b[37m", word1[i], end="")

        print("\033[0m")

        if word1 == word:
            print("Congratulations! You guessed the word: " + str.upper(randomWord))
            break

        attempts += 1

    if word1 != word:
        print("You Ran Out Of Attempts \nThe Correct Word Was: " + str.upper(randomWord))

def main():
    print("Wordle 2.0")
    print("In this version there are no repeating letters")
    print("Enter a 5 letter word: ")
    gamePlay(word)

if __name__ == "__main__":
    main()
    