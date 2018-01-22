
index ={'a':[], 'b':[], 'c':[], 'd':[], 'e':[],
        'f':[], 'g':[], 'h':[], 'i':[], 'j':[],
        'k':[], 'l':[], 'm':[], 'n':[], 'o':[],
        'p':[], 'q':[], 'r':[], 's':[], 't':[],
        'u':[], 'v':[], 'x':[], 'w':[], 'y':[],
        'z':[], 'ó':[]}


def make_index(product_tree):
    for element in product_tree:
        text = element[1].text
        if text is not None:
            start_with = text[0].lower()
            if start_with == ' ':
                start_with = text[1].lower()
            try:
                index[start_with].append(text.lower())
            except KeyError:
                print(start_with)
    return index