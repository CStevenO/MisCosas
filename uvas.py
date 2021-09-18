def suficientes_uvas(cantidad_ivan,cantidad_nicolas,cantidad_adriana,cantidad_verdes,cantidad_moradas,cantidad_negras):
    if(cantidad_ivan <= cantidad_verdes):   #felices o casi o fallamos
        cantidad_verdes -= cantidad_ivan
        if(cantidad_nicolas <= cantidad_verdes+cantidad_moradas): #felices o casi
            total = cantidad_negras + cantidad_verdes + cantidad_moradas - cantidad_nicolas
            if(cantidad_adriana<=total):    #felices
                return "felices"
            else:                           #casi
                return "casi"
        else:                               #casi o fallamos
            if(cantidad_adriana<=cantidad_negras):  #casi
                return "casi"
            else:                           #fallamos
                return "fallamos"
    else:                                   #casi o fallamos o al menos somos amigos
        if(cantidad_nicolas <= cantidad_moradas):   #casi o fallamos
            total = cantidad_negras + cantidad_moradas - cantidad_nicolas
            if(cantidad_adriana <= total):   #casi
                return "casi"
            else:                           #fallamos
                return "fallamos"
        else:                               #fallamos o al menos somos amigos
            if(cantidad_adriana <= cantidad_negras):
                return "fallamos"
            else:
                return "al menos somos amigos"

print(suficientes_uvas(30,25,35,20,20,20))
