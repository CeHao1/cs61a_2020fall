def add_chars(w1,w2):
    if w1=='':
        return w2
    elif w1[0]==w2[0]:
        return add_chars(w1[1:],w2[1:])
    else:
        print(w2[0])
        return w2[0]+add_chars(w1,w2[1:])