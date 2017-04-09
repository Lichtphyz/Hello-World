pyg = 'ay'  # set up the piglatin suffix

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha(): # check that the word has letters and no other symbols
    word = original.lower() #convert to lower case
    first = word[0]         #grab the first letter
    new_word = word + first + pyg   #add the parts together
    new_word = new_word[1:len(new_word)]   #remove the first letter of the word
    print new_word  #print the finished result
else:
    print 'empty'  #print 'empty' if there was no word, or an invalid entry
