# Wordle

## How Its Made
This is a basic version of the popular game Wordle from The New York Times, the only difference being that the words you guess will not have any repeating letters. It reads a text file full of words and randomly selects one that is 5 letters long and has no repeating letters. This word is then converted to a list and compared to the user's input which is also converted to a list. If statements are used to determine if the user's word contains the same letters and if they share the same index. The user's input is then output, and any letter that is the same and has the same index will be green, letters that are the same but share different indexes will be yellow, and letters that are not present in the original word will be white. The user has 6 attempts, a while loop enforces this. If the user does not accurately guess the word the answer is displayed. 

## Lessons Learned
From this project I learned how to utilize Ansi color codes and also got valuable practice working with lists.

## Install
Clone the repository.
Download the text file or any text file, just ensure the file name matches the filePath.

