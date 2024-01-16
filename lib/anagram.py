# your code goes here!

# You will write a program that, given a word and a list of possible anagramsLinks to an external site., selects the correct one(s).
# Your class, Anagram should take a word on initialization; instances should respond to a match() instance method that takes a list of possible anagrams. It should return all matches in a list. If no matches exist, it should return an empty list.
# In other words, given: 'listen' and ['enlists', 'google', 'inlets', 'banana'] the program should return ['inlets'].
class Anagram:
    def __init__(self, word):
        # Initialization method that takes a word and sorts its letters alphabetically
        self.letters_in_word = sorted([letter for letter in word])

    def match(self, word_list):
        # Method to find anagrams in the given word list
        match_word_list = []  # Initialize an empty list to store matching words

        # Loop through each word in the provided word list
        for word in word_list:
            # Check if the sorted letters of the current word match the sorted letters of the initialized word
            if sorted([letter for letter in word]) == self.letters_in_word:
                # If there is a match, append the word to the list of matching words
                match_word_list.append(word)

        # Return the list of matching words
        return match_word_list
