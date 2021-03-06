"""This file produces a list of possible words and panagrams for a given letter combination from the New York Times Spelling Bee game"""
import os


#input here
center_letter = "b"
satellite_letters = ["o", "t", "d", "n", "e", "m"]


#constants
WORD_FILE_PATH = os.path.join(os.path.dirname(__file__), "english_words.txt")
MINIMUM_WORD_LENGTH = 4
MAXIMUM_WORD_LENGTH = 19


def main(center_letter: str, satellite_letters: list[str]) -> tuple[list[str], list[str]]:
    """Given the center letter and satellite letters for the New York Times Spelling Bee Game, attempts to find all possible words and panagrams
    
    Returns:
        possible_words: a list of possible answers to the game
        possible_panagrams: a list of possible answers to the game that use all 7 letters"""
    #final outputs
    possible_answers = []
    possible_panagrams = []

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    acceptable_letters = [center_letter] + satellite_letters
    unacceptable_letters = [letter for letter in alphabet if letter not in acceptable_letters]

    def is_valid_word(word: str) -> bool:
        """Returns True if a word is a valid guess and False otherwise"""
        #no punctuation
        if "." in word or "-" in word or "'" in word or "/" in word:
            return False
        
        #no numbers
        for number in range(10):
            if str(number) in word:
                return False

        #need center letter
        if center_letter not in word:
            return False
        
        #can't be too short or too long
        if len(word) < MINIMUM_WORD_LENGTH or len(word) > MAXIMUM_WORD_LENGTH:
            return False
        
        #no duplicates
        #TODO is this needed?
        if word in possible_answers:
            return False

        #can only be made of acceptable letters
        for letter in unacceptable_letters:
            if letter in word:
                return False
        
        return True
    
    #go through the word list and append valid words to answer list
    with open(WORD_FILE_PATH, "r") as word_file:
        word_list = [word.lower()[:-1] for word in word_file] #.lower()[:-1] ensures no line breaks or uppercase letters in strings

    #append valid words to answer list
    for word in word_list:
        if is_valid_word(word):
            possible_answers.append(word)

    #search for panagrams in possible answer list
    for word in possible_answers:
        if all([letter in word for letter in acceptable_letters]):
            possible_panagrams.append(word)
    
    return possible_answers, possible_panagrams


if __name__ == "__main__":
    possible_answers, possible_panagrams = main(center_letter, satellite_letters)
    print(f"The possible words are: {possible_answers}")
    print(f"The possible panagrams are: {possible_panagrams}")