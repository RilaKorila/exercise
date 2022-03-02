#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int count_letter(string text);

int compute_score(string word);

int main(void)
{
    string text1 = get_string("Text: ");

    // Score both words
    int info[3] = count_letter(text1);

    int letter = info[0];
    int word = info[1];
    int sentence = info[2];

    float L = (float) letter * 100.0 / (float) word;
    float S = (float) sentence * 100.0 / (float) word;

    float index = 0.0588 * L - 0.296 * S - 15.8;
    print(index);
}

int compute_score(string word)
{
    // Compute and return score for string
    int score = 0;
    for (int i=0; word[i] != '\0'; i++){

        int num = tolower(word[i])-97;
        if ((num >= 0) && (num <= 25)){
            score += POINTS[num];
        }
    }

    return score;
}

bool is_character(char c){
    int n = tolower(word[i])-97;
    return ((n>=0) && (n<=25)) 
}

int count_letter(string text){
    int n = str_len(text);
    int letter = 0;
    int word = 0;
    int sentence = 0;

    for (int i=0; i<n; i++){
        if (text[i]==' '){
            letter++;
        }

        if (text[i]=='.'){
            sentence++;
            // 次の文の先頭までインクリメント
            while (!(is_character(text[i]))){
                i++;
            }
        }

        if is_character(text[i]){
            text++;
        }  
    }
    int info[3] = {letter, word, sentence};

    return info;
}