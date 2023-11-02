def palindromo (texto):
    texto_compact = texto.lower().replace(" ","")
    return texto == texto[::-1]     
    

print("abbsa",palindromo("abbsa"))
print("abba",palindromo("abba"))     