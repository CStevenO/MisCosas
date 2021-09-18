def clasificar_regalo(id):
    numero = str(id)
    rever = numero[::-1]
    if numero == rever:
        if id%2 == 0:
            return "boy"
        else:
            return "girl"
            
    else:
        if id%2 == 0:
            return "man"
        else:
            return "woman"
