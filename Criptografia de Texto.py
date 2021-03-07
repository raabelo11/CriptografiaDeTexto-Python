def barra():
    print ("--" * 100)

def cripto(frase):
    crip = " "
    barra()
    for letra in frase:
        if letra in "Aa": crip = crip + "!"
        elif letra in "Bb": crip = crip + "@"
        elif letra in "Cc": crip = crip + "#"
        elif letra in "Dd": crip = crip + "$"
        elif letra in "Ee": crip = crip + "%"
        elif letra in "Ff": crip = crip + "&"
        elif letra in "Gg": crip = crip + "*"
        elif letra in "Hh": crip = crip + "("
        elif letra in "Ii": crip = crip + ")"
        elif letra in "Jj": crip = crip + "-"
        elif letra in "Kk": crip = crip + "+"
        elif letra in "Ll": crip = crip + "="
        elif letra in "Mm": crip = crip + "/"
        elif letra in "Nn": crip = crip + "Ὧ"
        elif letra in "Oo": crip = crip + "₽"
        elif letra in "Pp": crip = crip + "∆"
        elif letra in "Qq": crip = crip + "┬"
        elif letra in "Rr": crip = crip + "Ψ"
        elif letra in "Ss": crip = crip + "Ω"
        elif letra in "Tt": crip = crip + "Ϋ"
        elif letra in "Uu": crip = crip + "ϓ"
        elif letra in "Vv": crip = crip + "ϕ"
        elif letra in "Ww": crip = crip + "Ϙ"
        elif letra in "Xx": crip = crip + "Ю"
        elif letra in "Yy": crip = crip + "Ѡ"
        elif letra in "Zz": crip = crip + "ш"
        elif letra in ",": crip = crip + "Ѭ"
        elif letra in ".": crip = crip + "в"
        elif letra in ":": crip = crip + "д"
        elif letra in "Ôô": crip = crip + "■"
        elif letra in "*": crip = crip + "Ӥ"
        elif letra in "Àà": crip = crip + "Ց"
        elif letra in "Úú": crip = crip + "|"
        elif letra in "Óó": crip = crip + "╚"
        elif letra in "Õõ": crip = crip + "Æ"
        elif letra in "Íí": crip = crip + "Ø"
        elif letra in "Éé": crip = crip + "⅜"
        elif letra in "Áá": crip = crip + "§"
        elif letra in "Çç": crip = crip + "ƒ"
        elif letra in "Ãã": crip = crip + "{"
        elif letra in "*": crip = crip + "↨"
        elif letra in "!": crip = crip + "☻"

        else:
            crip = crip + letra
    return crip
barra()
print(cripto(input("Digite sua frase para ser criptografada: ")))

barra()
def descr(lul):
    test = " "
    barra()
    for letra2 in lul:
        if letra2 in "!": test = test + "A"
        elif letra2 in "@": test = test + "B"
        elif letra2 in "#": test = test + "C"
        elif letra2 in "$": test = test + "D"
        elif letra2 in "%": test = test + "E"
        elif letra2 in "&": test = test + "F"
        elif letra2 in "*": test = test + "G"
        elif letra2 in "(": test = test + "H"
        elif letra2 in ")": test = test + "I"
        elif letra2 in "-": test = test + "J"
        elif letra2 in "+": test = test + "K"
        elif letra2 in "=": test = test + "L"
        elif letra2 in "/": test = test + "M"
        elif letra2 in "Ὧ": test = test + "N"
        elif letra2 in "₽": test = test + "O"
        elif letra2 in "∆": test = test + "P"
        elif letra2 in "┬": test = test + "Q"
        elif letra2 in "Ψ": test = test + "R"
        elif letra2 in "Ω": test = test + "S"
        elif letra2 in "Ϋ": test = test + "T"
        elif letra2 in "ϓ": test = test + "U"
        elif letra2 in "ϕ": test = test + "V"
        elif letra2 in "Ϙ": test = test + "W"
        elif letra2 in "Ю": test = test + "X"
        elif letra2 in "Ѡ": test = test + "Y"
        elif letra2 in "ш": test = test + "Z"
        elif letra2 in "■": test = test + "Ô"
        elif letra2 in "↨": test = test + "*"
        elif letra2 in "Ց": test = test + "À"
        elif letra2 in "|": test = test + "Ú"
        elif letra2 in "╚": test = test + "Ó"
        elif letra2 in "Æ": test = test + "Õ"
        elif letra2 in "Ø": test = test + "Í"
        elif letra2 in "⅜": test = test + "É"
        elif letra2 in "§": test = test + "Á"
        elif letra2 in "ƒ": test = test + "Ç"
        elif letra2 in "{": test = test + "Ã"
        elif letra2 in "в": test = test + "."
        elif letra2 in "Ѭ": test = test + ","
        elif letra2 in "д": test = test + ":"
        elif letra2 in "☻": test = test + "!"
        else:
            test = test + letra2
    return test

print(descr(input("Copie e cole sua frase pra ser discriptografada: ")))
barra()