def del_none_alpha_start(text, word):
    if not text[0].isalpha() and text[0] != word[0]:
        text = text[1:]
        text = del_none_alpha_start(text, word)
    return text

def del_none_alpha_end(text, word):
    if not text[-1].isalpha() and text[-1] != word[-1]:
        text = text[:-1]
        text = del_none_alpha_end(text, word)
    return text

def match_word(wrd, word, text):
    counter = 0
    if word in wrd:
            tmp_wrd = ""
            equals = True
            if wrd == word:
                counter += 1   
                    
            elif len(wrd) > len(word):  
                
                for letter in wrd:
                    if letter.isalpha() or letter == "'":
                        tmp_wrd += letter
                    
                    elif letter == "." or letter == "-":
                        tmp_wrd += letter if letter in word else " "
                        
                    else:
                        if letter not in word or letter == " ":
                            tmp_wrd += ' '
            
            
            tmp_wrd = tmp_wrd.strip()  
            if len(tmp_wrd.split(' ')) > len(word.split(" ")):
                for w in tmp_wrd.split(' '):
                    if w == word:
                        counter += 1
            else:
                tmp_wrd_striped = tmp_wrd.strip()
                counter += 1 if tmp_wrd_striped == word else 0
                    
    else:
        counter += 0
        
    return counter
    

def count_occurrences_in_text(word, text):
    """
    Return the number of occurrences of the passed word (case insensitive) in text
    """

    # TODO: your code goes here, but it's OK to add new functions or import modules if needed
    # This does not pass the unittests:
    
    text = str.lower(text)
    word = str.lower(word)
    text = del_none_alpha_start(text, word) if not text[0].isalpha() else text
    text = del_none_alpha_end(text, word) if not text[-1].isalpha() else text
    text_tmp = ""
    for letter in text:
        if letter == "\n" or letter == "\r":
            text_tmp += " "
        elif letter == ":":
            text_tmp += f"{letter} "
        else:
            text_tmp += letter
    
    if "  " in text_tmp:
        text = text_tmp.replace("  ", " ")
    else:
        text = text_tmp
        
    del(text_tmp)
    

    # text = text.split(" ")
    word_size = len(word.split(" "))
    counter = 0
    i= 0 
    tmp_text = []

    # Split the text in groups of n words matching the word passed
    if word_size > 1:
        text = text.split(" ")
        gap = len(word.split(" "))-1
        for i in range (0, len(text)):
            if i < len(text):
                j = i
                wrd = ''
                while j <= i+gap:
                    wrd += f'{text[j]} '
                    j += 1
                    if j >= len(text): break
                wrd = wrd.strip()
                if word in wrd: counter += match_word(wrd, word, text)
                
        
          
    else:
        text = text.split(" ")
        for wrd in text:
            counter += match_word(wrd, word, text)

              
    return counter
