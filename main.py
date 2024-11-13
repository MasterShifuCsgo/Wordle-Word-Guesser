# main.py

# Import the Word class from wordle_cracker.py
from wordle_cracker import Word

# Function to resolve word by printing word data and colors
def resolve_word(word):
    # Print out the word data
    print("Word:", word.word)
    print("Colors:", word.colors)

# Main execution
def main():
    # Prompt the user for a word and create a Word object
    word_input = input("Enter a word for Wordle: ")
    
    # Create a Word object using the input word
    word = Word(word_input)  # This will invoke the Word class from wordle_cracker.py
    
    # Resolve the word by printing its data and colors
    resolve_word(word)

if __name__ == "__main__":
    main()
