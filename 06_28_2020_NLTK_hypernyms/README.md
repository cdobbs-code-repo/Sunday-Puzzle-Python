This Sunday Puzzle involved finding a 5-letter word for an animal which, upon removing the middle letter, resulted in two opposites.

I utilized the NLTK (Natural Language ToolKit) library to solve this word problem. I mainly just needed to use NLTK's "hypernym" function. Hypernyms are umbrella terms, so-to-speak. For example, "color" is a hypernym of "orange." Therefore, by identifying whether "animal" was a hypernym of a given word, I was able to sift out animals from the English word list I iterated through.

I also copy pasted some of my initial results into a words_already_used.txt file. By doing this, I was 1. able to avoid rechecking words I already tried by filtering out any words in the text file. In addition, this text file functioned as a repository of the words I had already looked at, so I could go back and check them again if necessary.

