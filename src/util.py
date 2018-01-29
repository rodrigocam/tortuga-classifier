

index ={'a':[], 'b':[], 'c':[], 'd':[], 'e':[],
        'f':[], 'g':[], 'h':[], 'i':[], 'j':[],
        'k':[], 'l':[], 'm':[], 'n':[], 'o':[],
        'p':[], 'q':[], 'r':[], 's':[], 't':[],
        'u':[], 'v':[], 'x':[], 'w':[], 'y':[],
        'z':[], 'á':[], 'é':[], 'í':[], 'ó':[],
        'ú':[], '0':[], '1':[], '2':[], '3':[],
        '4':[], '5':[], '6':[], '7':[], '8':[],
        '9':[]}

"""
    This function creates an index to reduce the complexity of
    comparison betweem words in two big lists.
    If we have a word that starts with "a" we don't need to look
    all others words that not starts with this letter because is
    unlikely that this two words are very similar.
"""
def create_index(word_list):
    for element in word_list:
        text = element[1].text
        if text is not None:
            start_with = text[0].lower()
            if start_with == ' ':
                start_with = text[1].lower()
            try:
                index[start_with].append(text.lower())
            except KeyError:
                print("Unexpected start character %s" % start_with)
    return index