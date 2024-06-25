def dictionary(input_files):

    with open(input_files) as fpins:
        allstring = fpins.read()
        wordslist = []

    for words in allstring.split():  
        wordslist.append(words)
        #print(words)
        
    word_count = {}
    for word in wordslist:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        
    for i,n in word_count.items():

        print(i,n)        
    
    
    return word_count



if __name__ == '__main__':
        dictionary("/home/mako/PE/rosalind_ini6(1).txt") 
        
