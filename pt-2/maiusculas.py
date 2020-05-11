def maiusculas(frase):
    pos = 0
    string = ''
    while pos <= len(frase)-1:
        if 64 < ord(frase[pos]) < 91:
            string += frase[pos]
        pos += 1
    return string
