#include <iostream>
#include <string>
#include <sstream>
#include <vector>

//const std::string DIRECTORY = "C:\\Users\\kaspar\\repo 1\\Wordle-Word-Guesser\\text_files";
constexpr const char* DIRECTORY = "C:\\Users\\kaspar\\repo 1\\Wordle-Word-Guesser\\text_files";


struct Word {
    std::string letters;
    std::vector<std::string> colors; 

    Word(std::string letters_p, 
    std::vector<std::string> colors_p)
    : letters(letters_p), colors(colors_p){} 
};

Word initalize_word_letters_to_colors(const std::string& word_p){
    std::cout << "\033[1;32word does not have corresponding colors set. Please enter corresponding colors (yellow, green, gray).\033[0m\n";
    std::stringstream output;
    std::vector<std::string> colors;
    std::string color;

    for(int i = 0; i < word_p.size(); i++){
        output << "Enter letter \"" << word_p[i] << "\" color: ";
        std::cin >> color; // if the function encounters errors nothing is done.
        colors.push_back(color);
    }
    Word word(word_p, colors); // initalizes the word as a datastructure.
    return word;
}

//returns a vector of all the possible words derived from the text file given by directory.
std::vector<std::string> find_words(const char *dir, std::vector<Word> &words){
    /*
     in summary, it looks at the file using the directory. directory points to the area where the file resides.
     it opens the file, and starts evaluating if the word fits the corresponding word in the words vector.

     if the word in the directory and the word in the Word vector fit together, then it passes and gets added to the result vector
    */

    std::vector<std::string> result{};

    //loops through the Word vector to loop through each word the user has inserted.
    for(int i = 0; i < words.size(); i++){
        //test begins here to check if the word fits the criteria.

    }
}

int main(){

    system("clear");


    // ask user for inserted wordle word
    
    std::vector<Word> Words;
    while(true){
    std::string word;
    std::cout << "Enter you wordle word: ";
    std::cin >> word;

    Word data = initalize_word_letters_to_colors(word);
    Words.push_back(data);
    std::vector<std::string> found_words = find_words(DIRECTORY, Words);
    }


    return 0;
}
