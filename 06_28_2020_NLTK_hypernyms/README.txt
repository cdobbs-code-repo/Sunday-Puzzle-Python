# sunday_puzzle_06-28-2020

This Sunday Puzzle involved finding a 5-letter word for an animal which, upon removing the middle letter, resulted in two opposites.

To solve this problem, I utilized NLTK (Natural Language ToolKit). I specifically used NLTK so that I could find words for animals by using their functions to find a word's "hypernyms." Hypernyms are umbrella terms, so-to-speak. For example, "color" is a hypernym of "orange." By identifying whether "animal" was a hypernym of a given word, I was able to filter my results reasonably well.

I also copy pasted some of my initial results into a words_already_used.txt file. By doing this, I was 1. able to avoid rechecking words I had already tried by filtering out any words which could be found in the aforementioned text file and 2. I could maintain a repository of the words I had looked at in order to go back and check them again if necessary.

