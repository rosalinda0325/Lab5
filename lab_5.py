
"""
This program will translate a sentence captures by the user input.
First we read in the text file textese.txt then a list is created 
of strings from each lines in text file.
We will then create a dictionary from the text file
After the text file has been read we will close it

A function to tanslate will be defined which will split user 
input into array of strings. 

A loop will be created using user input for our array, it will find
key words and return back the value in the dictionary

print out the translated sentence to user
"""

"""

main()
 dictionary =translate():
 translate()


translate(sentence, dictionary)
 word = each word in sentence
 print translate()



create_dictionay()
 read in textese.txt
 create list = each line from file
 close file
 create a dictionary off lsit
 return


main()

"""

def main():
    sentence = "enjoy the excellent band tonight"
    dictionary = create_dictionary("textese.txt")
    translate(sentence, dictionary)

def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()

    print("words", words)
    translation = {}
    for word in words:
        [k, v] = word.split(",")
        translation[k] = v
    return translation

    return { 
        "tonight" : "2nite", "late": "l8"
    }


def translate(sentence, dictionary):
    print("From translate", sentence)
    words = sentence.split() 
    for word in words:
        print(dictionary.get(word, word), " ", end="")

main()





