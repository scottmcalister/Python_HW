import os
import string

file_num = 1

#sets file
file_PyPara = 'paragraph_' + str(file_num) +'.txt'
# open and reads file and saves text as paragraph string
paragraph_str = ''
# with open function, open the file that has been put into the object 'txtfile'
with open(file_PyPara, 'r') as txtfile:
    paragraph_txt = txtfile.read()

#sentence count by counting ., ? and !
sen_count = paragraph_txt.count('.') + paragraph_txt.count('?') + paragraph_txt.count('!')

#create a string of upper and lowercase letters
letters = string.ascii_letters + " " 

#loops through paragraph string and deletes all characters 
# that are not letters replacing with nothing
for x in paragraph_txt:
    if x not in letters:
        paragraph_txt = paragraph_txt.replace(x,'')


#reassigns the paragraph string and makes a list of words by splitting at spaces
paragraph_list = paragraph_txt.split()

#counts all of the letters in list paragraph
letter_total = 0
for word in paragraph_list:
    letter_total += len(word)

#counts words by counting the length of paragraph list
word_count = len(paragraph_list)

#calculates average word length by dividing the total # of letters
#by the number of words
avg_word_length = letter_total/word_count

# calculates words per sentence by dividing the number of words by the number of sentences.
words_per_sentence = word_count/sen_count

print('Paragraph Analysis\n-----------------\nApproximate Word Count: ' 
                        + str(word_count)+ '\nApproximate Sentence Count: '+ str(sen_count) + 
                        '\nAverage Letter Count: ' + str(avg_word_length) + 
                        '\nAverage Sentence Length: ' + str(words_per_sentence))

