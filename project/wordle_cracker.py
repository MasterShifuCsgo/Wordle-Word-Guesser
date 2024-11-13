
# User defined Variables
WORDLE_ANSWER_FILE_DIRECTORY = 'C:\Users\50704267035\python\Wordle\text_files\wordle-answers-alphabetical.txt'


#using a class as a datastructure that holds the data for the word
class Word:

    def __init__(self, WordleWord, colors=None):
        self.word = WordleWord
        # check if the word is a string if not ask the user to enter a string
        while type(self.word) != str:
            print("Word should be a string. Please enter a valid word.")
            self.word = input("Enter a word: ")
        
        #check if the user specified a color for each of the words letters
        #if not asks the user for the colors
        if(colors is None):
            self.colors = self.get_word_colors(self.word)
    
    # function that starts asking the user for the colors of each letter. ot put is a dictionary where the keys are the letters, and the values are colors.
    def get_word_colors(self, word):
        colors = {}
        for i in range(len(word)):
            color = input(f"Enter the color of letter {word[i]}: ")
            while color not in ['yellow', 'gray', 'green']:
                print("Invalid color. Please enter yellow, gray or green.")
                color = input(f"Enter the color of letter {word[i]}: ")
            colors[word[i]] = color
        return colors

#function that finds matching words format he wordle answer file. the directory is an argument, struct wi

def search_word_in_file(directory, word):
    #this function opens the file in the specified directory which is a .txt file. each word is seperated by a CLRF



    
    with open(directory, 'r') as file:
        # read the file line by line
        for line in file:
            '''
            split the line into words
            takes a word from the answer file. checks the color of the word.
            if the color is green
             checks if the 
            if the color is yellow
            it checks if the letter is in the word at the same index
            if the color is gray
            add the index to a list of blacklisted indecies where the search algorithim dosent bother to look.            
            '''

            # split the line into words
            words = line.split()

            

                




    # if no matching word is found, return an empty list
    return []





# function that uses the above functions to get word colors and search for the words in the file.
def resolve_word(word):
    # defining datastructure that helps with hangling data of the word.
    word_data = Word(word)
    
    # get word colors
    word_data.get_word_colors(word)
    
    # search for the word in the file
    # first agrument is the directory argument that specifies the location of the wordle answer file. its a constant variable
    # second argument is the word that we are searching for.
    # the function will return the matching words as a list of strings
    
    matching_words = search_word_in_file(WORDLE_ANSWER_FILE_DIRECTORY, word_data)
    
    # print out the matching words and their colors
    print("Matching Words: ")


    #print out the word data
    print("Word: ", word.word)
    print("Colors: ", word.colors)











     







